x = 50

def sampleFunction(x):
	print "x is ", x
	x = 2
	print "Changed local x to ", x

sampleFunction(x)
print "x is still ", x	