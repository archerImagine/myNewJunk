# Chapter 12 | Object Oriented Programming #

## Introduction ##

We have written a lot of code till now, these codes were mostly data manipulation code, where every thing happened sequentially and by calling different functions from one or many function, this type of programming is called **Procedural Programming.**

There is another type of programming were we combine the data and the functionality into a single entity which we call as Class. This programming idea is called **Object Oriented Programming.**

There are two main aspect of **Object Oriented Programming**:

* **Class** : A **Class** creates new type.
* **Objects** : A **Objects** is **instances** of the class.

Two main components are involved in a Objects, which is a instance of a Class.

* **Fields**:- Variables which belongs to a class or object where we store data are called **Fields**. These are of two types.
    - **Instance Variables** : Variables which belongs to a particular object instances.
    - **Class Variables** : Variables which are shared across all the object instances.
* **Methods**:- Object can also have functionality in addition to storing data, The functionality is provided by the function within a object which is called **Methods.**

TODO: One question which we have to find answer is to is there any class methods or static methods.

* [The definitive guide on how to use static, class or abstract methods in Python ](https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods)

## The `self` ##

Methods are nothing but function inside a class, but it has one major difference than any other normal function. In a method definition, the first argument is always `self `, similar to `this ` in Java or C++.

This first argument `self ` refers to the object itself and by convention it is called `self `, though we can name as anything but it is advisable to name it `self `.

One important question remains, i.e. **how does self gets its value?**

Consider this, we have a class called `MyClass` and an instance of this class called `myobject` . When we call a method on `myobject` instance, we call it using `myobject.method()`, this gets converted to `MyClass.method (myobject)`

## Classes ##
The most simplest class will be

````python
class Person(object):
    pass # Empty Block

p = Person()
print p
````

gives a output:-

````
<__main__.Person object at 0x10d455a10>
````

Few things to note in the above code:-

* Use the keyword `class` to create a class.
* Instance is create just by calling the class name, as shown by `p = Person()`

## Methods ##

Here is an example of Methods in action.

````python
class Person:
    def sayHi(self):
        print "Hello, How are you."

p = Person()
p.sayHi()
````

## The `init ` method ##

There are some predefined methods of significance in python, `init` is one of them.

`init` is executed as soon as the object of the class in instantiated. This method id useful to do only initialization. It starts with `__init__`

Here is an example of `init` method

````python
class Person:
    def __init__(self,name):
        self.name = name
    def say_Hi(self):
        print "Hello, my name is ", self.name

p = Person('ABCD')
p.say_Hi()
````
Few things to note in the above code:-

* `__init__` takes a argument `name`, we save this variable to the instance variable `name`, we know this is the instance variable because we invoke it by `self.name`
* We never explicitly call `__init__`, but pass the parameter as a argument in the object creation time.
* We can now use `self.name` in any of the class methods, like we have done in `say_Hi` method.

## Class and Object Variables ##

Field are nothing but variables which are bound to the class name space. As already mentioned there are two type of variables:-

* **Class Variables**:
* **Object / Instance Variables**:

Lets consider the below code, for understand this:-

````python
class Robot(object):
    """Represent a Robot with a string"""

    # A class variable, counting the number of robots.
    population = 0
    def __init__(self, name):
        """Initalize the data"""
        self.name = name
        print "(Initalizing {})".format(self.name)

        # When this person is created, the robot 
        # adds to the population
        Robot.population += 1
    def die(self):
        """I am dying"""
        print "{} is being destroyed ".format(self.name)
        Robot.population -= 1
        if Robot.population == 0:
            print "{} was the last one ".format(self.name)
        else:
            print "There are still {:d} robots working".format(Robot.population)
    def say_hi(self):
        """Greetings by the robot
            Yeah, they can do that
        """

        print "Greetings, my master call me {}".format(self.name)
    @classmethod
    def how_many(cls):
        """prints the current population"""
        print "We have {:d} robots".format(cls.population)

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3P0")
droid2.say_hi()
Robot.how_many()

print "\nRobots can do come work here.\n"
print "\nRobots have done their work, so let's destroy them"

droid1.die()
droid2.die()

Robot.how_many()
````

* `population ` is a class variable, which belongs to the `Robot` class.
* `name ` is a instance variable, which belongs to the object.
* `population ` is accessed by `Robot.population `, since it is a class variable, if we have both class and instance variable with the same name, then the instance variable take preference.
* Another way of accessing population is `self.__class__.population `
* `how_many()` is a class method, we have marked `how_many()` with a decorator, which we will discuss in future.
* All class members are by default public, with come exception. The naming rule being, the variable or methods which are not public should begin with `__`

## Inheritance ##
Code re-usability was always of concern for software development, so in the OOP world, **Inheritance** helps in this regards.

Inheritance is just a type and a subtype relationship between classes. 

We can have a **base class**, from with sub classes are derived, So this helps in code re-usability as, the sub classes does need to duplicate the code already present in the base class. Also change to base class are automatically reflected in the subclass.

One more advantage is that we can pass the Base class, when we are not sure about with sub class should handle the situation, this is called **Polymorphism**.

