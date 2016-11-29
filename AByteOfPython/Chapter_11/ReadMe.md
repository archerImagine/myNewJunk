# Chapter 11 | Problem Solving #

## Introduction ##
We have seen some major python constructs, like tuple, list, loops, function, etc. So we have the basic ingredients to solve a problem. We have learn the bits and pieces, now we will make the complete model using this.

## The Problem ##
Everything begins with a problem definition. 

> I want a program which creates a backup of all my important files.

This problem definition is good, but it does not convey a great deal of information. When this is the case a little more **analysis** is required.  

When we are done with analysis, we would like to **design**. When making design one thing should be kept in mind that it is a creative process and two people may or may not come up with the same design, which is perfectly fine.

We once we have the design we make our initial implementation, the same implementation is here.

```python
import os, time

# 1. File to be backed up is specified in the list.

source =['/Users/xyv/myWorks/myGithubCode']

# 2. The Backup must be stored in a main backup directory.

targetDir = '/Users/xyv/myWorks/myGithubCode/backup'

# 3. The files are backed up into a zip file
# 4. The name of zip file is current date and time.

target = targetDir + os.sep + time.strftime('%Y%m%d%H%M%S') +".zip"

# Create target directory if it is not present
if not os.path.exists(targetDir):
    os.makedir(targetDir)       # make directory

# 5. We use the zip command to put the file in a zip archive.
zipCommand = "zip -r {0} {1}".format(target,''.join(source))

print "Zip Command is:"
print zipCommand

print "Running: "

if os.system(zipCommand) ==0 :
    print "Sucessfull backup to ", target
else:
    print "Failed Backup."
```

Once the implementation is over, we are in **testing** phase, where we test the code for all possible value and then if a problem is found we try to **debug** the code.

## Second Version. ##
We can modify the above version of code, so that it stores backup in a hierarchical directory structure.

## Phases of Problem solving ##

For the above discussion we can conclude that these are the step in the problem solving.

* What - Analysis
* How - Design
* Do It - Implementation
* Test - Testing and Debugging
* Use - Operation or Deployment
* Maintain - Refinement
