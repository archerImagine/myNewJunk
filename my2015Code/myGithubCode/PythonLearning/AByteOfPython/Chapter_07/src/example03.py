number = 23
running = True

while running:
	guess = int(raw_input('Enter an integer : '))

	if guess == number:
		# New block starts here
		print "Congratulations, you guessed it."
		print "(but you do not win any prizes!)"
		running = False
		break # This break cause the else: block not to be executed.
	elif guess < number:
		# Another Block.
		print "No, it is litte higher than that."
	else:
		print "No, it is litte lower than that."
else:
	# this is not executed if the while loop has a break.
	print "The while Loop is over."
print "Done"	
	

