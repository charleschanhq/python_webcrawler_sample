import requests
from bs4 import BeautifulSoup as bp 

url='http://news.qq.com/'
newdata=requests.get(url).text
soup=bp(newdata,'lxml')
titles=soup.select("div.text > em.f14 > a.linkto")
for i in range(len(titles)):
	for n in titles:
		my_title=n.get_text()
		my_link=n.get("href")
		dataset={my_title,my_link}
		print(dataset)

    
