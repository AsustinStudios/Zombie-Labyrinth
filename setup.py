import os
import subprocess
import sys

import pkg_resources
import setuptools


this_dir = os.path.dirname(os.path.abspath(__file__))


def version():
    _version = None
    try:
        dot_git_dir = os.path.join(this_dir, '.git')
        if os.path.isdir(dot_git_dir):
            root = os.path.dirname(dot_git_dir)
            p = subprocess.Popen(['git', 'describe'], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, cwd=root)
            _version = p.communicate()[0].decode()
    except (OSError, ValueError):
        pass

    version_filename = os.path.join(this_dir, 'VERSION')
    if not _version:
        if os.path.isfile(version_filename):
            _version = open(version_filename, 'r').read()
        else:
            raise Exception("Could not determine version %s" %
                            version_filename)

    if '-' in _version:
        _version = _version.replace('-', '.post', 1).split('-')[0]

    with open(version_filename, 'w') as f:
        f.write(_version)

    return _version.strip()


def get_requirements(requirements_file: str) -> list[str]:
    reqs = []
    with open(requirements_file, 'r') as f:
        for req in f.readlines():
            req = req.strip()
            if not req or req.startswith('--') or req.startswith('#'):
                continue
            try:
                next(pkg_resources.parse_requirements(req))
            except ValueError:
                print('Ignoring requirement line "%s".' %
                      req.strip(), file=sys.stderr)
            else:
                reqs.append(req)
    return sorted(reqs)


setuptools.setup(
    name='zombie-labyrinth',
    version=version(),
    # don't use multi-line descriptions!
    description='2D TPS',
    license='GPLv3',
    url='https://github.com/AsustinStudios/Zombie-Labyrinth',
    author='Asustin Studios',
    author_email='studios@asustin.net',
    maintainer='Roberto Lapuente',
    maintainer_email='roberto@lapuente.me',
    packages=setuptools.find_packages(include=('src*',)),
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'zombie-labyrinth = src.main:main',
        ]
    },
    install_requires=get_requirements('requirements.txt'),
    extras_require={
        'tests': get_requirements('requirements-dev.txt'),
    },
    python_requires='>=3.10, <4',
    classifiers=[
        'Programming Language :: Python :: 3.10',
    ],
)
