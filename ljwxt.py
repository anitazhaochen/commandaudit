#-*-coding:utf-8 -*-
import urllib
from urllib import request,parse



url = "http://zhjw.dlnu.edu.cn/"
req = request.Request(url)
resp = urllib.request.urlopen(req)
cookie = resp.headers['Set-Cookie']

url = "http://zhjw.dlnu.edu.cn/loginAction.do"
headers = {
"Cookie":cookie
}

form = {
"ldap":"auth",
"zjh":"2015081327",
"mm":"zc19951213"
}
postData = parse.urlencode(form).encode('UTF-8')

req = request.Request(url,headers=headers,data=postData)

resp = urllib.request.urlopen(req)

#print(resp.headers)
print(resp.read().decode('gbk'))

url = "http://zhjw.dlnu.edu.cn/xkAction.do?actionType=17"

headers = {
"Cookie":cookie
}
req = request.Request(url,headers=headers)

resp = urllib.request.urlopen(req)

print(resp.read().decode('gbk'))
url = "http://zhjw.dlnu.edu.cn/xkAction.do"
form = {
"actionType":6,
"pageNumber":0,
"xzkzh":"tsxx000",
}
postData = parse.urlencode(form).encode('UTF-8')
req = request.Request(url,headers=headers,data=postData)
resp = urllib.request.urlopen(req)

url = "http://zhjw.dlnu.edu.cn/xkAction.do"
form = {
"kcId":"00000015_02",
"preActionType":6,
"actionType":9,
}
postData = parse.urlencode(form).encode('UTF-8')
req = request.Request(url,headers=headers,data=postData)
resp = urllib.request.urlopen(req)


