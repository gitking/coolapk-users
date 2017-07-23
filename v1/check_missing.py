#coding=utf-8
import re
import requests

f = open('unicode.txt')
for i in f:#2017年1月24日 10:13:08
    raw = requests.get('http://coolapk.com/u/'+str(i[:-1])).text
    b = re.findall('alt="(\S+)"', raw)
    if not b == []:
        dt = re.findall(r'<strong>(\d+)</strong>动态', raw)[0]
        yy = re.findall(r'<strong>(\d+)</strong>应用关注', raw)[0]
        fx = re.findall(r'<strong>(\d+)</strong>发现', raw)[0]
        fs = re.findall(r'<strong>(\d+)</strong>好友关注', raw)[0]
        try:
            with open('1users.csv', 'a') as users:
                users.write(str(i[:-1])+','+dt+','+yy+','+fx+','+fs+'\n')
        except UnicodeEncodeError:
            with open('1unicode.txt', 'a') as un:
                un.write(str(i[:-1])+'\n')
        except:
            with open('1others.txt', 'a') as others:
                others.write(str(i[:-1])+'\n') 
    else:
        with open('1others.txt', 'a') as others:
            others.write(str(i[:-1])+'\n') 
f.close()
