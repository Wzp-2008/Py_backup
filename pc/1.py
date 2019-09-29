import bu
import requests
url = "www.baidu.com"
HTML = requests.get(url)
HTML.encoding = "utf-8"
HTML = HTML.text
