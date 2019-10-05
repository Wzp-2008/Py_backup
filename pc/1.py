from bs4 import BeautifulSoup
import requests
url = "https://translate.google.cn/?hl=zh-CN#view=home&op=translate&sl=en&tl=zh-CN&text=Hello!"
HTML = requests.get(url)
#HTML.encoding = "utf-8"
HTML = HTML.text
soup = BeautifulSoup(HTML,"html.parser")
soup_t = soup.prettify()
p = soup.find_all("div",class_="result-shield-container tlid-copy-target")
print(p)