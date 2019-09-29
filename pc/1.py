import beautifulsoup4
import requests
url = "www.baidu.com"
HTML = requests.get(url)
HTML.encoding = "utf-8"
HTML = HTML.text
