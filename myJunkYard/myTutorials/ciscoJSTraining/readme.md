# Cisco JS Training #

## Different type of Web Application. ##

1. Classical web application.
    * UI generation happens on server side.
    * Role of browser is limited.
    * User exp is delayed because of the journey to and fro from browser to server.
    * see a blank for some time.
2. Rich Internet Application.
    * Push the UI experience to client side.
    * Only data flows from browser and server.
    * Gives desktop like experience. ex **Gmail**

### Types supported in JavaScript ###

* Very limited data type in JavaScript.
* We have to compare for approximation and not absolute because we only have floating point.
* No support for **classes**

1. typeof 123
    * "number"
2. typeof "123"
    * "string"
3. typeof true
    * "boolean"
4. typeof {}
    * "object"
5. typeof undefined
    * "undefined"
6. typeof function(){}
    * "function"

*  **typeof NaN**
    *  **"number"**

### Difference between Object and Function ###

JavaScript is flexible for use as OOAD and Functional Programming. Focus towards functional.Functions are first class citizen.


|        Object        |            Function           |
| :------------------- | :---------------------------- |
| var o = {}           | var f = function (){}         |
| var o = new Object() | var f = new Function()        |
| o.id = 100           | f.id = 100                    |
|                      | function can return function, |


### Functions ###
When we invoke a function we get 2 parameters inside the functions.
* arguments
    * array like object.
    * gives the length parameters
* this
    - represent the object invoking the function.
    - it is also called invocation context.
Each function have 3 methods:-
1. call()
2. apply()
3. bind()

The first 2 can be used to change the context of this. ex: emp.whoAmi.call(product)

### Diff between call and apply ###
The arguments to the function are passed as an array in apply.
ex:- 
greet.call(emp,"Mr." ,"Have a nice day");
greet.apply(emp,["Mr." ,"Have a nice day"]);

There is a difference between arguments and Array

````js
function f(){
    console.dir(arguments);
    console.dir([1,2,3,4,5]);
}
f(1,2,3,4,5);
````

**ducktyping**

````
function bindThis(fn,obj){
    return function(){
        return fn.apply(obj,[].slice.apply(arguments,0));
    }
}
````

Self invoking anynonous function.

### Closure ###
1. Outer function
2. Variable inside outer function.
3. Inner function.
4. Refer the outer variable from inner function.
5. The variable is controlled by inner function with a private scope.

### Memoization ###

````
function isPrime(n){
var defaults = {0:true, 1:true,3:true,4:true}
    isPrime.cache = isPrime.cache || defaults;
    if(typeof isPrime.cache[n] != "undefined"){
    console.log("From Cache");
    return isPrime.cache[n];
}
isPrime.cache[n] = true;
for(var i = 2; i <= (n/2);i++){
    if(n%i == 0){
    is
}
}
}
````

-------

# Day 2 #

### Predicates. ###
A function which takes an arguments and returns a boolean function.

## Object Creation ##

### Constructor ###

When should we go for Constructor function?
Constructor function relives from the knowledge of the object internal.
Constructor will give typeof return value which is not just a Object.

````
function Employee(id,firstName,salary){
    this.id = id;
    this.firstName = firstName;
    this.salary = salary;
}

var e1 = new Employee(101,"Animesh", 10000);

e1
    Employee {id: 101, firstName: "Animesh", salary: 10000}

````

## Inheritance ##
### Prototype inheritance ###

Create an object based on another object.

Prototype is present in function.

Object has constructor

Base object property modification result in objects property.

Hopping happens for reading and not writing value.

Mixin: Copying everything from base object to derived class.

Behavior should be borrowed from base so use `Constructor.prototype.functionName = function (){}`, use this only which uses the public interfaces and not object state.

Calling a function with a parameter is a getter and with parameter is a setter.





