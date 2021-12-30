import urllib.parse
import urllib.request

data=bytes(urllib.parse.urlencode({'world':'hello'}), encoding='utf8')
respone=urllib.request.urlopen('http://httpbin.org/post',data=data)
print(respone.read())