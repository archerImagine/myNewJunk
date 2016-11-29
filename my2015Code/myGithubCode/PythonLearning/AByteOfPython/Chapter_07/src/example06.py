while True:
	s = raw_input("Enter Something : ")
	if s == 'quit':
		break
	if len(s) < 3:
		print 'Too Small '
		continue
	print 'Input is of sufficient length'