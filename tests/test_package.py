import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('package',ROOT/'scripts/package.py')
package=importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)

class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'source'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','dist','__pycache__'))

    def test_release_is_reproducible_and_self_contained(self):
        a=package.build(self.root,Path(self.temp.name)/'first')
        b=package.build(self.root,Path(self.temp.name)/'second')
        self.assertEqual({p.name:p.read_bytes() for p in a.iterdir()},
                         {p.name:p.read_bytes() for p in b.iterdir()})
        metadata=json.loads((a/'release.json').read_text(encoding='utf-8'))
        for artifact in metadata['artifacts']:
            raw=(a/artifact['name']).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(),artifact['sha256'])
            self.assertEqual(len(raw),artifact['size'])
            self.assertLess(len(raw),1024*1024)
            with zipfile.ZipFile(a/artifact['name']) as z:
                self.assertIsNone(z.testzip())
                self.assertEqual(z.namelist(),sorted(z.namelist()))
                self.assertTrue(all(not n.startswith('/') and '..' not in n.split('/') for n in z.namelist()))
                self.assertFalse(any(n.endswith('.mcp.json') for n in z.namelist()))
                prefix='plugins/lassu/' if 'plugin-' in artifact['name'] else ''
                for skill in package.SKILLS:
                    self.assertIn(prefix+'skills/'+skill+'/references/connection.md',z.namelist())

    def test_modified_generated_skill_fails(self):
        path=self.root/'plugins/lassu/skills/lassu-record-video/SKILL.md'
        path.write_text(path.read_text(encoding='utf-8')+'Changed instructions.\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'Generated file differs'): package.validate(self.root)

    def test_missing_reference_fails(self):
        (self.root/'skills/lassu-record-video/references/connection.md').unlink()
        with self.assertRaisesRegex(ValueError,'Broken or escaping'): package.validate(self.root)

    def test_escaping_reference_fails(self):
        path=self.root/'skills/lassu-record-video/SKILL.md'
        path.write_text(path.read_text(encoding='utf-8')+'[outside](../../LICENSE)\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'Broken or escaping'): package.validate(self.root)

    def test_english_policy_includes_documentation(self):
        (self.root/'docs/invalid.md').write_text(chr(0x4e2d), encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'Non-English'): package.validate(self.root)

    def test_version_mismatch_fails(self):
        (self.root/'VERSION').write_text('0.2.0\n')
        with self.assertRaisesRegex(ValueError,'mismatch'): package.validate(self.root)

    def test_legacy_platform_setup_fails(self):
        path=self.root/'skills/lassu-record-video/SKILL.md'
        original=path.read_text(encoding='utf-8')
        for directive in ['Use /Applications/'+'Lassu.app.', 'macOS requires '+'Node.js 22.']:
            path.write_text(original+'\n'+directive, encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'Legacy platform-specific'): package.validate(self.root)

    def test_windows_personal_path_fails(self):
        path=self.root/'docs/invalid.md'
        for separator in ['\\', '\\\\', '/']:
            path.write_text(separator.join(['C:', 'Users', 'example', 'private']), encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'Personal machine path'): package.validate(self.root)

    def test_directory_symlink_fails(self):
        path=self.root/'docs/linked'
        try:
            path.symlink_to(self.root/'skills', target_is_directory=True)
        except OSError as error:
            self.skipTest('Directory symlink privilege is unavailable: '+str(error))
        with self.assertRaisesRegex(ValueError,'Symlinks are not portable'): package.validate(self.root)

    def test_readiness_metadata_matches_both_native_status_shapes(self):
        metadata=json.loads((self.root/'compatibility.json').read_text(encoding='utf-8'))
        # Representative authenticated responses from the native status handlers.
        for status in [
            {'canRecord': False, 'canScreenshot': True, 'capabilities': ['display', 'window', 'screenshot']},
            {'canRecord': False, 'canScreenshot': True, 'capabilities': {'recording': True, 'screenshot': True}},
        ]:
            checks=metadata['runtimeReadinessChecks']
            self.assertFalse(status[checks['lassu-record-video']])
            self.assertTrue(status[checks['lassu-edit-screenshot']])
        metadata['runtimeReadinessChecks']['lassu-edit-screenshot']='screenshots'
        (self.root/'compatibility.json').write_text(json.dumps(metadata), encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'readiness'): package.validate(self.root)

    def test_unexpected_executable_or_mcp_config_fails(self):
        (self.root/'plugins/lassu/.mcp.json').write_text('{}')
        with self.assertRaisesRegex(ValueError,'Unexpected'): package.validate(self.root)

    def test_two_marketplaces_resolve_identical_plugin(self):
        c=json.loads((self.root/'.agents/plugins/marketplace.json').read_text(encoding='utf-8'))
        a=json.loads((self.root/'.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
        self.assertEqual(c['plugins'][0]['source']['path'],a['plugins'][0]['source'])
        self.assertEqual(c['name'],a['name'])
        self.assertEqual(c['plugins'][0]['policy']['installation'],'AVAILABLE')

if __name__=='__main__': unittest.main()
