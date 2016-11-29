def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return text == reverse(text)

something = raw_input("Enter a Text: ")
if is_palindrome(something):
	print "Yes, its is a palindrome"
else:
	print "No, It is not a palindrome"