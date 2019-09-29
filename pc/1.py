from bs4 import BeautifulSoup
import requests
url = "https://www.bilibili.com/video/av58329669"
HTML = requests.get(url)
HTML.encoding = "utf-8"
HTML = HTML.text
soup = BeautifulSoup(HTML)
soup_t = soup.prettify
p = soup.find_all("span")
print(p)