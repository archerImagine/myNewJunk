number = 23

guess = int(raw_input('Enter an integer : '))

if guess == number:
	# New block starts here
	print "Congratulations, you guessed it."
	print "(but you do not win any prizes!)"
elif guess < number:
	# Another Block.
	print "No, it is litte higher than that."
else:
	print "No, it is litte lower than that."
print "Done"