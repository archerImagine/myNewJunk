# Getting only one line output from `ls` command #

When we give `ls` command to get the list of files in a directory it displays the list in column format. as shown below.

````
Desktop  Documents  Downloads  examples.desktop  Music  Pictures  Public  Templates  Videos
````

But if we want to list them in a vertical line we have to give the following command parameters.

````
ls -x1
````

This gives the output in the format mentioned below.

````
Desktop
Documents
Downloads
examples.desktop
Music
Pictures
Public
Templates
Videos
````

So what does the parameters mean.

1. `x` : list entries by lines instead of by columns, so it will list them vertically.
2. `1`: list one file per line, so we get files listed vertically in place of column.