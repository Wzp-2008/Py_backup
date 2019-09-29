from bs4 import BeautifulSoup
import requests
url = "http://www.baidu.com"
HTML = requests.get(url)
HTML.encoding = "utf-8"
HTML = HTML.text
soup = BeautifulSoup(HTML)
soup_t = soup.prettify()
find_all("tr")
print(soup_t)