import sys,time

f = None

try:
	f = open("poems.txt")

	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print line,
		sys.stdout.flush()
		print "Press Ctrl + C now"

		time.sleep(2)
except IOError:
	print "Could Not find file poems.txt"
except KeyboardInterrupt:
	print "!! You cancelled the reading from the file."
finally:
	if f:
		f.close()
	print "Cleaning up: Closed the file"