# Chapter 13 | Input and Output #

## Introduction ##

In most of our programing work, we would like to do these things.

* Take input from user
* Give output to the user
* Read files as input
* write to files as output.

All these operations are in totality know as Input/Output operation.

## Input from User ##

Consider the below code:-

````python
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = raw_input("Enter a Text: ")
if is_palindrome(something):
    print "Yes, its is a palindrome"
else:
    print "No, It is not a palindrome"
````

In the above code, the function `raw_input` take arguments as a string, which is displayed to the user, and once the user enters a text followed by enter key, the text is assigned to the variable `something `

## File ##
We can do file operation with the help of `file ` class and its methods like `read`, `readline`, `write`. Also we can define the mode in which to open the file, i.e. `binary ` or `text `. Then there is a method `close()` to close the file.

Consider the below example:-

````python
poem = ''' 
            Programmin is fun,
            When the work is done
            if you wanna make your work also fun: 
            Use Python.
        '''

# Open a file for writing
f = open('../data/poem.txt','w')

# write the text to the file
f.write(poem)

# Close the file.
f.close()

# If no mode is specified,
# 'r'ead mode is assumed to be default.

f = open('../data/poem.txt')
while True:
    line = f.readline()

    if len(line) == 0:
        break
    print line

f.close()
````
The modes to open a file are:-

* read mode `r`
* write mode `w`
* append mode `a`

## Pickle ##

`Pickle ` is a inbuilt python modules, which help in storing a object state into a file. This is what we call storing the object **Persistently**.

here is the code 

````python
import pickle

shoplistfile = '../data/shoplist.data'
shoplist = ['apple','mango','carrot']

f = open(shoplistfile,'wb')

pickle.dump(shoplist,f)

f.close()
del shoplist

f = open(shoplistfile,'rb')
storedList = pickle.load(f)
print "storedList: ", storedList
````
The call to `dump ` function,  writes the object into the file, this process is generally called **pickling.**

Then the call to `load `, writes back the data from a file to the object, this process is called **unpickling**

## Unicode  ##
If we need to represent text, which are not in English we might need the unicode support, which starts with the letter `u`.

When we have to transfer text over network, we generally convert it to `utf-8`, also when we deal with unicode in out code, we have to give this comment

````
# encoding=utf-8
````
