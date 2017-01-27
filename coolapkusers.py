#coding=utf-8
import re
import requests

for i in range(784579, 790156):#2017年1月24日 10:13:08
    raw = requests.get('http://coolapk.com/u/'+str(i)).text
    a = re.findall('setTimeout', raw)
    if not a == []:
        with open('reserved.txt', 'a') as reserved:
            reserved.write(str(i)+'\n')
        continue
    
    b = re.findall('alt="(\S+)"', raw)
    if not b == []:
        dt = re.findall(r'<strong>(\d+)</strong>动态', raw)[0]
        yy = re.findall(r'<strong>(\d+)</strong>应用关注', raw)[0]
        fx = re.findall(r'<strong>(\d+)</strong>发现', raw)[0]
        fs = re.findall(r'<strong>(\d+)</strong>好友关注', raw)[0]
        try:
            with open('users.csv', 'a') as users:
                users.write(str(i)+','+b[0]+','+dt+','+yy+','+fx+','+fs+'\n')
        except UnicodeEncodeError:
            with open('unicode.txt', 'a') as un:
                un.write(str(i)+'\n')
        except:
            with open('others.txt', 'a') as others:
                others.write(str(i)+'\n') 
    else:
        with open('others.txt', 'a') as others:
            others.write(str(i)+'\n') 
