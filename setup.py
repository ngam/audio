#!/usr/bin/env python
import os
import re
import sys
import shutil
import subprocess
from pathlib import Path
from setuptools import setup, find_packages
import distutils.command.clean

import torch
from tools import setup_helpers

ROOT_DIR = Path(__file__).parent.resolve()


def _run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, cwd=ROOT_DIR).decode('ascii').strip()
    except Exception:
        return None


def _get_version(sha):
    version = '0.11.0a0'
    if os.getenv('BUILD_VERSION'):
        version = os.getenv('BUILD_VERSION')
    elif sha is not None:
        version += '+' + sha[:7]
    return version


def _make_version_file(version, sha):
    sha = 'Unknown' if sha is None else sha
    version_path = ROOT_DIR / 'torchaudio' / 'version.py'
    with open(version_path, 'w') as f:
        f.write(f"__version__ = '{version}'\n")
        f.write(f"git_version = '{sha}'\n")


def _get_pytorch_version():
    if 'PYTORCH_VERSION' in os.environ:
        return f"torch=={os.environ['PYTORCH_VERSION']}"
    return 'torch'


class clean(distutils.command.clean.clean):
    def run(self):
        # Run default behavior first
        distutils.command.clean.clean.run(self)

        # Remove torchaudio extension
        for path in (ROOT_DIR / 'torchaudio').glob('**/*.so'):
            print(f'removing \'{path}\'')
            path.unlink()
        # Remove build directory
        build_dirs = [
            ROOT_DIR / 'build',
        ]
        for path in build_dirs:
            if path.exists():
                print(f'removing \'{path}\' (and everything under it)')
                shutil.rmtree(str(path), ignore_errors=True)


def _get_packages(branch_name, tag):
    exclude = [
        "build*",
        "test*",
        "torchaudio.csrc*",
        "third_party*",
        "tools*",
    ]
    exclude_prototype = False
    if branch_name is not None and branch_name.startswith('release/'):
        exclude_prototype = True
    if tag is not None and re.match(r'v[\d.]+(-rc\d+)?', tag):
        exclude_prototype = True
    if exclude_prototype:
        print('Excluding torchaudio.prototype from the package.')
        exclude.append("torchaudio.prototype")
    return find_packages(exclude=exclude)


def _init_submodule():
    print(' --- Initializing submodules')
    try:
        subprocess.check_call(['git', 'submodule', 'init'])
        subprocess.check_call(['git', 'submodule', 'update'])
    except Exception:
        print(' --- Submodule initalization failed')
        print('Please run:\n\tgit submodule update --init --recursive')
        sys.exit(1)
    print(' --- Initialized submodule')


def _parse_sox_sources():
    sox_dir = ROOT_DIR / 'third_party' / 'sox'
    cmake_file = sox_dir / 'CMakeLists.txt'
    archive_dir = sox_dir / 'archives'
    archive_dir.mkdir(exist_ok=True)
    with open(cmake_file, 'r') as file_:
        for line in file_:
            match = re.match(r'^\s*URL\s+(https:\/\/.+)$', line)
            if match:
                url = match.group(1)
                path = archive_dir / os.path.basename(url)
                yield path, url


def _fetch_sox_archives():
    for dest, url in _parse_sox_sources():
        if not dest.exists():
            print(f' --- Fetching {os.path.basename(dest)}')
            torch.hub.download_url_to_file(url, dest, progress=False)


def _fetch_third_party_libraries():
    if not (ROOT_DIR / 'third_party' / 'kaldi' / 'submodule' / 'CMakeLists.txt').exists():
        _init_submodule()
    if os.name != 'nt':
        _fetch_sox_archives()


def _main():
    sha = _run_cmd(['git', 'rev-parse', 'HEAD'])
    branch = _run_cmd(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
    tag = _run_cmd(['git', 'describe', '--tags', '--exact-match', '@'])
    print('-- Git branch:', branch)
    print('-- Git SHA:', sha)
    print('-- Git tag:', tag)
    pytorch_package_dep = _get_pytorch_version()
    print('-- PyTorch dependency:', pytorch_package_dep)
    version = _get_version(sha)
    print('-- Building version', version)

    _make_version_file(version, sha)
    _fetch_third_party_libraries()

    setup(
        name="torchaudio",
        version=version,
        description="An audio package for PyTorch",
        url="https://github.com/pytorch/audio",
        author="Soumith Chintala, David Pollack, Sean Naren, Peter Goldsborough",
        author_email="soumith@pytorch.org",
        classifiers=[
            "Environment :: Plugins",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: BSD License",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX",
            "Programming Language :: C++",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: Implementation :: CPython",
            "Topic :: Multimedia :: Sound/Audio",
            "Topic :: Scientific/Engineering :: Artificial Intelligence"
        ],
        packages=_get_packages(branch, tag),
        ext_modules=setup_helpers.get_ext_modules(),
        cmdclass={
            'build_ext': setup_helpers.CMakeBuild,
            'clean': clean,
        },
        install_requires=[pytorch_package_dep],
        zip_safe=False,
    )


if __name__ == '__main__':
    _main()
