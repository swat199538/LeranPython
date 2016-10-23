# _*_ coding: utf-8 _*_
import urllib2

response = urllib2.urlopen('http://www.bing.com')

a = response.read()

print a

fileObjec = open('./baidu.html', 'w+')
fileObjec.write(a)
fileObjec.close()

