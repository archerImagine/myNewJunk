#!/usr/bin/env python 
x = input("enter number")
a, b = 0, 1

while x:
	print a
	a,b = b,a+b;		
	x -= 1;

a,b = 0,1
num = input("Enter Number")
for i in range(num):
	print a,
	a,b = b,a+b
