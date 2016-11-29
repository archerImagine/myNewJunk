#!/usr/bin/env python 

limit = input("Enter Limit:")

a = 0
while a < 10:
	print "a = ", a
	a += 1;
	if a > limit:
		break

else:
	print "limit exceded"

print "END"