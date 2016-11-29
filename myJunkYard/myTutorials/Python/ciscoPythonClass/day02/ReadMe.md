# Day 2 Python Class #
## Different Data Type ##
### NoneType ###
* Generally use with function, if it does not return a value, and you can use it in a right side execution like:-  
````
def greet():print "Hello World"
y = greet() #executes the function
print y #prints non.
````
* All variable are by default initialized to `none` in python.  
* `none` evaulates to `false` in boolean.  
* Never initialize a variable in python.

### bool ###
* have two values `true` and `false`
* since all variables are object, so we can do something like this.  
````
True,False = False,True
```  
* 0,0.0,"",(),[],{},False,None all evaluates to false.  
````
a = 0
print "a is True" if a else "a is false"
a = "0"
print "a is True" if a else "a is false"    #True
````
* check if a object evaluates to True or False by using `bool(o)`, it is also a Type constructor or Type Conversion.

### Numeric ###
* **int**
  * There are two type of `int` in python, `int` and `longs`, `int` is optimized for System architecture for register optimization, `long` is in heap.

    ````
    a = 10
    type(a) #<type 'int'>

    a = 233255438807987876767676
    type(a) #<type 'long'>

    ````
  * In Python3, there is only one type, is `int`
  * `print 0xcafe` `#Hex`
  * `print `0879` `#Octal`
  * `oct(10)` prints the octal notation. in string
  * `bin(10)`
  * `hex(10)`
  * Python has support for complex number `a +ib`, `a.real()`,`a.imag()`,`a.conjugate()`
  * represent binary as `0b11011011`
  * `int()` converts compatibility type to int. as it take a radix parameter, `int(`0xfabc`,16)`
  * Python is a strict type checking, also you have to do type conversion in Python.
  * Variables are type less, but Object have a type.
* **float**
* *fractions.Decimal* and **fractions.Fractions**
  * `from fractions import Fraction`, `a = Fraction(1,4)`

### Iterable Objects ###
* **Collections**
    * **Sequences** : Indexable objects, can have duplicates.
        - **String** : 
            + `a = "Hello World`
            + `a = "I'll be back"`
            + `a = ''' I am Back ''''`, use triple quotes to represent multi line.
````
install_path = r"c:\backup"
````
            *   Unicode Quotes : `a = u"Hello"`
            *   SubStr is not present in Python, but 
````
a = "Hello World"
a[3:7] #lo w
a[-5:] #last five character.
````
            *   `a[0:10:2]`, all alternate number, skip index is 2
            *   `a[::-1`, reverse a string
            *   `+`, concatenates strings
            *   `*`, sequence repeater, 
````
a = "Hello"
b = a * 5 #5 times Hello
````
            *  Format Specifier, `%s, %d`
````
rec = "Sam", 56, "Bangalore"
output = "Name : %s, Age : %d, City : %s"
print output % rec
````
            *  `a.startswith("Hello") `
            *  `a.endswith("world")`
            *  `"wo" in a`
            *  `a.count("is")`
            *  `a.find("is")`, in error return -1
            *  `a.upper()`
            *  `a.lstrip()`, `a.rstip()`, `a.strip()`
            *  `a.strip()`, break a string in a list, with out argument it is space delimiter.
            *  `a.join()`, reverse of split
        +  **Unicode**
        +  **bytearray()**, creates mutable string object, all string apis are available
````
b = bytearray("Hello World")
````
            *  `b[:] = "New String"`, `id()` remains same, but value changes
            *  `b.append(`a`)`, append char at the end of a byte array
            *  `a += b` is different that `a = a + b`, id does not change in first
            *  `b.extend("aaaaaaaa")`, take a string and appends, but append only append on 1 char
            *  `a.insert(index,' ')`, at index, insert the second parameters, takes a char as 2nd param.
            *  `b.pop()`, removes last char, and returns a ascii value., when passed a arguments as index, it removes element at that index.
            *  use a bytearrary for list with numbers below 255.
        +  **tuple**
````
t = 10, 5.6,5+4j, True, None, (10,20,30)
````
            *   Tuple packing and un packing.
            *   Tuple is immutable.
            *   `a.count(55)`: no of 55 in a tuple
            *   `a.index(43)`: what is an index of 43.
        +   **list**
````
a = [44,55,77,88]
````
            *   Mutable.
            *   Square brackets.
            *   `a += 55, 66, 77` : adds to the original list without id modification.
            *   `+=` with string does a string.
            *   `zip(names,ages)` list of each element from names and ages.
            *   `for name,age in zip(names,ages): print output %(name,age)` : **Parallel iteration.**
````
from itertools import izip
izip(names,ages,cities)
````
            *   `enumerate`, count over a tuple
````
for i,n in enumerate(names):print i,n
````
            *   `sorted`, sorts an list
            *   `reversed(names)`: iterate on a reverse list, not reverse the list.
            *   `sum()` : sum of a list
            *   `x = 10,` : single tuple list
            *   `all(a)`: all element should evaluate to true.
            *   `iter(a)` : change the list to an iterator.
            *   `a.append()` : appends at end
            *   `a.pop()` : remove from end
            *   `a.pop(0)`: from first, becomes a queue
    * **Set** : Unordered collection. and no duplicates.
        - Useful when finding an element in a unordered
        - set difference, `set(a) - set(b)` all the element in a which are not there in b.
        - `set(a) & set(b)` : set intersection.
        - `set(a) | set(b)` : set union
        - `set(c).issubset(set(b))`
        - `set(c).issuperset(set(b))`

````
s = {33,44,55,66,33,44} #ordering, and duplicates are removed.

````

   * **Map** :
````
a = 10,22,33,44,55,66,77
b = map(square,a) #give square of a
sqr = lambda x:x*x  #lambda will only take single line body.
b = map(lambda x: x*x,a)
````
    -   **Comprehensions**
        +   There are very fast, so should be used in place of lambda.
        +   **Generator comprehensions**

   ````
   a = 10,22,33,44,55,66,77
   b = [x*x for x in a]
   b = [x for x in a if x % 3 == 0]
   b = [x*x for x in a if x % 3 == 0] #square after applying filter.
   ```` 
   * **reduce**
````
a = 10,22,33,44,55,66,77
reduce(lambda x,y:x*y,a) #takes on function, with two parameters.
````
## Reference ##
1. [Format String](https://docs.python.org/2/library/string.html#new-string-formatting)






