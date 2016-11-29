# Day 3 #
## Dictionary ##
* Extension of sets.
````
info = {"name" : "John", "age" : 56,"city":"Mumbai"}
type(info)
<type 'dict'>
````
* `info["name"] = "Sam"` : add element, if key is not there, it will create a new key and add it.
* `info = dict(name="John",host="localhost",port=80)` :`dict` keyword can be used.  
````
names = {"John"}
data = dict(zip(names,cities))
data = dict(izip(names,cities)) #efficient object
````
* Trying to access a key from dict non exsistent throws error, `info.get("name")` will not throw a exception. `info.get("name","undefined")` : returns "undefined" if a key is not there.
* `"city" in info` : check for the key
* `info.keys()` : returns all the keys in a dict as a list
* `info.setdefault("name","undefined")` : if key is not there, add the key initialize with "undefined", existing key will not be modified.
* `info.values()`: returns values.
* `info.items()`: returns tuple sets.
* iteration on dict.
````
for k in info.key():print k,info[k] #ineffcient, extra list is created,
for k in info:print k,info[k] #effcient, no extra list is created,
````
* Scala, clojure,R,Go,Julia compete in Machine Learning.
* `info.iterkeys()`
* `info.itervalues()`
* `info.iteritems()`
* `info["country"] = "India"`, after this iteration will not work.
* `info.viewkeys()`: view of actual dict.
* `info.clear()` : clear dict.
* `del a[:]` : clears a list.

