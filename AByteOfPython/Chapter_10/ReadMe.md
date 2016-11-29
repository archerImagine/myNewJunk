# Chapter 10 | Data Structures #

# Introduction #
There are four built-in data structures in python.

1. list
2. tuple
3. dictionary
4. set

## List ##

A list holds a ordered collection of items.

Few important things about list:-

* List are mutable, i.e. the list members can be added, removed, or merged without creating a new list.
* List are denoted by `[]`
* Ordered collection, means the order items are put in the list it comes out in the same manner

One important thing not related to List, which is mentioned is,
````
print items,
````

The above line will print all the items in the same line instead of multiple lines.

All the modification methods on list like, `append()`, `sort()` all work on the same list, no temporary list is created.

## Tuple ##

Few things to remember about tuples.

* Tuple's are immutable, i.e., it cannot be modified, even if modified, it will create a new tuple.
* Tuple are denoted by `()`, which are optional

A tuple with just one element have a special syntax, `(8,)`

Tuple can also be created like this:-

````python
newZoo = 'monkey' ,'camel', zoo
````

So the `()` is not compulsory.

## Dictionary ##

A Dictionary is just like an address book, you find the address of the contact by going to the name of the contact. So this is called a association of `<key,value>`

Few important points to note about it:-

* Only immutable objects can become keys.
* Values can be both immutable or mutable.
* The dictionary is not ordered.
* A Dictionary is denoted like:-

```python
d = {
    key1:value1,
    key2:value2
}
```

We can access each key-value pair of the dictionary using the `items` method of the dictionary which returns a tuple.

## Sequence ##
List, tuples and strings are example of sequence.

The characteristics of Sequence are:-

* **MemberShip Test** (`in` and `not in`)
* **Indexing Operation**
* **Slicing Operation**

A slice operation returns the elements from the start position to just before the end element.

Negative numbers are used to slice from the end of the sequence.

Third arguments of slice is the step operator.

## Sets ##
Sets are unordered collections of simple objects.

To copy a set or object use the full slice operation.

### Learning Table ###

|       | Mutability | Brackets |  Ordered  |
| ----- | :--------: | :------: | :-------- |
| Tuple | immutable  |   `()`   | Ordered   |
| List  |  Mutable   |   `[]`   | Ordered   |
| Dict  |  Mutable   |   `{}`   | UnOrdered |
| Set   |  Mutable   |   `{}`   | UnOrdered |

This question my help to remember these different factors

* [What are some mnemonics to remember list, tuple, dictionary and sets](http://www.reddit.com/r/learnpython/comments/34azxe/what_are_some_mnemonics_to_remember_listtuple/)




