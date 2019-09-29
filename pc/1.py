from bs4 import BeautifulSoup
import requests
url = "https://fanyi.baidu.com/?aldtype=16047#en/zh/Zoom"
HTML = requests.get(url)
HTML.encoding = "utf-8"
HTML = HTML.text
soup = BeautifulSoup(HTML)
soup_t = soup.prettify()
p = soup.find_all("p")
print(p)