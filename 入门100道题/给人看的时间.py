#给人看的时间
import time
for i in range(4):
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))#time.time()返回的是系统时间戳 time.localtiem(time.time())返回本地时间组成的元组
    time.sleep(1)