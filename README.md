My-Python-Boilerplate
=================================================
[![Build Status](https://travis-ci.org/martelogan/my-python-boilerplate.svg?branch=master)](https://travis-ci.org/martelogan/my-python-boilerplate)

Description
-------------

This repo, constructed from Kenneth Reitz's [sample python boilerplate](https://github.com/kennethreitz/samplemod), serves as a template for python projects developed by Logan Martel (github username: [martelogan](https://github.com/martelogan)).

Creating a Project from this Skeleton
-------------

The following table illustrates steps required to setup a basic python project from this skeleton:

## Status of Skeleton Tasks

- [x] Clone this template project
- [ ] Find & Replace all instances of _My-Python-Boilerplate_ (case-sensitive) with your project name
- [ ] Find & Replace all instances of _my-python-boilerplate_ (case-sensitive) with your project name
- [ ] Find & Replace all instances of _my_python_boilerplate_ (case-sensitive) with your project name
- [ ] Modify this README (and subdirectory READMEs) with general project documentation
- [ ] Modify project contributors as necessary under: [AUTHORS](AUTHORS), [setup.py](setup.py), [docs/conf.py](docs/conf.py), and all README citations
- [ ] Leverage existing directories as desired (e.g. data under data/, config under config/, etc.)
- [ ] Replace this README section with a project status checklist

Installation
-------------

1. Make sure you have all the dependencies needed to build this project. In particular, immediately after git clone, you should be able to successfully build 
the project from a command-line environment under **[Python 2.7](http://docs.python-guide.org/en/latest/starting/install/linux/)** 
via the command:
```bash
   python setup.py develop
```

2. The recommended IDE for developer consistency is [PyCharm](https://www.jetbrains.com/pycharm/). 
Leveraging PyCharm, it would be ideal for project contributors to ensure that code conforms to [PEP 8 standards](https://www.python.org/dev/peps/pep-0008/).

Development
------------

Our development workflow will be simple:

**Always develop on your own branch. Only merge code to Master via PR's. Only merge code that has no conflicts with master. Only merge code that builds successfully via _python setup.py develop_**.

Execution
------------

The first thing we do is import the module and get an ``ExampleClass`` 
object.

```python
   >>> from my-python-boilerplate import ExampleClass as Ex
   >>> example = Ex("hello")
   >>> ...
```


License
-------
This code is under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

If you use or modify _my-python-boilerplate_, please credit the original author as

* Logan Martel - https://github.com/martelogan
