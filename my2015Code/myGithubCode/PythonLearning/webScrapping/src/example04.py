from selenium import webdriver
import time
import csv

url = "https://in.groups.yahoo.com/neo/groups/KeerthiChalet/conversations/messages"

fp = webdriver.FirefoxProfile("C:\\Users\\animeshb\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\u55ebw2r.automation")
driver = webdriver.Firefox(fp)

driver.get(url)



# yg-msglist-auth yg-msglist-auth-mobile

person = {}
tempList = []

print "Sleeppiiing ------------------> "
time.sleep(10)

# yg-msglist-id

idNoTotal = driver.find_element_by_class_name("yg-msglist-id")

print "idNoTotal.text: ", idNoTotal.text

while len(tempList) != (int(idNoTotal.text)):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    

    tempList = driver.find_elements_by_class_name("yg-msglist-auth")
    print "len(tempList): ", len(tempList)
    time.sleep(3)

count = 0

for x in tempList:
    if x.text not in person:
        person[x.text] = 1
        print person
        print "\n\n"
    else:
        person[x.text] +=1
        

with open('names.csv', 'w') as csvfile:
    fieldnames = ['DisplayName', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    # writer.writerow(person)
    for k,v in person.iteritems():
        writer.writerow((k,v))
