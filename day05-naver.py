import urllib.request

client_id = "*******"
client_secret = "*******"
search_text = urllib.parse.quote("빅데이터")
page_start = 1   
display = 5

url = "https://openapi.naver.com/v1/search/news?query=%s&start=%s&display=%s" %(search_text, page_start, display )

reqObj = urllib.request.Request(url)
print(reqObj)

reqObj.add_header("X-Naver-Client-Id", client_id)
reqObj.add_header("X-Naver-Client-Secret", client_secret)

htmlObj = urllib.request.urlopen(reqObj)
print(htmlObj)

htmlObj_body = htmlObj.read()
print(htmlObj_body.decode('utf-8'))
