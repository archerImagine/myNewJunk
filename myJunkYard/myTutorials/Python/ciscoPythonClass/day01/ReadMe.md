# Python Day 1 #
## What is Python ##

* Rapid proto typing as faster development.
* A dynamic multi paradigm programming language with support for procedural, functional and OO programming.
* Fastest learning curve.
* Modern, flexible and highly feature-rich with emphasis on programmer productivity.


## Features of Python ##

* Scalable
* Highly extensible. 
* Rich set of library.
* Automatic garbage collection.
* Support of run time error handling (exception)
* Design philosophy emphasizes on code readability and consistency.

## History of Python ##

## The Zen of Python, by Tim Peters ##

* Beautiful is better than ugly.
* Explicit is better than implicit.
* Simple is better than complex.
* Complex is better than complicated.
* Flat is better than nested.
* Sparse is better than dense.
* Readability counts.
* Special cases aren't special enough to break the rules.
* Although practicality beats purity.
* Errors should never pass silently.
* Unless explicitly silenced.
* In the face of ambiguity, refuse the temptation to guess.
* There should be one-- and preferably only one --obvious way to do it.
* Although that way may not be obvious at first unless you're Dutch.
* Now is better than never.
* Although never is often better than *right* now.
* If the implementation is hard to explain, it's a bad idea.
* If the implementation is easy to explain, it may be a good idea.
* Namespaces are one honking great idea -- let's do more of those!



You can get this by using

````python
import this
````

## What can we use python for? ##
* General application development.
* Scripting for complex scripts.
* Automation and testing tools.
* System programming. (glue layer)
* Cross platform GUI Development (WxPython,PyGTK,Glade-Python, PyQt, **Kivy**)
* Web Devlopment (DJango, Zope)
* Internet Programing - web robots
* Network programming.


## Python Implementations ##
* Jython - Sun
* IronPython - Microsoft.
* PyPy

## Current State of python ##

Currently python(CPython) is available in two version.

* 2.76 : maintains backward compatibility on 2.x version
* 

## Platform Support ##

* it is not platform independence, but platform neutral.

## Statements in Python ##
### Simple Statement ###
* Ends with newline

* Print tuple, everything has a string representation, delimit with space and adds new line to the end.
* `,` adds two line of print statement.
`print 10,"hello",3.4,7.6`

* Prints to standard err
`print >>stderr`



### Complex statements ###


## Variables ##

````
a = 10
````

* All variable are references, like void *
* variables are untyped.
* All assignments are reference assignment.
* the below gives the type of value stored just now.
````
type(a)
````

* comma separated values are **tuple**
````
a = 10,20,30
a[0]
len(a)
````

* tuple unpack/packing
````
a = 10,20,30
b,c,d = a
b,c = a #error
````

* parallel assignment, below example a = 10, b = 20

````
a,b= 10,20

a,b = 10,20
a,b = 5,a+10

value a = 5
value of b = 20
````
* swapping
````
a,b = 10,20
a,b = b,a
````
* Assignment chain loading
````
a = b = c = 10
````

````
a = 10
a += 5;
a
````


* You cannot have assignment as part of expression in right side.

## References ##

* Variables
* Attributes of an object
* Index of a sequence
* Key of a mapping

* `del` deletes the reference of object. accessing a variable not defined is a **NameError**
````
a = 10
del a
````
* del deletes an reference and not the actual object
````
rec = ["john",45,"Bangalore"] #list, can be deleted
rec = "john",45,"bangalore" #cannot delete
````
* del is not used to delete a variable.

## Modules ##

* Load a module
* when imported a module, it creates a modules object, so you can access the attributes.
````
import module1
#use module1 in the file.
````
* when we import a module, it creates a `.pyc` file.
* Import modules as a name.
````
import module1 as myName
````
* Import need not be first statement in the file.
* No variable Hosting in python.
* Modules are singleton.
* Find attributes of a module/object use `dir()`
* No differences between a data and function in python, both are attributes.
* We can even import one member from a module using `from module1 import name` name will be accessible or `from module1 import name as myName` myName is accessible pointing to name.
* do not do this `from module1 import *` as it will remove current namespace.

## Pass ##
* have empty statement in a block.

----

# Post Lunch #
## Compound Statement ##
### Conditional Statements ###

* bool is a inbuilt data type
* `a<>b` only in python2
* `a is b`, will return true, if both refer to the same object.
* number and string equality should be checked with `==` and not `is`

````
a = "Hello World"
b = "Hello World"
a == b #TRUE, Data Comparison
a is b #False, Reference comparison.
````
Does not work for this

````
a = "Hello"
b = "Hello"
a = b #True
a is b #True, because the HashCode is done, because there is no space for CRC to trigger.
````
* `a is not b`
* `a in b`, find if a is present in a collection/tuple.
````
a = 44,55,66,77,88,99
55 in a
````
* `a not in b`, reverse of above.
* Combine multiple boolean for short circuit `not` , `and`,`or`
* Strict indendation is there in python, in place of {}

* `id(a)` will return a unique identifier, like address.
````
a = 10
c = a
a is c #TRUE
id(a) == id(c) #True, both should be same
````
* `hash(a)` gives the hash code, mostly hash code is same as the container.
````
a = 10
b = 20
hash(a)
hash(b) #Both return the same hash code. 
````

* `help(sys.getrefCount)` for help on any api.

* `c = a if a > b else b`, is a ternary operator.

````
if [boolean-expression]:
    <true-statement1>
elif [another-boolean-expression]:
    <true-statements2>
````

### Loop ###

* all loops have a `else` condition.
* `for` is use to iterate over a collection.
                


## Question ##
* Replacement for Matlab.
* any reading guides.

## Links ##
* [REPL](http://repl.it/languages)
* [Matlab Replacement](http://www.scipy.org/)
* [Mayavi](http://mayavi.sourceforge.net/)
* [Blender](http://www.blender.org/documentation/blender_python_api_2_70_5/)
* [Python Style Guide](http://legacy.python.org/dev/peps/pep-0008/)
* [Python Challenge](http://www.pythonchallenge.com/)




