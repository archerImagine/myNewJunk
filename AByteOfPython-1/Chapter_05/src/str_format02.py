# decimal precision of 3 for float 0.333
print '{0:.3f}'.format(1.0/3)

# fill with _ and the text centered.
print '{0:_^11}'.format('hello')
print '{0:_^10}'.format('hello')

# Keyword based.
print '{name} wrote {book}'.format(name="Swaroop", book="A Byte of python")
