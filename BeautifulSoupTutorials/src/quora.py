from bs4 import BeautifulSoup
import urllib2

url = "http://localhost/myGithubCode/PythonLearning/BeautifulSoupTutorials/html/quora.html"

page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

# print soup.prettify()

soup.prettify()

spanLink = soup.find_all("span", {"class": "link_text"})

for span in spanLink:
	print span.text