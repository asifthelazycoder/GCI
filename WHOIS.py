from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from sys import exit as out

#Initializing 3 lists for 3 columns
name = []
dates = []
reg = []

#Getting query from user
rquery = input("Enter name or email: ")
if " " in rquery.strip():
    cquery = rquery.replace(" ", "+")
else:
    cquery = rquery

#Getting the source code
url = "https://viewdns.info/reversewhois/?q={}".format(cquery)
hdr = {"User-Agent": "Mozilla"}
req = Request(url, headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, 'lxml')

#Checking if atleast 1 result is found
table = soup.find('table', border="1")
if not table:
    print("There are 0 domains that matched this search query.")
    out()
        
#Getting data from table  
rows = table.find_all('tr')
for row in rows:
    name.append(str(row.find_all('td')[0].text))
    dates.append(str(row.find_all('td')[1].text))
    reg.append(str(row.find_all('td')[2].text))

print("There are {} domains that matched this search query.\n".format(len(name)-1))

#Storing data in dictionary
data = dict()
for x in range(len(name)):
    data[str(x)] = name[x] + ", " + dates[x] + ", " + reg[x]
    
#Result
for key, value in data.items():
    if key == "0":
        print("-->", value, "\n")
    else:
        print(key + ".", value)


