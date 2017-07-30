#coding=utf-8
import time
import requests
import libaso

start = 10001
end =  1070920
ends = str(end)

headers1 = {
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Z2 Plus Build/N2G47O) +CoolMarket/6.10.6',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Sdk-Int': '25',
    'X-Sdk-Locale': 'en-US',
    'X-App-Id': 'coolmarket',
    'X-App-Version': '6.10.6',
    'X-App-Code': '1608291'
}

apiurl = 'https://api.coolapk.com/v6/user/profile?uid='

def downloader(url):
    headers1['X-App-Token'] = libaso.getAS() #LOL
    headers=headers1
    raw = requests.get(url, headers=headers, timeout=5)
    return raw

with open('starttime'+ends+'.txt','a') as st:
    st.write(time.ctime()+'\n')

for i in range(start,end):
    si = str(i)
    url = apiurl+si
    try:
        apidata = downloader(url)
    except:
        print(si)
        continue

    try:
        apijson = apidata.json()
    except:
        with open('err'+ends+'.txt','a') as errs:
            errs.write(si+'\n')
        continue

    if 'message' in apijson:
        with open('revs'+ends+'.csv', 'a',encoding='utf-8') as revs:
            revs.write(si+','+apijson['message']+'\n')
        continue

    username = apijson['data']['username']#用户名

    feed = str(apijson['data']['feed'])#动态数
    follow = str(apijson['data']['follow'])#关注数
    fans = str(apijson['data']['fans'])#粉丝数
    # albumFavNum = str(apijson['data']['albumFavNum'])#喜欢应用集数,上古api不统计    
    # apkCommentNum = str(apijson['data']['apkCommentNum'])#应用评论数,上古api不统计
    albumNum = str(apijson['data']['albumNum'])#应用集数
    apkFollowNum = str(apijson['data']['apkFollowNum'])#关注应用数
    apkRatingNum = str(apijson['data']['apkRatingNum'])#评分数    
    discoveryNum = str(apijson['data']['discoveryNum'])#发现数

    weibo = apijson['data']['weibo']#微博
    blog = apijson['data']['blog']#博客
    bio = apijson['data']['bio']#签名

    province = apijson['data']['province']#省
    city = apijson['data']['city']#市

    astro = apijson['data']['astro']#星座
    gender = str(apijson['data']['gender'])#性别，-1未填写，1男，0女

    groupname = apijson['data']['groupName']#管理员附加组
    usergroupname = apijson['data']['userGroupName']#用户等级


    isDeveloper = str(apijson['data']['isDeveloper'])#开发者
    apkDevNum = str(apijson['data']['apkDevNum'])#开发应用数量
    
    logintime = str(apijson['data']['logintime'])#最后登录时间


    with open('feed'+ends+'.csv','a',encoding='utf-8') as feeds:
        feeds.write(si+','+username+','+feed+'\n')
    with open('follow'+ends+'.csv','a',encoding='utf-8') as follows:
        follows.write(si+','+username+','+follow+'\n')
    with open('fans'+ends+'.csv','a',encoding='utf-8') as fanss:
        fanss.write(si+','+username+','+fans+'\n')
    # with open('albumFavNum'+ends+'.csv','a',encoding='utf-8') as albumFavNums:
        # albumFavNums.write(si+','+username+','+albumFavNum+'\n')
    # with open('apkCommentNum'+ends+'.csv','a',encoding='utf-8') as apkCommentNums:
        # apkCommentNums.write(si+','+username+','+apkCommentNum+'\n')    
    with open('albumNum'+ends+'.csv','a',encoding='utf-8') as albumNums:
        albumNums.write(si+','+username+','+albumNum+'\n') 
    with open('apkFollowNum'+ends+'.csv','a',encoding='utf-8') as apkFollowNums:
        apkFollowNums.write(si+','+username+','+apkFollowNum+'\n')
    with open('apkRatingNum'+ends+'.csv','a',encoding='utf-8') as apkRatingNums:
        apkRatingNums.write(si+','+username+','+apkRatingNum+'\n')
    with open('discoveryNum'+ends+'.csv','a',encoding='utf-8') as discoveryNums:
        discoveryNums.write(si+','+username+','+discoveryNum+'\n')

    if weibo != '': 
        with open('weibo'+ends+'.csv', 'a', encoding='utf-8') as weibos:
            weibos.write(si+','+username+','+weibo+'\n')    
    if blog != '':
        with open('blog'+ends+'.csv', 'a', encoding='utf-8') as blogs:
            blogs.write(si+','+username+','+blog+'\n')        
    if bio != '':
        bio = bio.replace('\n',' ').replace(',',' ').replace('\r\n',' ')
        with open('bio'+ends+'.csv', 'a', encoding='utf-8') as bios:
            bios.write(si+','+username+','+bio+'\n')            

    if province != '':
        with open('local'+ends+'.csv', 'a', encoding='utf-8') as locals:
            locals.write(si+','+username+','+province+','+city+'\n')    

    if gender != '-1':
        with open('gender'+ends+'.csv', 'a',encoding='utf-8') as genders:
            genders.write(si+','+username+','+gender+'\n')
    if astro != '':
        with open('astro'+ends+'.csv', 'a',encoding='utf-8') as astros:
            astros.write(si+','+username+','+astro+'\n')

    if usergroupname != None:
        with open('usergroupname'+ends+'.csv','a',encoding='utf-8') as usergroupnames:
            usergroupnames.write(si+','+username+','+usergroupname+'\n')
    if groupname != None:
        with open('groupname'+ends+'.csv','a',encoding='utf-8') as groupnames:
            groupnames.write(si+','+username+','+groupname+'\n')

    if isDeveloper == '1':
        with open('developer'+ends+'.csv','a',encoding='utf-8') as developers:
            developers.write(si+','+username+','+apkDevNum+'\n')

    if logintime != 'None':
        with open('logintime'+ends+'.csv','a',encoding='utf-8') as logintimes:
            logintimes.write(si+','+username+','+logintime+'\n')

with open('endtime'+ends+'.txt','a') as et:
    et.write(time.ctime()+'\n')