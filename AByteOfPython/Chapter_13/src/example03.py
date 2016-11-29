poem = ''' 
			Programmin is fun,
			When the work is done
			if you wanna make your work also fun: 
			Use Python.
		'''

# Open a file for writing
f = open('../data/poem.txt','w')

# write the text to the file
f.write(poem)

# Close the file.
f.close()

# If no mode is specified,
# 'r'ead mode is assumed to be default.

f = open('../data/poem.txt')
while True:
	line = f.readline()

	if len(line) == 0:
		break
	print line

f.close()