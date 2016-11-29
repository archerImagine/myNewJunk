


myHeader = []

def findHeader(header):
    print "EXAMPLE02: ",header
    for row in header:
        print "EXAMPLE02: ", row
        for newRow in row:
            # print "EXAMPLE02: newRow", newRow, newRow.text
            if newRow.text is not None:
                myChild = newRow.getchildren()
                if len(myChild) == 2:
                    for x in myChild:
                        for y in x:
                            if y.text is not None:
                                myHeader.append(y.text.encode('ascii','ignore'))
            else:
                myChild = newRow.getchildren()
                for x in myChild:
                    if x.text is not None:
                        myHeader.append(x.text.encode('ascii','ignore'))
    return myHeader