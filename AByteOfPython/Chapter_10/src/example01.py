shoplist = ['apple','mango','carrot', 'banana']

print "I have ", len(shoplist), "items to purchase"

print "These Items are: "
for item in shoplist:
	print item,

print "\n\nI also have to buy rice."
shoplist.append("rice")

print "My Shopping list is now ", shoplist

print "I will also sort my list"
shoplist.sort()

print "The first item I will buy is ", shoplist[0]

oldItem = shoplist[0]
del shoplist[0]

print "I bought the ", oldItem
print "My Shopping list is now ", shoplist