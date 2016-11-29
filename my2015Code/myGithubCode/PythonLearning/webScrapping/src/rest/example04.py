import example01,example02,example03
import csv
import time

tree = example01.queryServer(1)


mytree  = tree.xpath("//table[@id='resultsTable']")
myCount = tree.xpath("//div[@class='alignRight']")

countString = myCount[0].text
myTotalCount = countString[countString.find("of ")+2:countString.find("m")]
myTotalCountInt = int(myTotalCount)

myHeader = mytree[0].getchildren()[0]
myBody = mytree[0].getchildren()[1]

def writeCSV(myBody):    
    for x in range(len(myBody)):
        handle.writerow(example03.findProperBody(myBody[x]))
    return x

with open('csvs/mylist_'+time.strftime("%Y-%m-%d")+'.csv', 'wb') as csvfile: #%d-%m-%Y
    count = 1    
    handle = csv.writer(csvfile)
    handle.writerow(example02.findHeader(myHeader))
    rowsWritten = writeCSV(myBody)
    while rowsWritten + len(myBody) != myTotalCountInt:
        count += 1
        tree = example01.queryServer(count)
        mytree  = tree.xpath("//table[@id='resultsTable']")
        myBody = mytree[0].getchildren()[1]
        rowsWritten += writeCSV(myBody)
        print "EXAMPLE04 2) : ", rowsWritten + len(myBody), myTotalCountInt, count, len(myBody)
    