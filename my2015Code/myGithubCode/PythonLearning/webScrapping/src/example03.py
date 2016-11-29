mydict = {
    "Animesh":0,
    "fahim" : 1
}

for x in xrange(1,10):
    mydict["Animesh"] += 1
    if 'unknown' not in mydict:
        mydict['unknown'] = 0
    mydict["unknown"] += 2

for k,v in mydict.iteritems():
    print k,v

print mydict, len(mydict)