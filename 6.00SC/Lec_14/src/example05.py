import random 
import pylab

def flipPlot(minExp,maxExp):
	ratios = []
	diffs = []
	xAxis = []

	for exp in range(minExp,maxExp+1):
		xAxis.append(2 ** exp)
	print "xAxis: ", xAxis
			
	for numFlips in xAxis:
		numHeads = 0
		for n in range(numFlips):
			if random.random() < 0.5:
				numHeads += 1
		numTails = numFlips - numHeads
		ratios.append(numHeads/float(numTails))
		diffs.append(abs(numHeads - numTails))

	pylab.title('Difference Between Heads and Tails')
	pylab.xlabel('Number of Flips')
	pylab.ylabel('Abs(#Heads - #Tails')
	pylab.plot(xAxis, diffs)
	pylab.figure()
	pylab.plot(xAxis, ratios)
	pylab.title('Heads/Tails Ratios')
	pylab.xlabel('Number of Flips')
	pylab.ylabel('Heads/Tails')


flipPlot(4,20)	
pylab.show()

