"""Minimal setup file for tasks project."""

from setuptools import setup, find_packages

setup(
    name='calclator',
    version='0.1.0',
    license='proprietary',
    description='Minimal Project Task Management',

    author='Brian Okken',
    author_email='Please use pythontesting.net contact form.',
    url='https://pragprog.com/book/bopytest',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=[],
    extras_require={},

    entry_points={
        'console_scripts': [
            'calclator = calclator',
        ]
    },
)

