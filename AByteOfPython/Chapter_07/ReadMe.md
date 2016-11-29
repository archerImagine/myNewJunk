# Chapter 07 | Control Flow #

All the code we have seen till now are series of statements executed in a sequence. Python executes this in a top down order. But we know we want code or programs which can take decision on its own.

This decision can be as simple as printing "Good Morning" or "Good Evening", based on some criteria.

These are achieved by the help of **Flow Control Statements.** There are 3 type of flow control statements:-

1. `if`
2. `for`
3. `while`

## The `if` statement ##

The `if` statement is used to check a condition, if the condition is **true**, we run a block of code statement (called `if` block), else we process another block of statement (called `else` block).

The `else` clause is optional. Here is an example showing the use of `if` statements.

````
number = 23

guess = int(raw_input('Enter an integer : '))

if guess == number:
    # New block starts here
    print "Congratulations, you guessed it."
    print "(but you do not win any prizes!)"
elif guess < number:
    # Another Block.
    print "No, it is litte higher than that."
else:
    print "No, it is litte lower than that."
print "Done"
````
Few things to note in the above code:-

* The `if` statement in `if guess == number:` ends with a `:`, indicating that a block statement follows.
* Each block of code is represented by a same level of indentation.
* The `elif` statement combines the need of two separate `if-else - if-else` statements. Also saving unnecessary indentation.

There is also a concept of nested `if` in which on `if` block is inside another `if` block.

The minimal valid `if` statement is

````
if True:
    print "Hello!"
````

## The `while` Statement ##

The `while ` statement allows you to repeatedly execute a block of code as long as the condition is True. This is what we call a **looping** statement.

A `while ` can also have an optional `else` statement.

Here is an example of the use of `while ` statement:-

````
number = 23
running = True

while running:
    guess = int(raw_input('Enter an integer : '))
    if guess == number:
        # New block starts here
        print "Congratulations, you guessed it."
        print "(but you do not win any prizes!)"
        running = False
    elif guess < number:
        # Another Block.
        print "No, it is litte higher than that."
    else:
        print "No, it is litte lower than that."
else:
    print "The while Loop is over."
print "Done"    
````
The code is same as the last code, only difference being because of the `while` statement, the check for correct number can be run multiple time.

The `else` block of the `while ` statement is executed after the `while ` block has completed. The `else` part will not be executed if `break ` from the `while ` loop.

## The `for ` Loop ##

The `for .. in` statement is another looping statement which iterates over a sequence of object.

The `for .. in` loops also have an optional `else` block, which is executed at the end of the `for` loop but is not executed if we `break` from the `for` loop.

Here is a sample `for` loop.

````
for i in range(1,5):
    print i
else:
    print "The loop is over."
````

## The `break ` statement ##
The `break` statement works like a explicit end to a loops, in addition to when the loop will manually exist.

Here is an example of `break ` statement,

````
while True:
    s = raw_input("Enter Something: ")
    if s == "quit":
        break
    print "Length of the string is ", len(s)
print "Done"
````

## The `continue ` statement ##

The `continue ` statement is used in a loop, to indicate that exit the remaining line of code and continue from next loop iteration. A very simple example of this will be:-

````
while True:
    s = raw_input("Enter Something : ")
    if s == 'quit':
        break
    if len(s) < 3:
        print 'Too Small '
        continue
    print 'Input is of sufficient length'
````


