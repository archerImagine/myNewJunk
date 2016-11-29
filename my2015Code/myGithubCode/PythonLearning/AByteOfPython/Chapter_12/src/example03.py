class Person:
	def __init__(self,name):
		self.name = name
	def say_Hi(self):
		print "Hello, my name is ", self.name

p = Person('ABCD')
p.say_Hi()