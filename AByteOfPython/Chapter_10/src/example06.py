# This is a string object
name = "swaroop"

if name.startswith('swa'):
	print "Yes,the string starts with 'swa'"

if 'a' in name:
	print "Yes, it contains the string 'a'"

if name.find('war') != -1:
	print "Yes, it contains the string 'war'"

delimiter = "_*_"

myList = ['apple','mango','carrot','banana']
print delimiter.join(myList)