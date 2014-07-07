import re
import requests
import simplejson as json
from bs4 import BeautifulSoup 



def parse(link):
	resp = requests.get(url=str(link),cookies={"over18":"1"})
	soup = BeautifulSoup(resp.text)
	print(resp)
	print(link)
	tittle = soup.find(id="main-container").contents[1].contents[2].contents[1].string
	date = soup.find(id="main-container").contents[1].contents[3].contents[1].string
	print(tittle)
	print(date)
	t={}
	t["標題"]=str(tittle)
	t["日期"]=str(date)
	
	g = json.dumps(t,ensure_ascii=False,indent=4)
	f2 = open('ptt_title_date.json', 'a')
	f2.write(g+',')
	f2.close
	#print(g)

f = open('pttlink.txt','r')   
for line in f.readlines():
	link = re.search("http:.*html",line).group()
	print (link)
	try:
		parse(str(link))
	except:
		pass
f2 = open('ptt.json','a')
f2.write(']')
f2.close	
 

#f.close()   
   


    
    








