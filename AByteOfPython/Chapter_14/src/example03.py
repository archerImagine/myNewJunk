try:
	text = raw_input("Enter Something ---> ")
except EOFError:
	print "Why did you do an EOF on me?"
except KeyboardInterrupt:
	print "You cancelled the operation"
else:
	print "you entered {}".format(text)