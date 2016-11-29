def printMax(a,b):
	if a > b:
		print a, " is maximum. "
	elif a == b:
		print a, " is equal to ", b
	else:
		print b, "is maximum"

# Directly Pass the Literal Value

printMax(3,4)

x = 5
y = 7

# Pass the variable as arguments.
printMax(x,y)