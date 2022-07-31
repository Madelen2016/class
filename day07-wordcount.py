from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv


url = "http://www.pythonscraping.com/pages/warandpeace.html"

try :
    htmlObj = urlopen(url)
except :
    print("요청이 제대로 되지 않았습니다")
else :
    bsObj = BeautifulSoup(htmlObj, "lxml")

    print(bsObj.prettify())

diaList = bsObj.findAll("span", {"class" : "red"})
 
for dia in diaList :
        print(dia.get_text() + "\n\n")

print("이 페이지에 존재하는 대사는 총 " + str(len(diaList)) + "개 입니다!!!")
      
findObj = bsObj.find("span", {"class" : "red"})
textObj = findObj.get_text()

#단어 추출과 관계없는 문자 제거하기
textObj = textObj.replace("\n" , "")
textObj = textObj.replace("-" ,  "")
textObj = textObj.replace(", " ,  "")

#긴 문자열을 공백을 기준으로 분리하기
splObj = textObj.split(" ")     # 리스트 반환
print(splObj)

word_freq = {}    # 단어와 빈도수를 쌍으로 저장할 딕셔너리 생성

for  word  in  splObj :
    word_freq.setdefault(word, 0) #모든 단어의 빈도수 값을 0으로 초기화
    word_freq[word] += 1     # 각 단어의 카운트를 증가시킴
    
print(word_freq)

xList=[ ]    # x축 자료로 사용할 단어 이름들을 저장할 리스트 생성
yList=[ ]    # y축 자료로 사용할 각 단어의 빈도수들을 저장할 리스트 생성

for  word  in word_freq :
        xList.append(word)
        yList.append(word_freq[word])

print(xList)
print(yList)

from matplotlib import pyplot

pyplot.bar(xList, yList)
pyplot.xlabel("word")
pyplot.ylabel("frequency")
pyplot.title("words' frequency")

pyplot.show ()

with open("wordcount.csv", "w") as myFile :  # 소스 코드와 같은 폴더에 wordcount.csv 이름으로 저장된다 
    myFile.write("words, frequency\n")
    for word in word_freq :
        myFile.write("{0}, {1}\n" .format(word, word_freq[word]))

