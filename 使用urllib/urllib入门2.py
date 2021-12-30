import urllib.request

respone=urllib.request.urlopen('https://www.python.org')
print(respone.status)
print(respone.getheaders())
print(respone.getheader('Sever'))