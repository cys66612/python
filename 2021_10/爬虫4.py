import urllib.request

respone=urllib.request.urlopen('https://www.python.org')
print(type(respone))
#print(respone.read().decode('utf-8'))