# Chapter 15 | Standard Library. #

The Python standard library has a huge number of modules, and is even part of the standard distribution.

## `sys ` Modules. ##
The `sys` modules has system specific functionality. Few examples are:-

* We use `sys.argv ` for finding out the command line arguments.
* We can check the version of Python we are using. This is found by using this `sys.version_info`


## Logging Module. ##

We have a logging modules which logs the code's log into a user directory as a text file. This is the modules `logging `

Here is the code for proper logging.

````python
import os, platform, logging

if platform.platform().startswith('Windows'):   
    logFile = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'),"test.log")
else:
    logFile = os.path.join(os.getcwd(),"../log/test.log")

print "Logging To:->>>>", logFile

logging.basicConfig(
    level=logging.DEBUG,
    format = '%(asctime)s : %(levelname)s : %(message)s',
    filename = logFile,
    fileMode = 'w',)

logging.debug("Start")
logging.info("Doing SOmething")
logging.warning("Dying Now")
````

Few important points is the previous Code:-

* We are using 3 standard library, 
    - `os` : For interacting with OS.
    - `platform ` : Information about the platform.
    - `logging ` : The module to log.
* The first thing which we do is check the platform details, 
* `os.path.join()`, joins the two arguments passed.

## Module of the week. ##

All the system's Modules cannot be described here, so kindly check this blog for more [details](http://pymotw.com/2/contents.html).

## Links ##

Here are some links for studying more on this.

* [The Python Standard Library ](https://docs.python.org/2/library/)