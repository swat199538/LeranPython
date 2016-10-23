# _*_ coding: utf-8 _*_
import sys
import requests

reload(sys)
sys.setdefaultencoding('utf8')

paramss = {"wd": "python"}

headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

r = requests.get('https://www.baidu.com/s', params=paramss, headers=headers)
print r.url
abc = r.text

abc.encode('utf-8')

files = open('./abcd.html', 'w')
files.write(abc)
files.close()
