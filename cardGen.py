import codecs
import requests
import re

from bs4 import BeautifulSoup
cards_file = codecs.open("cards.csv", "w", "utf-8")
#input_verbs_file=open('verbs.txt',"r")
#lines=input_verbs_file.readlines()
result=[]
separator="*"
#english_verb
#print(result[1].split(',')[1])

#german_verb
#print(result[1].split(',')[0])

#divTag=soup.find_all("div", {"class": "blue-box-wrap"})
#person=divTag.find_all("i", {"class": "graytxt"})
url =  'https://learngerman.dw.com/en/grammar'
baseurl =  'https://learngerman.dw.com'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, features="lxml", from_encoding='utf-8')
#aTag=soup.find_all("div", {"class": "col-xs-12"})
#aTag=soup.find_all("a")
aTag=soup.find_all("a", {"href": re.compile("\/gr-")})
print("Articles found: " + str(len(aTag)))
for x in range(len(aTag)):
#for x in range(0,3):
    contenturl =  baseurl + aTag[x].get('href')
    resp = requests.get(contenturl)
    contentsoup = BeautifulSoup(resp.text, features="lxml", from_encoding='utf-8')
    h=contentsoup.find("h2")
    content=contentsoup.find("div", {"class": "richtext-content-container"})
    print(str(x) + ". "  + h.text.replace('\n', ' ').replace('\r', ''))
    #print(str(content).decode('utf-8').replace('\n', ' ').replace('\r', ''))
    cards_file.write(str(h).decode('utf-8').replace('\n', ' ').replace('\r', '') + separator + str(content).decode('utf-8').replace('\n', ' ').replace('\r', '') + '\n')

    #print(content)
#https://learngerman.dw.com/en/simple-past-irregular-verbs/gr-39001619
#print(divTag[2])
cards_file.close()
