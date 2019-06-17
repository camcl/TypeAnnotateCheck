# Type annotations in Python: The mypy static type-checker

The pieces of code stored here were initially written to present Type Annotations in Python and Static Type-Checking
during the PhDCircus event organized on 2019, May 24 at TDB.
The Jupyter/IPython Notebook _mypy\_examples.ipynb_ aimed to show live example of code run 
either with the mypy type checker or with the regular Python
interpreter.

## Getting Started

The repository contains, along the IPython code:
- _mypy.ini_: an example of configuration file for mypy,
- _mytuples.py_: a simple short piece of code for illustrating the use of mypy with Python (and not IPython),
- _mypycheck.py_: a piece of code for making mypy static type-checking usable with the IPython environment.

### Prerequisites

Python >= 3.5, for example on Ubuntu systems (further info at https://realpython.com/installing-python/)
```
$ sudo apt-get update
$ sudo apt-get install python3.x
```

Jupyter Notebook (Formerly known as the IPython Notebook)
```
$ python3 -m pip install --upgrade pip
$ python3 -m pip install jupyter
```
The installation of Jupyter Notebook above will also install the IPython kernel 
which allows working on notebooks using the Python programming language.


Alternatively,

IPython (Productive Interactive Computing), provides a kernel for Jupyter
```
$ pip install ipython
```

mypy

```
$ pip install mypy
```

### Installing

The installation of IPython should create a _.ipython_ folder at your system's home folder.

The code for the customized magic function _mypycheck.py_ has to be saved at 

```
 ~/.ipython/profile_default/startup/mypycheck.py
```

## Running the Jupyter Notebook

Once you have saved the files in a project folder, open a terminal and run

```
$ cd /path/to/project
$ jupyter notebook
```

This should open a new tab/window in your browser with a locally-hosted Jupyter server (_http://localhost:8888/tree_)
 and a list of the files you downloaded, including the _mypy\_examples.ipynb_ file. Open the that file.

The Jupyter Notebook is ready for running!

## References/Further Documentation

* https://docs.python.org/3/reference/compound_stmts.html#function
* https://docs.python.org/3/glossary.html#term-function-annotation
* https://www.python.org/dev/peps/pep-3107/
* https://docs.python.org/3/library/typing.html
* https://mypy.readthedocs.io/en/latest/index.html
* https://realpython.com/python-type-checking
* https://switowski.com/python/ipython/2019/02/15/creating-magic-functions-part3.html

## Authors

* **Camille Clouard** - *Initial work*