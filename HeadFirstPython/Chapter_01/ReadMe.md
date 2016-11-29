# Chapter 01 | Everyone loves List #

This is the first Chapter learning of Head First Python by Paul Barry, This markdown file is my notes for the first chapter, not sure if any copyright issues are there.

## Introduction ##

When starting learning a new language, we should always ask ourself why this is required?

Python is a great language, especially for beginners through which you can target Desktops, web, handhelds, servers along with GUIs. The syntax is very developer friendly.

We will use Python 3 for this course. 

When the initial setup for python development is over like.

* Configure Python 3.
* Choose you editor (IDE) of choice.
* Configure the IDE to use proper python interpreter.

Once the above task are over and you have execute a `"Hello World` program, we are ready for diving into the world of python.

## List ##

We are are interested in representing information in a list, everyone of us have one list of other, be it shopping list, book list, TODO list. Some list are very simple and some are very complex.

Python has a built in way of dealing with list. A basic python list looks like this.

* `movies = ["The Holy Grail", "The Life of Brain", "The Meaning of Life"]`

A list is created using.

* A variable name, `movies` in the above case.
* The list is enclosed in a `[]` square brackets.
* Within the square brackets we have the items of the list, separated by comma.
* Type information is not required in python, So `movies` does not have a type associated with itself.
* List are like arrays, so the items inside the List are indexed from `0`. We can access individual items by using this notation `movies[0]` will give `"The Holy Grail"`.

### List Methods ###

List as informed earlier can be like an array, but it is much more than that, it have a variety of methods which allows various functionality to list.

These links can act for your references.

* [Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
* [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)


Here are some important methods which can be used. The examples follows.

* `len()`
    - This method tells us about the length of the argument passed, if is `len(movies)` it will return `3`
* `append()`
    - This appends a single item to the existing list.
* `pop()`
    - This removes the last item of the existing list, and returns that value.
* `extend()`
    - Extend the list by appending all the items in the given list
* `remove()`
    - Searches and removes a specific item from the list.
* `insert()`
    - Inserts a item a predefined position.



 ````
 cast = ["Cleese", "Palin", "Jones", "Idle"]

 print(len(cast)) #Prints the value 4

 cast.append("Gilliam") # list is now ["Cleese", "Palin", "Jones", "Idle", "Gilliam"]

 cast.pop() # return "Gilliam", list is now ["Cleese", "Palin", "Jones", "Idle"]

 cast.extend(['Gilliam', "Chapman"]) # list is not ["Cleese", "Palin", "Jones", "Idle", 'Gilliam', "Chapman"]

 cast.remove('Chapman') # list is now ["Cleese", "Palin", "Jones", "Idle", "Gilliam"]

 cast.insert(0,"Chapman") # List is now ['Chapman', 'Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
 ````

The above code can be found [here](src/Page09.py)


Python list can also have inter mixed data type in the same list. 

* `movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gillman", 91,]`,  This is a perfect example of it.


### Iteration on List ###

The most primitive way of navigating the list is by the array index operation, but it is not extensible. Python have iteration over list using a `for` loop. The syntax is.

````
for each_flick in movies:
    # List processing code.
````

The for loop works on any number of item in the list. The above code have few important things to note.

* `for` , `in` are keywords in Python. `for` keywords is the best way to iterate over a list.
* `each_flick` is a target identifier, and `movies` is a list. The keyword `in` separates the target identifier with the list.
* `:` at the end of the for loop identifies the beginning of the list processing code.
* The target identifier `each_flick` is just like any other variable in python, with the scope till the end of the current scope. The target identifier is assigned a single value from the list `movies` after every iteration on the list `movies`.
* With `for` loop we need to maintain the state of the list, we automatically exit at the end of the list.


## List within list ##

We can also have a list within a list, as we already noted the list is not supposed to homogeneous.

Here is an example of list within a list.

````
movies = [
    "The Holy Grail", 1975, "Terry Jones & Terry Gillman", 91,
    [
        "Graham Chapman",
        [
            "Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"
        ]
    ]
]
````

The above list is a list of list. We can also use a `for` loop to iterate over it.

````
for each_item in movies:
    print(each_item)
````

The above code will give you the output.

````
The Holy Grail
1975
Terry Jones & Terry Gillman
91
['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]
````

So it can never differentiate the list within the list, we can use a special function and built in keywords to separate them.

### Condition ###

We can use a language construct called `if` condition. The construct of the syntax is like this.

````
if some condition holds:
    # The true code block
else:
    # The false code block
````

The above code is a decision making code, which decides the flow of the code. When we do some condition check such as `2<3`, if it is true, the true part of the code is executed else the false code block.

* `isinstance(list_name, list)` is one such condition checking built in function. This takes two parameters. `list_name` is the name of the list. `list` is the type to check if `list_name` is of that type.
* We can find all the built in function, `dir(__builtins__)` with this.


So now with the power of the `if` and `isinstance()` can we build a better code.

````
for each_item in movies:
    if isinstance(each_item,list):
        for item in each_item:
            print(item)
    else:
        print(each_item)
````

This code will print.

````
The Holy Grail
1975
Terry Jones & Terry Gillman
91
Graham Chapman
['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']
````

This is better than but still the last list in not expanded. We can get it done by this code.

````
for each_item in movies:
    if isinstance(each_item,list):
        for nested_item in each_item:
            if isinstance(nested_item,list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)
````


This gives the output:-

````
The Holy Grail
1975
Terry Jones & Terry Gillman
91
Graham Chapman
Michael Palin
John Cleese
Terry Gilliam
Eric Idle
Terry Jones
````

Which is what we want, but if we add another sublist, we have to write another extra piece of code. And the last code if you see, this portion of code is repeated multiple times.

````
for nested_item in each_item:
    if isinstance(nested_item,list):
````

As many times we encounter a sublist we have to put such code block. To help in this condition we have recursion and functions to thanks.

## Function & Recursion ##

### Function ###

Functions are a named variable for a block of code. When we have to repeat same piece of code multiple times we can extract it to make a function. This function can again be used in multiple places.

The syntax of a function is:-

````
def function_name(argument(s)):
    function code block.
````

As shown in the above piece of syntax, we have a `function_name`, this `function_name` can be used to execute the function code block by calling it using `function_name()`.

The above multiple lines of code can be condensed into this.

````
def print_lol(the_list):
    for list_item in the_list:
        if isinstance(list_item,list):
            print_lol(list_item) # This call to the same function is called Recursion.
        else:
            print(list_item)
````

In the above code if you see we have reduced the total no of line of code, and we are calling the same `print_lol` again, this philosophy is called Recursion.

The default recursion limit can be 1000 in Python, understanding this we have to think of recursion as putting the function on to a [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)). The maximum size a stack can grow in python is 1000.

## Bullet Points ##

This section is a revision of what we have learned till now. 

* Identifiers are name that refer to data objects. The identifier have no type but the data type to which they refer to do.
* A list is a collection of data, separated by commas and surrounded by square brackets.
* List are like array on steroids.
* List can be used with built in functions and also support a bunch of list methods.
* List can hold any data, and the data can be of mixed type. Lists can also hold list.
* List can shrink and grow as needed. All the memory required for this is managed by Python.
* Python uses Indentation to group statements together.
* `len()` provides a length of some data objects or count the number of items in a collection like a list.
* The `for` loop lets you to iterate over a list and is convenient to use in place of a `while` loop.
* The `if .. else` statements help in decision making in the code.
* `isinstance()` checks whether an identifier refers to a particular data type of not.
* `def` is used to define a custom keywords.

## References ##

* [Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
* [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
