import sys
import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')


def load_html(url, param):
    full_url = url+'/'+param
    headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    r = requests.get(full_url, params=None, headers=headers)
    return r


def print_key(text):
    soup = BeautifulSoup(text, "html.parser")

    # word
    span = soup.find('span', class_='keyword')
    print span.get_text()

    # word's phonetic symbol
    span2 = soup.find('span', class_='phonetic')
    print span2.get_text()

    # word's Chinese meaning
    div = soup.find('div', class_='trans-container')
    li = div.find('li')
    print li.get_text()


words = ['apple', 'banana', 'teach', 'code', 'fire']

for key in words:
    url = 'http://www.youdao.com/w/eng/'
    html = load_html(url, key)
    print_key(html.text)





