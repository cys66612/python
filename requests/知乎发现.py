import requests
import re

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

r=requests.get('https://www.zhihu.com/explore',headers=headers)
patten=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
title=re.findall(patten,r.text)
print(title)