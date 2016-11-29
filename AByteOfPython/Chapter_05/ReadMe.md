# Chapter 05 | Basics #

## Comments ##

Comments are any text to the right of `#`. Few examples of comments are as below,

````
print "Hello World!"    #prints hello world.

#Print is a statement.
print "Hello World!"
````

Comments are necessary for coding because always remember, human memory is a bitch, so always comment your code, at least to find why you wrote the code.

Few important points which a comment can address:-

* explain assumptions.
* explain important decisions.
* explain important details.
* explain problem's you are trying to solve.

Always remember [Code Tells You How, Comments Tell You Why ](http://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/)

## Literal Constants ##

These are some of literal constants, `5`,`1.23`,`This is a string.` These are called literals because, its value is used literally as number `2` always represents itself, i.e. it is a constant as the value does not change.

## Numbers ##

Python has two types of **Numbers**

1. **integers**
2. **floats**.

### Integers ###
The example of Integers are whole numbers like `2`.

### Floats ###
The floating numbers are number with decimal points, example like `1.25` and `24.3 E -4`

The `E` notation indicates power of `10`

> There is no long type in python.

## Strings ##

A string is a sequence of character within one of these type of quotes.

* Single Quotes `' '`
* Double Quotes `" "`
* Triple Quotes `""" """`

Here is an example of strings, `"This is a string"`

We can use the above 3 Quotes to specify string.

* Single Quotes `'This is Single Quote String'`
* Double Quotes `"This is Double Quote String"`
* Triple Quotes `"""This is Triple Quote String"""`
    - Triple Quotes can be uses to specify multi line strings.
    - You can also use `''' '''`, to specify triple quotes.

### String Mutability ###

Strings are Immutable, which means, once created we cannot change a string.

> There is no `char` type in Python.

### `format()` method ###

`format()` method help us to create a string from various other information.

````
age = 20
name = "Archer"

print '{0} was {1} years old, when he learned Python.'.format(name,age)
print 'why is {0} learning Python?'.format(name)
````
The piece of code like `{0}` and `{1}` are nothing but just similar to fill in the blanks type of question in our class exams, where the value is filled by the `.format()` arguments, `name` fills the blank at `{0}` and `age` fills the blank at `{1}`

> The numbers inside `{}` are optional.

More formally, python in the `format()` method substitute each argument value into the specification.

### Escape Sequence. ###

Suppose we have to specify `'` in a string, we can do this by this sample string.

````
"what's your name?"
````

But if you have to use only `'` and not `"` in your string, then we have a problem, To solve situation like this we can use **Escape Sequence**.

Here is how we could modify the string:

````
'what\'s your name?'
````

Some common escape sequence and its use:-

| Escape Sequence |      Purpose       |
| :-------------: | -----------------: |
|        \\       | escapes back slash |
|        \n       |           new line |
|        \'       |       single quote |
|        \"       |       Double Quote |
|        \r       |    Carriage return |
|        \t       |                Tab |

### Raw String ###

If we do not need any special processing in a string, like support of escape characters, we need a Raw String, which is denoted by prefixing with `r` char as shown below:-

````
myStr = r"Hello \n my dear"

print myStr
````

This will print:-

````
Hello \n my dear
````

>This raw string is very useful for processing regular expression.


## Variable ##

Only programming using Literals is difficult and possibly not much useful programs may be possible.

We need a method or techniques to store any information and then manipulate that information. This is were *Variables* are of help.

To use variables, we have to assign them names.

## Identifier Naming ##

Identifier is the name which a variable receives, so these are govern by some rules of python.

* The first character of the name should be an alphabet or `_`
* The rest of the name can contain any alphaNumeric character and `_`
* Names are case sensitive, so `myName` is not same as `myname`.

## Data Type ##

Variables can store different type of information, which are called data types. Some of the data types are float, integers and string. We can also create our own data type using **Classes.**

## Object ##

In Python, every thing is a object, along with literal objects, numbers, strings etc.

## Logical and Physical Line ##

A physical line is what we see when we write a line of code. A logical line is when python sees something as a single statement. Primarily every physical line corresponds to a logical lines.

Example of a single logical and physical line:-

````
print "Hello World!"
i = 5
````

We can combine multiple logical lines into one physical line with the help of `;`

````
i = 5; print i;
````

> It is strongly recommended to have a single line of code per logical and physical line.


## Indentation ##
White space have special importance in Python, most at the beginning of the line of code.

Basically the initial whitespace are called Indentation, so a series of logical code are separated by Indentation.

Wrong level of Indentation, gives `IndentationError`.

Python does not have support for braces, try `from future import braces`

