import example02



def findProperBody(myChild):
    detailRow = []
    myName = myChild.find("td[@headers='name_header']")
    myUserID = myChild.find("td[@headers='userid_header']")
    myPhone = myChild.find("td[@headers='phone_header']")
    myBuilding = myChild.find("td[@headers='building_header']")
    myTitle = myChild.find("td[@headers='title_header']")
    myOrg = myChild.find("td[@headers='organization_header']")

    detailRow.append(myName.getchildren()[0].text.encode('ascii','ignore'))
    detailRow.append(myUserID.getchildren()[0].text.encode('ascii','ignore'))
    if len(myPhone.getchildren()) == 2:
        if type(myPhone.getchildren()[0].text) is str:
            detailRow.append(myPhone.getchildren()[0].text.encode('ascii','ignore'))
        else:            
            detailRow.append(myPhone.getchildren()[0].getchildren()[0].text.encode('ascii','ignore'))
    else:
        detailRow.append(" ")
    detailRow.append(myBuilding.getchildren()[0].text.encode('ascii','ignore'))        
    detailRow.append(myTitle.getchildren()[0].getchildren()[0].text.encode('ascii','ignore'))
    detailRow.append(myOrg.getchildren()[0].getchildren()[0].text.encode('ascii','ignore'))
    return detailRow



# writeCSV()

# findProperBody(example02.body[8])    