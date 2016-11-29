zoo = ('python','elephant','penguin')
print "Number of animal in the zoo is ", len(zoo)

newZoo = 'monkey' ,'camel', zoo
print "No of cages in the new zoo", len(newZoo)

print "All animal in the zoo are", newZoo

print "Animals bought from old zoo are", newZoo[2]
print "Last animal of old zoo is", newZoo[2][2]

print "No of animals in the newZoo is ", len(newZoo) - 1 + len(newZoo[2])

