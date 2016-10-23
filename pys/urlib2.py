import urllib
import urllib2

url = 'https://www.baidu.com/s'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'

values = {'wd': 'python'}

heards = {'User-Agent': user_agent}

data = urllib.urlencode(values)

print data

request = urllib2.Request(url, data, heards)

print request

reponse = urllib2.urlopen(request)

htm = reponse.read()

files = open('baidus.html', 'w')

files.write(htm)

files.close()



