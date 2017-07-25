#!/usr/bin/python2.7

from bs4 import BeautifulSoup
import urllib2
import re
#open file and return string

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_file():
	adss=raw_input("file name:")
	try:
		print adss
		f=open(adss,"r+")
		text=f.read()
	except :
		print "FILE NOT OPEN!!!"
		exit()
	finally:
		f.close()
	return text
#wordlist to counted sorted list
def words_conut(list):
	dic={}
	for word in list:
		if word in dic:
			dic[word]+=1
		else:
			dic[word]=1
	arr=sorted(dic.iteritems(),key=lambda item:item[1],reverse=True)
	return arr
def words_info(word):
	info=[]
	spAll=[]
	url="http://www.iciba.com/"+word
	#
	html=urllib2.urlopen(url).read()
	soup=BeautifulSoup(html,"html.parser",from_encoding="utf-8")
	speak=soup.find_all("div",class_="base-top-voice")
	#speak
	sp2=soup.select(".base-speak span span")
	result=[]
	speak2=""
	for sp_lst in sp2:
		speak2=speak2+str(sp_lst.string)
	print speak2
	result.append(speak2)#append a string
	#mean
	m_lst=soup.select("div div div div div ul li span")
	content=""
	for item in m_lst:
		content=content+str(item.string)
	content=content[:-4]
	print content
	result.append(content) #append a string
	return result  #return["1","2"]

	#word count info write]
def writeinfo(list):
	file=open("result.txt","a+")
	try:
		for item in list:
			file.write(item+"\n")
	except :
		print "CANT WRITE!!!"
	finally:
		file.close()
			
		
	



	
#file --> list
st=get_file()
word_list=re.findall(r"\b[a-zA-Z']+\b",st)
list_ctst=words_conut(word_list)
means=[]
for (i,j) in list_ctst:
	info1=str(i)+":"+str(j)
	means.append(info1)
	get=words_info(i)
	for item in get:
		means.append(item)
print means
writeinfo(means)

# means= words_info('do')


