# Chapter 16 | More #

## Passing Tuple around ##

We might have thought of returning more than 1 values as a return type a lot of time, and most time we used array to return multiple values. We have an option of returning a tuple in python. Which can return atleast 2 values.

````python
def getErrorDetails():
    return (2,'details', "hello")

errNum, errStr, errStr2 = getErrorDetails() 

print "errNum: ", errNum
print "errStr: ", errStr
print "errStr2: ", errStr2
````

In the above example we are returning 3 values. The usage `a,b = <some expression >` interprets the result of the expression as a tuple of two values.

As are use case of tuple, the fastest way to swap two values is

````python
a,b = 10,12

a,b = b,a

print a,b
````

## Special Methods ##
There are some methods, which have special meaning. Like `init ` and `del `. Special methods are used to mimic some special behavior from a class.

Like if we want a behavior like `x[item]` from our own class, we have to implement a special method called `getitem()`.

To find a list of such special methods we can go to [manual ](https://docs.python.org/2/reference/datamodel.html#special-method-names).

Some special methods are mentioned below:-

* `init(self)` : This method is called just before newly created object is returned for usage.
* `del(self)` : Called just before an object is destroyed.
* `str(self) :` Called when we use `print ` statement or when `str()` is used.
* `lt(self,other) : ` Called when less than operator is used.
* `getitem()` : Called when `x[key]` indexing operation is used.
* `len(self) : ` Called when built in `len()` function is invoked.

## Single Statement Blocks. ##

We a conditional statement like `if` has just one statement to execute we can have it in the same line as the condition inplace of an indentation.

````
flag = True

if flag: print "true"
````

Though this is not a recommended practice, we can use it for debugging.

## Lambda Forms ##

A Lambda statement is used to create a new function objects. Essentially `Lambda` takes a parameters followed by a single expression which actually becomes the body of the function.

````
points = [{'x':2, 'y':3}, {'x':4, 'y': 1}]

print points

points.sort(key = lambda i: i['y'])
print points
````

## List Comprehension ##
List Comprehension are a way to create a new list from an existing list. Consider the below example.

````
listOne = [2,3,4]
listTwo = [2*i for i in listOne if i > 2]

print listOne, listTwo
````

## Receiving Tuples and Dictionaries from Function. ##
There is a special way of receiving parameters to a function as a tuple or a dictionary.

Consider the below example:-
````
def powersum(power, *args):
    """Returns  the sum of each argument raised to the specified power"""
    total = 0
    for x in args:
        total += pow(x,power)
    return total

print powersum(2,3,4)
````

Because of `*` prefix on `args`, all the extra arguments are stored as a tuple. If a `**` prefix had been used instead, the extra arguments will be considers key/value pair of a dictionary.

## The `assert ` statement ##

The `assert ` statement is used to assert is something is true.

````
mylist = ['item']

assert len(mylist) >= 1

mylist.pop()

assert len(mylist) >= 1
````

The second assertion fails.

## Decorators. ##


