# Checking whether a text is a palindrome should also ignore punctuation, 
# spaces and case. For example, “Rise to vote, sir.” is also a palindrome 
# but our current program doesn’t say it is. 
# Can you improve the above program to recognize this palindrome?

forbidden = (".","?","!",":",";","-","_","(",")","[","]","...","'" ," ","/",",")

def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return text == reverse(text)

something = raw_input("Enter a Text: ")
something = something.lower()

for x in something:
	if x in forbidden:
		something = something.replace(x,"")

if is_palindrome(something):
	print "Yes, its is a palindrome"
else:
	print "No, It is not a palindrome"