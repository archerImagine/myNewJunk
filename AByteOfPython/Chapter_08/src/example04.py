x = 50

def sampleFunction():
	global x
	print "x is ", x
	x = 2
	print "Changed global x to ", x

sampleFunction()
print "Value of x is ", x	