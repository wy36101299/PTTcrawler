import re
import sys
import json
import requests
from time import sleep
from bs4 import BeautifulSoup  

def crawler(start,end):
	page = start; times = end-start+1; g_id = 0;
	for a in range(times):
		print('index is '+ str(page))
		resp = requests.get(
		url="http://www.ptt.cc/bbs/Gossiping/index"+str(page)+".html", 
		cookies={"over18": "1"}
		)
		soup = BeautifulSoup(resp.text)
		for tag in soup.find_all("div","r-ent"):
			try:
				link = str(tag.find_all("a"))
				link = link.split("\"")
				link = "http://www.ptt.cc"+link[1]
				g_id = g_id+1
				parseGos(link,g_id)
			except:
			    pass
		sleep(0.2)
		page += 1
def parseGos(link , g_id):
	resp = requests.get(url=str(link),cookies={"over18":"1"})
	soup = BeautifulSoup(resp.text)
	print(resp)
	# author
	author  = soup.find(id="main-container").contents[1].contents[0].contents[1].string.replace(' ', '')
	# title
	title = soup.find(id="main-container").contents[1].contents[2].contents[1].string.replace(' ', '')
	# date
	date = soup.find(id="main-container").contents[1].contents[3].contents[1].string
	# ip
	try:
		ip = soup.find(text=re.compile("※ 發信站:"))
		ip = re.search("[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*",str(ip)).group()
	except:
		ip = "ip is not find"
	# content
	a = str(soup.find(id="main-container").contents[1])
	a = a.split("</div>")
	a = a[4].split("<span class=\"f2\">※ 發信站: 批踢踢實業坊(ptt.cc),")
	content = a[0].replace(' ', '').replace('\n', '').replace('\t', '')
	# message
	num , all , g , b , n ,message = 0,0,0,0,0,{}
	for tag in soup.find_all("div","push"):
		num += 1
		push_tag = tag.find("span","push-tag").string.replace(' ', '')
		push_userid = tag.find("span","push-userid").string.replace(' ', '')
		push_content = tag.find("span","push-content").string.replace(' ', '').replace('\n', '').replace('\t', '')
		push_ipdatetime = tag.find("span","push-ipdatetime").string.replace('\n', '')

		message[num]={"狀態":push_tag,"留言者":push_userid,"留言內容":push_content,"留言時間":push_ipdatetime}
		if push_tag == '推 ':
			g += 1
		elif push_tag == '噓 ':
			b += 1
		else:
			n += 1			
	messageNum = {"g":g,"b":b,"n":n,"all":num}
	# json-data
	d={ "a_ID":g_id , "b_作者":author , "c_標題":title , "d_日期":date , "e_ip":ip , "f_內文":content , "g_推文":message, "h_推文總數":messageNum }
	json_data = json.dumps(d,ensure_ascii=False,indent=4,sort_keys=True)+','
	
	store(json_data) 
	
def store(data):
    with open('data.json', 'a') as f:
        f.write(data)

store('[') 

crawler(int(sys.argv[1]),int(sys.argv[2]))


store(']') 
with open('data.json', 'r') as f:
	p = f.read()
with open('data.json', 'w') as f:
	f.write(p.replace(',]',']'))
