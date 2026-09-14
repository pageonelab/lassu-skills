#!/usr/bin/env python3
"""Build portable, deterministic skill/plugin artifacts without third-party code."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('lassu-record-video', 'lassu-edit-screenshot')

def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=True) + '\n').encode()

def generated(root=ROOT):
    version = (root / 'VERSION').read_text(encoding='utf-8').strip()
    metadata = dict(name='lassu', version=version,
        description='Record concise narrated videos and edit screenshots with the local Lassu app.',
        author={'name': 'PageOneLab'}, skills='./skills/')
    codex = dict(metadata, interface=dict(displayName='Lassu',
        shortDescription='Narrated videos and screenshot editing.',
        longDescription='Use the signed-in Lassu desktop app to capture and produce videos or edit screenshots. Connect the app MCP server separately. Capabilities depend on the installed app.',
        developerName='PageOneLab', category='Productivity', capabilities=[],
        defaultPrompt='Record a concise narrated demonstration with Lassu.'))
    result = {
        'plugins/lassu/.codex-plugin/plugin.json': encoded(codex),
        'plugins/lassu/.claude-plugin/plugin.json': encoded(metadata),
        '.agents/plugins/marketplace.json': encoded({'name':'lassu', 'interface':{'displayName':'Lassu'},
            'plugins':[{'name':'lassu','source':{'source':'local','path':'./plugins/lassu'},
                'policy':{'installation':'AVAILABLE','authentication':'ON_INSTALL'},'category':'Productivity'}]}),
        '.claude-plugin/marketplace.json': encoded({'name':'lassu','owner':{'name':'PageOneLab'},
            'plugins':[{'name':'lassu','source':'./plugins/lassu','version':version,
                'description':metadata['description']}]}),
    }
    for skill in SKILLS:
        for path in sorted((root / 'skills' / skill).rglob('*')):
            if path.is_file():
                result['plugins/lassu/' + path.relative_to(root).as_posix()] = path.read_bytes()
    return result

def sync(root=ROOT, check=False):
    wanted = generated(root)
    actual = set(p.relative_to(root).as_posix() for p in (root/'plugins/lassu').rglob('*') if p.is_file())
    extras = actual - set(wanted)
    if extras:
        raise ValueError('Unexpected generated plugin files: ' + ', '.join(sorted(extras)))
    for name, data in wanted.items():
        path = root / name
        if check:
            if not path.is_file() or path.read_bytes() != data:
                raise ValueError('Generated file differs: ' + name + '; run python scripts/package.py sync')
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)

def validate(root=ROOT):
    version=(root/'VERSION').read_text(encoding='utf-8').strip()
    if not re.fullmatch(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)', version):
        raise ValueError('VERSION must be a stable semantic version')
    compatibility=json.loads((root/'compatibility.json').read_text(encoding='utf-8'))
    if compatibility['pluginVersion'] != version or compatibility['schemaVersion'] != 1:
        raise ValueError('Compatibility metadata/version mismatch')
    # Readiness fields are shared by both native apps. Capability containers
    # differ (macOS string array, Windows object) and are not installation gates.
    if compatibility.get('runtimeReadinessChecks') != {
        'lassu-record-video': 'canRecord', 'lassu-edit-screenshot': 'canScreenshot'
    } or 'requiredCapabilities' in compatibility:
        raise ValueError('Use shared native runtime readiness fields')
    if compatibility.get('automationProtocol') != {'min': 1, 'max': 1}:
        raise ValueError('Unvalidated automation protocol range')
    if set(compatibility.get('platforms', [])) != {
        'darwin-arm64', 'darwin-x64', 'win32-arm64', 'win32-x64'
    }:
        raise ValueError('Platform metadata must match validated native targets')
    for name in SKILLS:
        directory=root/'skills'/name
        text=(directory/'SKILL.md').read_text(encoding='utf-8')
        if not text.startswith('---\nname: '+name+'\ndescription: ') or '\n---\n' not in text[4:]:
            raise ValueError('Invalid skill frontmatter: '+name)
        if len(text.splitlines()) > 200:
            raise ValueError('Keep the main skill concise: '+name)
        if re.search(r'/Applications/[^\s`]+\.app|macOS requires Node\.js', text):
            raise ValueError('Legacy platform-specific setup in portable skill: '+name)
        for link in re.findall(r'\]\(([^)]+)\)',text):
            if '://' in link or link.startswith('#'):
                continue
            target=(directory/link.split('#')[0]).resolve()
            if not target.is_relative_to(directory.resolve()) or not target.is_file():
                raise ValueError('Broken or escaping skill reference: '+link)
    for path in root.rglob('*'):
        relative=path.relative_to(root)
        if any(part in {'.git','dist','__pycache__','.venv'} for part in relative.parts):
            continue
        if path.is_symlink():
            raise ValueError('Symlinks are not portable: '+str(relative))
        if not path.is_file():
            continue
        data=path.read_bytes()
        if len(data)>1024*1024:
            raise ValueError('Source file exceeds 1 MiB: '+str(relative))
        text=data.decode('utf-8')
        # English-only repository policy: reject CJK, including comments and fixtures.
        if re.search('[\u3400-\u9fff\uf900-\ufaff]',text):
            raise ValueError('Non-English CJK content: '+str(relative))
        if re.search(r'/' + r'Users/[^/\s]+|[A-Za-z]:[\\/]+Users[\\/]+[^\\/\s]+',text):
            raise ValueError('Personal machine path in source: '+str(relative))
    if (root / '.git').exists():
        messages = subprocess.run(['git', 'log', '--format=%B'], cwd=root, check=True, capture_output=True, text=True).stdout
        if re.search('[\u3400-\u9fff\uf900-\ufaff]', messages):
            raise ValueError('Commit messages must be in English')
    sync(root,check=True)

def archive(destination, files):
    with zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_STORED) as z:
        for name,data in sorted(files.items()):
            info=zipfile.ZipInfo(name, date_time=(2026,1,1,0,0,0))
            info.create_system=3
            info.external_attr=0o100644 << 16
            info.compress_type=zipfile.ZIP_STORED
            z.writestr(info,data,compress_type=zipfile.ZIP_STORED)

def build(root=ROOT, destination=None):
    validate(root)
    version=(root/'VERSION').read_text(encoding='utf-8').strip()
    out=destination or root/'dist'
    out.mkdir(parents=True,exist_ok=True)
    common={name:(root/name).read_bytes() for name in ('LICENSE','VERSION','compatibility.json')}
    skills={p.relative_to(root).as_posix():p.read_bytes() for p in (root/'skills').rglob('*') if p.is_file()}
    archive(out/f'lassu-skills-{version}.zip',common|skills)
    archive(out/f'lassu-plugin-{version}.zip',common|generated(root))
    artifacts=[]
    for name in (f'lassu-plugin-{version}.zip',f'lassu-skills-{version}.zip'):
        data=(out/name).read_bytes()
        artifacts.append({'name':name,'sha256':hashlib.sha256(data).hexdigest(),'size':len(data)})
    (out/'release.json').write_bytes(encoded({'schemaVersion':1,'version':version,'artifacts':artifacts}))
    entries=artifacts+[{'name':'release.json','sha256':hashlib.sha256((out/'release.json').read_bytes()).hexdigest()}]
    (out/'SHA256SUMS').write_bytes(''.join(f"{a['sha256']}  {a['name']}\n" for a in entries).encode('ascii'))
    return out

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['sync','check','build'])
    args=parser.parse_args()
    if args.command=='sync': sync()
    elif args.command=='check': validate()
    else: print(build())
