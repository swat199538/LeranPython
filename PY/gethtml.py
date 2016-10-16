# encoding = 'UTF-8'
import urllib.request


def get_html(url):
    parge = urllib.request.urlopen(url).read()
    parge = parge.decode('UTF-8')
    return parge

html = get_html("http://www.baidu.com")
f = open(".\\web.html", 'a', encoding='utf-8')
f.write(html)
f.close()

