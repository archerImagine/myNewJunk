import requests
from lxml import html
import os,time
url = 'http://wwwin-tools.cisco.com/dir/empadvquery.go'
params = {
    "sortOrderAdv":"a",
    "fn":"",
    "mailStop":"",
    "lastName":"",
    "streetAddress":"",
    "userid":"",
    "city":"",
    "telMain":"",
    "state":"",
    "telVoiceMail":"",
    "postalCode":"",
    "telMobile":"",
    "country":"",
    "telOther":"",
    "cubeNumber":"",
    "telFax":"",
    "floor":"",
    "telPager":"",
    "building":"BANGALORE -PRITECH PARK",
    "title":"",
    "employeeType":"Regular",
    "managerName":"",
    "emplid":"",
    "group":"",
    "deptNumber":""
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest',
           'Host': 'wwwin-tools.cisco.com',
           'Referer': 'http://wwwin-tools.cisco.com/dir/details/',
           'Connection' : 'keep-alive',
           'DNT':'1',
           "Cookie": "JSESSIONID=0000VYhvCcIxEIi5jJwwNMt2sZe:29799; DIRWEB25=%5BSHOW_PHOTO_RESULTS%3DY%5D%5BUITEMPLATES%3DL%5D%5BPAGESIZE%3D100%5D%5BEXPAND_HIERARCHY%3DY%5D%5BHOVERUI%3DY%5D%5BBPS%3DN%5D; CP_GUTC=173.37.145.95.1425882457870239; v1st=88494729DB36CB2C; Apache=173.37.253.212.1428381044129959; utag_main=v_id:014c20e256d70015c729ea471dfe0e065002f05d0093c$_sn:4$_ss:1$_st:1431323050185$_pn:1%3Bexp-session$ses_id:1431321250185%3Bexp-session; s_nr=1431321252519-Repeat; ObSSOCookie=C3CcHRVJxD%2FZX4Zg3J2IFvs9c2GQdN5CC9qzWac9v%2B6csZMefLbvSnD5%2BK%2Fg5emTYsEObWzOi%2B03H3gcFPAFIzbyTiCQvCSy6TFSFUk99xEfz%2FMuGQGjjlANjlUn5VAIHUkDGbTQpluZ3XVQ%2F7n5fpMi3X70yS1n0N8eLwKEFIoInMSOMixgA9mDNUMdnn%2FamJX01zz9eXu8z7y%2FGn22sm1AASN0%2FQCI%2BSxxqgv5B19XFL3gdr6CzDJna2nfeJsQKSAp9oIfbPvQwJpE6zyxhNo4iKoQEofHzhrzjLFXpyvQTxZJqaiudrr4du8TkKiY7fzjVO4TfQCivVGHANw%2BngtmSMPqtmvNe05BqvCoEOY%3D"}

# response = requests.get(url, params=params, headers=headers)
# print response, response.status_code
# print response.headers['content-type']
# print response.ok #response.content, 
# tree = html.fromstring(response.content)
# print "tree: ", tree
# print type(response.content)
# rows = tree.xpath("//table[@id='resultsTable']")
# print rows, len(rows)
# data = list()
# for row in rows:
#     for c in row.getchildren():
#         print c

def queryServer(count):        
    params['pageNum'] = str(count)
    response = requests.get(url, params=params, headers=headers)
    # print "EXAMPLE01", response, response.status_code
    # print "EXAMPLE01", response.headers['content-type']
    # print "EXAMPLE01", response.ok #response.content
    # print "EXAMPLE01", response.content
    directory = 'html/' + time.strftime("%d_%m_%Y")
    if not os.path.exists(directory):
        os.makedirs(directory)
    f = open(directory+'/myFile_'+str(count)+'.html', 'w')
    f.write(response.content)
    tree = html.fromstring(response.content)
    return tree


# queryServer(1)    