# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('docs/index.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='my-python-boilerplate',
    version='0.1.0',
    description='Boilerplate repository for python libraries.',
    long_description=readme,
    author='Logan Martel',
    author_email='logan.martel@outlook.com',
    url='https://github.com/martelogan/my-python-boilerplate',
    license=license,
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        # Specify the Python versions you support here.
        'Programming Language :: Python :: 2.7',
    ],
    # What does your project relate to?
    keywords= (
		'Python'
    ), 
    packages=find_packages(exclude=('tests', 'docs'))
)

