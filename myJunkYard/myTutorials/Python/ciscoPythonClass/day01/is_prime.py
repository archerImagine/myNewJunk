#!/usr/bin/env python 
x = input("Enter a Number ")

a = 2
num = x
for a in range(a, num):
	if num % a == 0:
		print('not prime')
		break
else:
	print('prime')