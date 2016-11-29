class SchoolMember(object):
	"""Represent any  School Member"""
	def __init__(self, name,age):
		self.name = name
		self.age = age
		print "(Initalized School Member: {})".format(self.name)

	def tell(self):
		"""Tell my details"""
		print "Name: {} Age: {}".format(self.name,self.age),

class Teacher(SchoolMember):
	"""Represents a teacher"""
	def __init__(self, name,age,salary):
		SchoolMember.__init__(self,name,age)
		self.salary = salary
		print "Intialized Teacher: {}".format(self.name)
	def tell(self):
		SchoolMember.tell(self)
		print "Salary: {}".format(self.salary)

class Student(SchoolMember):
	"""Represents a student"""
	def __init__(self, name,age,marks):
		SchoolMember.__init__(self,name,age)
		self.marks = marks
		print "Intialized Student: {}".format(self.name)
	def tell(self):
		SchoolMember.tell(self)
		print "marks: {}".format(self.marks)

t = Teacher('Mrs. ABCD ', 40, 30000)
s = Student('XYZ',25,75)

print

members = [t,s]

for member in members:
	member.tell()

		
		