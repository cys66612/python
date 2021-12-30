from urllib import request,parse

url='http://httpbin.org/post'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Host':'httpbin.org',
}
dict={
    'name':'Germey'
}
data=bytes(parse.urlencode(dict),encoding='utf8')
req=request.Request(url=url,data=data,headers=headers,method='POST')
respone=request.urlopen(req)
print(respone.read().decode('utf-8'))