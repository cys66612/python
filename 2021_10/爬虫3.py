import urllib.request
import urllib.parse
import json

char = input("请输入你想要翻译的中文：")
url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
date = {}
head={}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
date['i'] = char
date['from']='en'
date['to']='zh-CHS'
date['smartresult']= 'dict'
date['client']='fanyideskweb'
date['salt']='16340445584440'
date['sign']='152aad891da84b01dc04c8f219fcec07'
date['lts']='1634044558444'
date['bv']='5f70acd84d315e3a3e7e05f2a4744dfa'
date['doctype']='json'
date['version']='2.1'
date['keyfrom']='fanyi.web'
date['action']='FY_BY_CLICKBUTTION'

date=urllib.parse.urlencode(date).encode('utf-8')
req=urllib.request.Request(url,date, head)
response=urllib.request.urlopen(req)
html=response.read().decode('utf-8')
#print(html)
target=json.loads(html)
#print(target)
print("翻译结果是:%s " % (target['translateResult'][0][0]['tgt']))