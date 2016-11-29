# Chapter 09 | Modules #

## Introduction ##

We all know that we should always reuse code, the few ways of doing it are:-

* by writing reusable function.
* To have a module with resuable function.
* write the module in native language, and provide a python interface.

We will discuss in details the 2nd option which we have. To create modules the most simplest way is to create a `.py` file with functions in it.

This module which we created can be `import`**ed**, by another program to make use of these function.

The most simplest use of module can be understood by importing the `sys` module.

````
import sys

print ("the Command line arguments are: ")

for i in sys.argv:
    print i

print "\n\nThe PYTHONPATH is", sys.path,"\n"
````

Lets dissect the above code:-

* `import sys` : This tells python, that we want to use the functionality of this module called `sys`. 
    - Since `sys` is a built in module, the python interpreter knows where to find this module.
    - If it was not a standard module, it will search in `sys.path` directories.
    - Initialization is only done at the time of `import`
* `sys.argv` : This is a list of strings, which contains the command line arguments passed to the program.
    - The name of the script is always the first element of `sys.argv`
* `sys.path` : This contains the list of directory from which we can import modules.
    - The first output of the above is the current directory.

## Byte-compiled .pyc files ##

Importing modules is a very costly affair, so python has a trick to solve this problem. It creates a **Byte-Compiled ** files with extension as `.pyc` which is an intermediate form.

So the `.pyc` is created during the first `import` statements, subsequent imports gets the `.pyc` file.

The `.pyc` files are platform-independent.

## The `from ... import ` statement ##

We can also use statement like

````
from sys import argv
````

which will avoid writing `sys.` every time we want to access `argv`, but this will also prevent from having a local variable with the name `argv`.

So `import` statement are the suggested way to import, as we will avoid name clashes.

## A module's name ##

Every module have a name and statements in a modules can find out the name of their module.

Consider the below code:-

````
if __name__ == '__main__':
    print "This is run by itself."
else:
    print "This is being imported."
````

Every Python module has a `__name__` defines, if its name is `__main__` that implies that its is run standalone, else it is being imported.

## Making your own modules ##

Each `.py` is a module, and we can import it using its filename.

We even use the dot notation to access the members of the imported modules, which is very pythonic.

we can also use 

````
from mymodule import *
````

which will import all the public names, but not the private members.
## The `dir` function ##

We can use the `dir` function to list the identifiers that an object defines.

When we supply a name to `dir()`, it returns all the public interface. When we do not supply a name to `dir()` it gives public interface of the current module.

Consider the below code:-

````
import sys

print dir(sys)

a = 5
print dir()

del a

print dir()
````

We use the `del` keyword to delete a variable.

## Packages. ##

Modules are organized into packages. Packages are just folders with a special file called `init.py`.

## Further Reading ##

To read further about the `from sys import...` options kindly read these

* [Reddit | Difference between "from module import *" and "import module"?](http://www.reddit.com/r/learnpython/comments/1q1z2s/difference_between_from_module_import_and_import/)
* [Reddit | Difference between "import ____" and "from ___ import *"](http://www.reddit.com/r/learnpython/comments/22vs9c/difference_between_import_and_from_import/)
* [StackOverflow | Python import X or from X import Y? (performance)](http://stackoverflow.com/questions/3591962/python-import-x-or-from-x-import-y-performance)
