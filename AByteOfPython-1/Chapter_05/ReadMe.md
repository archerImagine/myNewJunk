# Chapter 05 | Basics #

Just printing a text is not what a programming languages is meant to do. We would want to take inputs, manipulate the inputs, output the manipulation, these all are some of the task which we try to accomplish from a programming languages.  Python is no different.

Some of the basics of how Python achieve this is explained in this chapter.

## Comment ##

**A code tells you how, but a comments tells why.** This is an apt interpretation on the use of comment. Code is meant to be understood by humans, comments comes a long way in helping to understand the code by humans.

The purpose of comment in source code is to.

* explain assumptions.
* explain important decisions.
* explain important details.
* explain the problem we are solving.

In a python a comment starts with the `#` symbols. We can provide comments in to ways.

````
print "Hello World"  # Note, print is a statement.
````

and

````
# Note, print is a statement.
print "Hello World"

````

## Literal Constant ##

Some example of Literals are.

* `5`, the number `5` is a literals.
* `1.23`, this floating point number is also a literal.
* `"This is a string"`, this string is also a literal.

Why we call all these as literals because these values never changes, a `5` is always `5` it cannot be `6` or `7`. Also literal are constant because we cannot change its value.


## Numbers ##

There are two type of numbers.

* integers.
    - The example of integers are numbers like `2`, `3`, `1234`. Integers are whole number.
* floats.
    - The example of floats are numbers like `3.14`, `1.234` also the `E` notation like `53.4E-4`

There is no `long` type in python.


## Strings ##
A *string* is a sequence of characters.

### Single Quote ###

We can specify the string with single quote, `'This is a string'`

### Double Quote ###

We can also have strings surrounded by `""`, `"This is a string"`

### Triple Quote ###

We can also use `""" """` to have multi line strings. We can also use it as doc strings.

### Strings are immutable ###

Each and every string are immutable, i.e we cannot change the same string, we can though copy it and modify a copy of that string.

### format method ###

When we need to construct string from dynamic information, the `format()` method comes to our rescue.

````
name = "Swaroop"
age = 10

print '{0} was {1} years old when he wrote this book'.format(name, age)
````

In the above example, we have specified `{0}` and `{1}` as specification, which are replaced by the arguments passed to the `format()`, which are `name ` and `age `.

The numbers in the specification are optional, also we can have named specification like `{name}` and `{age}` and pass the parameters to `format()` as named argument like `.format(name="Swaroop", book="A Byte of python")`.

We can also have different variant to specification.

* `'{0:.3f}'.format(1.0/3)` : decimal precision of 3 for float 0.333
* `'{0:_^11}'.format('hello')` : fill with _ and the text centered.


By default, there is a new line character introduced to the `print ` statement, if we do not want the new line character we can do.

````
print 'a',
print 'b'
````

### Escape Sequence ###

We can also escape the normal behavior by the use of `\` character.

* `\n` : for new line
* `\t` for tabs.
* `\'` to escape the `'` in a single quote string.

### Raw String ###

If we want a string to behave just like a string without the escape sequence we can use the string appended with `r` like `r"NewLines are indicated by \n"` will output like `NewLines are indicated by \n`

The raw string is very helpful in case of using regular expression.

## Variable ##

Working with only literals become very boring and tedious over a period of time, we should have some way to store values and manipulate them. Variables comes to our help in the regards.

We can store anything in a variables, and then use it in the program to manipulate the values. 

We have to name these variables so we can use these. 

### Identifier Naming ###

The rules governing the identifier naming are:-

* The first character should be alphabet, Unicode, or underscore `_`
* The rest of the character can follow with alphabet, unicode, underscore or digits.
* Identifier name are case sensitive.


## Logical and Physical line ##

A Physical line, what we see when we write a python program, A logical line is what python sees as a single statement.

* `print 'hello world'`: This is both a physical and logical line.
* `i = 5; print i;` : This is a physical line, but also a logical line.


## Indentation ##

Indentation is of paramount importance in Python. Each block of code is represented by the amount of indentation.

Two block of code with the same level of indentation are of the same level, we can create blocks of code with the help if flow statement.

Python uses 4 spaces for indentation.

The below code will give an error.

````
i = 5

print "The value of i = ", i
    print i
````


