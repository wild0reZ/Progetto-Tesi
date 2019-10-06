from bs4 import BeautifulSoup

file = open('./testingFiles/a.xml','r')
contents = file.read()
soup = BeautifulSoup(file, 'xml')

jobs = soup.find_all('job')
print(soup)
