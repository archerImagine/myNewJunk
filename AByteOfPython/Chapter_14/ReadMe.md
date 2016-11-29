# Chapter 14 | Exceptions #

**Exceptions** occurs due to exceptional situation occurs in the program, which is very rare to happen. When such situation happens Python **raises** its hands to tell about the **error**.

## Errors ##

What will be the error in this line of code

````python
Print "Hello World!"
````

It gives the error

````python
File "example01.py", line 1
    Print "Hello World"
                      ^
SyntaxError: invalid syntax
````

As you can see a `SyntaxError` is raised.

## Exceptions ##

Consider the below code:-

````python
s = raw_input("Enter Something -----> ")
````

When the console is waiting to receive keys, press `Ctril + D`, we will get a `EOFError` which is really an exceptional situation.

## Handling Exceptions ##

We can handle exception using `try ... except ` statement.

Put the normal statement inside the `try` block and all error handlers in `except ` block.

Consider this code:-

````python
try:
    text = raw_input("Enter Something ---> ")
except EOFError:
    print "Why did you do an EOF on me?"
except KeyboardInterrupt:
    print "You cancelled the operation"
else:
    print "you entered {}".format(text)
````

What we are doing in the above code is:-
* Putting all the error prone code, in the `try` block.
* Then have respective handlers for error which we are expecting in the `expect ` block.
    - If a `except ` block has no name exception, it will handle all error.
    - There should be atleast on `except ` block.
* If the program does not handle the errors, it will be done by python default handlers.
* The `else` clause is executed when not error occurs.

## Raising Exception ##

We can also raise our own exception, for situation which are unique to our program, this can be done by using `raise ` statement, providing it with a name of exception and the object.

This new exception we we are throwing should be a derived class of `Exception `.

Here is an example of raising the exception.

````python
class ShortInputException(Exception):
    """A User defined exception class."""
    def __init__(self, length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = raw_input('Enter Something -----> ')
    if len(text) < 3:
        raise ShortInputException(len(text),3)
except EOFError:
    print "Why did you do an EOF on me? "
except ShortInputException as ex:
    print "ShortInputException: The input was {0} long, expected atleast {1}".format(ex.length,ex.atleast)
else:
    print "No Exception was raised."
````

In the above code, we have made our own exception which is `ShortInputException`, and then in the `try` block we raise that exception, if the condition is true.

## Try .. Finally ##
We are reading a file inside the try block, and till now what we have seen are error handlers and `else` condition, but what about a condition, irrespective of what happens, the book has to be closed `finally`.

This is achieved from `finally` block.

Consider the below example.

````python
import sys,time

f = None

try:
    f = open("poems.txt")

    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,
        sys.stdout.flush()
        print "Press Ctrl + C now"

        time.sleep(2)
except IOError:
    print "Could Not find file poems.txt"
except KeyboardInterrupt:
    print "!! You cancelled the reading from the file."
finally:
    if f:
        f.close()
    print "Cleaning up: Closed the file"
````

In the above code, we are trying to open a file name `poems.txt`, if the file is present we will print the lines in the files, and there is a sleep, during this time, we can press `CTRL + C`, so we can check, even there is an exception, `finally` block is executed and the file is closed.

## The with Statement ##

The previous example of opening a file in `try` block and closing the file in `finally ` block, is a very common pattern. Hence we can use the `with` statement which is much cleaner.

Consider this code:-

````python
with open('poems.txt') as f:
    for line in f:
        print line,
````
When we use the `with` statement, we have two things to note.

* It always calls `thefile.enter` before the block is executed.
* It always calls `thefile.exit` after finishing the block.