# Chapter 08 | Functions #

## Introduction ##

Functions are reusable piece of code, The use of function is to give a name to a block of code. So this block of code can be executed multiple time when we invoke the function by using its name.

`len()` & `range()` are two function which we have already seen.

Here is a sample implementation of a function.

````
def sayHello():
    # Block belong to function
    print "Hello World"
# End of function
````
Few important things to remember from the above code:-

* Functions are defined using the keyword `def`
* The `def` keyword is followed by an identifier which is the function name.
* Identifier name is followed by pair of parentheses, which may include some variables names called parameters.
* Finally it has `:` to indicate the start of block
* Next is the block which is part of the Function.

## Functions Parameters ##

A Function can take parameters, which values are consumed by the function to produce some outputs. Parameters are similar to variables, just the only difference that Parameters can be never be without a initial value unlike variable.

Parameters are specified within the parentheses of the function definition separated by comma. When the function are invoked it has the arguments in the same order.

The names given in the function definition is called parameters, and the value we supply while calling are called arguments.

Here is an example of the both:-

````
def printMax(a,b):
    if a > b:
        print a, " is maximum. "
    elif a == b:
        print a, " is equal to ", b
    else:
        print b, "is maximum"

# Directly Pass the Literal Value

printMax(3,4)

x = 5
y = 7

# Pass the variable as arguments.
printMax(x,y)
````

## Local Variables ##

The variable declared inside a function is called **local variables**, as it cannot be accessed outside the function. This is called **Scope** of the variable.

If there is already a similar variable in the program, the local variable will take preference.

Here is an example showing the use of local variable:-

````
x = 50

def sampleFunction(x):
    print "x is ", x
    x = 2
    print "Changed local x to ", x

sampleFunction(x)
print "x is still ", x  # X value does not changes here.
````

## The `global ` statement ##

In the previous segment, if we had to change the value of the `x` which is outside the function scope, we have to use the `global` keyword. This practice is not encouraged.

Here is an example of use of `global`
````
x = 50

def sampleFunction():
    global x
    print "x is ", x
    x = 2
    print "Changed global x to ", x

sampleFunction()
print "Value of x is ", x   
````

## Default Argument Value ##

These feature is quite unique in Python, Suppose we want to have multiple arguments in a function, but not always we want to invoke the function with these many arguments, so when we do not invoke the function with these arguments, it should take some default values.

We can specify the default arguments value for parameters by appending `=` with the default values.

The default arguments value should be immutable i.e. it should not change.

````
def sayMessage(message,times=1):
    print message * times

sayMessage("Hello")
sayMessage("World ",5)
````

The parameters at the end only can be assigned the default arguments values.

## Keyword Arguments ##

Mostly we specify the arguments to function in the order in which there are mentioned in the function definition, But in python, we can specify the parameters while calling and assign values to them, so the order is not important. This is called keyword Arguments.

````
def sumNumbers(a,b,c,d,e):
    print a,b,c,d,e # prints 4 5 6 2 3
    return a +b +c +d +e

print sumNumbers(4,5,6, e=3,d=2)
```` 

So combining Keyword Arguments and Default arguments we can pass some value and ignore others if they have default arguments.

````
def func(a,b=5,c = 10):
    print "a is ",a, " and b is ", b, "and c is ", c

func(3,7)   
func(25,c=24)
func(c=50,a=100)
````

## VarArgs Arguments ##

We might also need the arguments to be of variable length. This are called **VarArgs** Arguments.

````
def total(initial=5,*numbers,**keywords):
    count = initial
    print "numbers:",numbers
    print "keywords", keywords
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print total(10,1,2,3,vegetables=50,fruits = 100)
````

* When we declared a starred parameter such as `*param`, then all the positional arguments from that points are collected in a tuple till the end.
* When we declare a double starred parameter such as `**param`, then all the keyword arguments from that point till end is collected in a dictionary.

## The `return ` statement ##

The `return ` statement are used to return the control back to the main program from a function, or to receive some values from a function.

````
def maximum(x,y):
    if x > y:
        return x
    elif x == y:
        return "The numbers are equal."
    else:
        return y

print maximum(2,3)
````

Every function by default returns a `return None`, in the absence of a return statement.

## DocString ##

Python has a feature formally called **documentation string.**, but most fondly called as **DocString.** It helps to understand the documentation of the function.

This docstring is used in both the `help()` method and also the `__doc__` string.

Here is an example.

````
def print_max(x,y):
    """
        Prints the Maximum of two numbers.
        The two values must be integers.
    """
    # convert to integers, if possible
    x = int(x)
    y = int(y)
    if x > y:
        print x, "is maximum."
    else:
        print y, "is maximum."

print_max(3,5)

print print_max.__doc__
help(print_max)
````