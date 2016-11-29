import csv


with open('../rest/csvs/mylist_14_05_2015.csv', 'rb') as csvfile1:
   with open('../rest/csvs/mylist_15_05_2015.csv', 'rb') as csvfile2:
	reader1 = (csv.DictReader(csvfile1))
	reader2 = (csv.DictReader(csvfile2))

	csv1Rows = [x for x in reader1]
	csv2Rows = [x for x in reader2]

	print len(csv1Rows), len(csv2Rows)

	def getDiff(csv1Rows, csv2Rows):
	    # see which rows are in csv1 but not 2
	    diff = []
	    for row in csv1Rows:
	        if row not in csv2Rows:
	            diff.append(row)

	    # see which rows are in csv2, but not csv1
	    # for row in csv2Rows:
	    #     if row not in csv1Rows:
	    #         diff.append(row)

	    # get rid of duplicates
	    # noDupesDiff = []
	    # for row in diff:
	    #     if row not in noDupesDiff:
	    #         noDupesDiff.append(row)

	    return diff
	
	diff = getDiff(csv1Rows, csv2Rows)

	
	print len(diff)

	for x in diff:
		print x

	def setDiff(csvfile1,csvfile2):
		print "setDiff"
		old, new = set(csvfile1), set(csvfile2)
		print old,new
		
		for added in new - old:
			print 'added', added
		for deleted in old - new:
			print('deleted', deleted)

	print setDiff(csvfile1,csvfile2)