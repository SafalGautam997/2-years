import requests
from lxml import html
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
res = requests.get("https://www.reddit.com/r/PewdiepieSubmissions/top/", headers=headers)
post_title = html.fromstring(res.content)
print(post_title.xpath('//h3[@class="_eYtD2XCVieq6emjKBH3m"]/text()'))
