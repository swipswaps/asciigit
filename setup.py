import sys
from setuptools import setup

setup (
    name = "asciigit",        # what you want to call the archive/egg
    version = "0.1",
    packages=['src'],
    install_requires=[
        'asciimatics',
        'GitPython'
    ],
    entry_points = {
        "console_scripts": [        # command-line executables to expose
            "asciigit = src.main:main",
        ],
    }
)