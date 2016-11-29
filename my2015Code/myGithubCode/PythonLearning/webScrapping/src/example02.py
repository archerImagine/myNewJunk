from selenium import webdriver
import time
url = "https://in.groups.yahoo.com/neo/groups/KeerthiChalet/members/all"


#http://stackoverflow.com/questions/15954682/setting-selenium-to-use-custom-profile-but-it-keeps-opening-with-default

fp = webdriver.FirefoxProfile("C:\\Users\\animeshb\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\u55ebw2r.automation")
driver = webdriver.Firefox(fp)

# link = driver.find_element_by_link_text('KeerthiChalet')

# link.click()

driver.get(url)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# screenreader-infobox

# element = driver.find_element_by_id("screenreader-infobox")
# liLink = driver.find_element_by_class_name("gstats")

# memberList = driver.find_element_by_id("yg-members-list")

# print memberList.size

#yg-members-list
# gstats

# print dir(element)
# print dir(liLink)

# print "liLink.text: ", liLink.text

emailList = []
# print type(emailList), len(emailList), emailList
print type(emailList)

while len(emailList) < 109:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    tempList = driver.find_elements_by_class_name("yg-email")
    emailList = tempList[:]
    print type(emailList)
    print "len(emailList): ", len(emailList), " len(tempList): ", len(tempList)
    time.sleep(10)

print emailList[0].text

print type(emailList)

for x in emailList:
    print x.text

# print "element.text: ", element.value

# http://stackoverflow.com/questions/26566799/selenium-python-how-to-wait-until-the-page-is-loaded
# link = driver.find_element_by_link_text('KeerthiChalet')
# link.click()