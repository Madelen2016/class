from urllib.request  import  urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/warandpeace.html"

try :
    htmlObj = urlopen(url)
    
except  :
    print("제대로 요청이 안됩니다")   

else :
    bsObj = BeautifulSoup(htmlObj, "lxml")
    print(bsObj)

nameList = bsObj.findAll( "span", {"class" : "green"} ) 
print(nameList)

princeText = bsObj.findAll(text = "the prince")

n = len(princeText)
print("the prince  "  + str(n) + "회 나타남")
print("-----------------------")

for  i  in princeText :
	print(i)

print("\n\n")
EmpressText = bsObj.findAll(text = "the Empress")

n = len(EmpressText)
print("the Empress  "  + str(n) + "회 나타남")
print("-----------------------")

for  i  in EmpressText :
	print(i)
