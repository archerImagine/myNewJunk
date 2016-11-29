# Pelican #

## Resources ##

To start with [Pelican ](http://blog.getpelican.com/), I have found these 3 resources which I find very helpful, and will also mentioned what I am learning from each sites.

* [Creating your own blog with Pelican ](http://chdoig.github.io/create-pelican-blog.html)
* [Making a Static Blog with Pelican ](http://nafiulis.me/making-a-static-blog-with-pelican.html#id19)
* [Pelican Documentation v3.6](http://docs.getpelican.com/en/3.6.0/)

## Installation ##

* [Pelican Doc | Install ](http://docs.getpelican.com/en/3.6.0/install.html)

As mentioned in the above link, and what we know mostly about installing packages, we will use `pip` to install `pelican`. 

We can use `virtualenv` to install `pelican` or we can install globally.

````
pip install pelican
````

If you use MARKDOWN, to write you blog you might additionally need the `markdown` package.

````
pip install Markdown
````

It will install some of its dependency. If you are using `virtualenv`, I will suggest some task which will help you.

Once the installation of `pelican`, `virtualenv`, `markdown`, `typogrify` is done run this command.

````
pip freeze > requirements.txt
````

This will generate a text file, `requirements.txt`, you can use this file to install all these dependency again in a new `virtualenv` using this command.

````
pip install -r requirements.txt
````

## Problem with Pelican Installation. ##

I am running on a `mac`, and when I run the first recommended command to setup a blank blog.

````
pelican-quickstart
````

It gave me this error,

````
Traceback (most recent call last):
  File "/Users/XYX/anaconda/bin/pelican-quickstart", line 7, in <module>
    from pelican.tools.pelican_quickstart import main
  File "/Users/XYX/anaconda/lib/python2.7/site-packages/pelican/__init__.py", line 20, in <module>
    from pelican.generators import (ArticlesGenerator, PagesGenerator,
  File "/Users/XYX/anaconda/lib/python2.7/site-packages/pelican/generators.py", line 22, in <module>
    from pelican.readers import Readers
  File "/Users/XYX/anaconda/lib/python2.7/site-packages/pelican/readers.py", line 9, in <module>
    import docutils.core
  File "/Users/XYX/anaconda/lib/python2.7/site-packages/docutils/core.py", line 20, in <module>
    from docutils import frontend, io, utils, readers, writers
  File "/Users/XYX/anaconda/lib/python2.7/site-packages/docutils/frontend.py", line 41, in <module>
    import docutils.utils
  File "/Users/XYX/anaconda/lib/python2.7/site-packages/docutils/utils/__init__.py", line 20, in <module>
    import docutils.io
  File "/Users/XYX/anaconda/lib/python2.7/site-packages/docutils/io.py", line 18, in <module>
    from docutils.utils.error_reporting import locale_encoding, ErrorString, ErrorOutput
  File "/Users/XYX/anaconda/lib/python2.7/site-packages/docutils/utils/error_reporting.py", line 47, in <module>
    locale_encoding = locale.getlocale()[1] or locale.getdefaultlocale()[1]
  File "/Users/XYX/anaconda/lib/python2.7/locale.py", line 543, in getdefaultlocale
    return _parse_localename(localename)
  File "/Users/XYX/anaconda/lib/python2.7/locale.py", line 475, in _parse_localename
    raise ValueError, 'unknown locale: %s' % localename
ValueError: unknown locale: UTF-8
````

So as per this error, we have to set the the variables as mentioned here.

* [
Pelican 3.3 pelican-quickstart error “ValueError: unknown locale: UTF-8”
](http://stackoverflow.com/questions/19961239/pelican-3-3-pelican-quickstart-error-valueerror-unknown-locale-utf-8)

````
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
````