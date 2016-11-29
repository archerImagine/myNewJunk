# Chapter 05: Reference Type #
---

* A reference value (object) is an instance of a specific *reference* type.
* ECMAScript though is Object Oriented, it lacks some basic constructs that have traditionally been associated with Object-Oriented programming, including Class and Interfaces.
* ECMAScript provides a number of native reference types, which are described in much details in the following sections.

## The Object Type ##
* Instances of **Object's** do not have much functionality, they are ideally suited to storing and transmitting data around.
* There are two ways to create a *Object*
    - The first ways is use the `new` operator with the `Object` Constructor.
````
var person = new Object();
person.name = "Nick";
person.age = 34;
````
The implementation of this can be seen [@ObjectTypeExample01](chapter05.html#ObjectTypeExample01)
    - The second ways is to use the **Object Literal Notation**.
````
var person = {
    name="Nick",
    age=34
};
````
The implementation of this can be seen [@ObjectTypeExample02](chapter05.html#ObjectTypeExample02)

 ## The Array Type ##
## The Date Type ##
## The RegExp Type ##
## The Function Type ##
## Primitive Wrapper Type ##
## Singleton Built-in Types ##








