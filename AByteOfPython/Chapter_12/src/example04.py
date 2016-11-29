class Robot(object):
	"""Represent a Robot with a string"""

	# A class variable, counting the number of robots.
	population = 0
	def __init__(self, name):
		"""Initalize the data"""
		self.name = name
		print "(Initalizing {})".format(self.name)

		# When this person is created, the robot 
		# adds to the population
		Robot.population += 1
	def die(self):
		"""I am dying"""
		print "{} is being destroyed ".format(self.name)
		Robot.population -= 1
		if Robot.population == 0:
			print "{} was the last one ".format(self.name)
		else:
			print "There are still {:d} robots working".format(Robot.population)
	def say_hi(self):
		"""Greetings by the robot
			Yeah, they can do that
		"""

		print "Greetings, my master call me {}".format(self.name)
	@classmethod
	def how_many(cls):
		"""prints the current population"""
		print "We have {:d} robots".format(cls.population)

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3P0")
droid2.say_hi()
Robot.how_many()

print "\nRobots can do come work here.\n"
print "\nRobots have done their work, so let's destroy them"

droid1.die()
droid2.die()

Robot.how_many()