def powersum(power, *args):
	"""Returns  the sum of each argument raised to the specified power"""
	total = 0
	for x in args:
		total += pow(x,power)
	return total

print powersum(2,3,4)