from bs4 import BeautifulSoup
import requests
url = "https://mcversions.net/"
HTML = requests.get(url)
#HTML.encoding = "utf-8"
HTML = HTML.text
soup = BeautifulSoup(HTML,"html.parser")
soup_t = soup.prettify()
s = soup.find_all("strong",class_="version")
li = soup.find_all("li",class_="list-group-item release")
for i in s:
    print(i)
for i in li:
    print(i)