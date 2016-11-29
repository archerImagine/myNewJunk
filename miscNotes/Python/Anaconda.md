# How to install both Python 2 and Python 3  with anaconda#

[Anaconda ](https://www.continuum.io/downloads) is a great Python package distribution. It come pre-built with all the necessary python packages. The default installation for Anaconda ask about which python version to download. 

When we need both python 2 and 3 Anaconda packages, we can follow the instruction mentioned [here](http://conda.pydata.org/docs/py2or3.html), which uses Conda package manager to solve the problem.

The first thing we should do is check the available python version, This we can get by firing this comand on the respective OS's terminal.

* `conda search python`

You might have installed a default version on python with Anaconda, Lets say that is Python 2.7.

The first thing we should do is to create a Python 2.7 Environment. This can be done by issuing the following command.

* `conda create -n py27 python=2.7 anaconda`
	- Here we create a environment with the name `py27`

The next thing to do is to install Python 3.5 with its Anaconda packages.

* `conda create -n py35 python=3.5 anaconda`
	- This will create a new environment name py35.

This is enough to have both the packages. The next task we have to do is to find where the environments are located, so as to modify the different paths accordingly.

We can list the environments by using.

* `conda info --envs`

This will list an output like this in ubuntu.

````
py27                     /home/newCode/anaconda2/envs/py27
py35                     /home/newCode/anaconda2/envs/py35
root                  *  /home/newCode/anaconda2
````
The `*` infront of the path siginifies the default options.

We can switch between the environments by giving these commands.

* `source activate py35`
	- This will activate the Python 3.5 interpreter.
* `source activate py27`
	- This will activate the Python 2.7 interpreter.

## Reference ##
* [Managing Python ](http://conda.pydata.org/docs/py2or3.html)

