import requests 
from bs4 import BeautifulSoup
import json
import os

#HTTP 요청
response = requests.get('https://madelen2016.github.io/class/')
#print(response)

htmlObj = response.content
#print(htmlObj)

bsObj = BeautifulSoup( htmlObj , 'html.parser') 
#print(bsObj)

listObj= bsObj.select('body > a')  #a 태그만 추출
#print(listObj)

dictObj= {}
for i in listObj :
        dictObj[i.text] = i.get('href')
print(dictObj)
        
for item in dictObj :        
    print(item, '  >  ', dictObj [item])


with open(os.path.join('result.json'), 'w+') as json_file:
    json.dump(dictObj, json_file)

