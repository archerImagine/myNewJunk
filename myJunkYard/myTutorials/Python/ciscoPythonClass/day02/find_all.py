#!/usr/bin/env python 
#Find index of all the sub string in a string
string = raw_input("Enter Main String")
subString = raw_input("Enter Sub String")

print[i for i in range(len(string)) if string.startswith(subString, i)]

start = 0
while True:
	start = string.find(subString,start)
	if start == -1:
		break
	print start
	start += len(subString)