from  urllib.request  import  urlopen
from  bs4  import  BeautifulSoup

htmlObj = urlopen("https://madelen2016.github.io/class/index.html ")

bsObj = BeautifulSoup(htmlObj, "lxml")
 
#print( bsObj.find('a') )
#print( bsObj.find_all('a') )

findList = bsObj.find_all('a')     #검색 결과 리스트 객체 반환

for i in findList :
    print(i)
