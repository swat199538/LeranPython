import sys
import xlrd
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

    # word's phonetic symbol
    span2 = soup.find('span', class_='phonetic')

    # word's Chinese meaning
    div = soup.find('div', class_='trans-container')
    li = div.find('li')

    a = span.get_text()
    b = span2.get_text()
    c = li.get_text()
    print b
    sql = "INSERT INTO words ( `word`, `phonetic_symbol`, `mean`) VALUES  ( '%s', '%s', '%s' );" % (a, b, c)
    print sql

'''for key in words:
    url = 'http://www.youdao.com/w/eng/'
    html = load_html(url, key)
    print_key(html.text)
'''


fname = 'seed.xlsx'
bk = xlrd.open_workbook(fname)

try:
    sh = bk.sheet_by_name('Sheet1')
except:
    print 'no sheet1'

nrows = sh.nrows

count = range(0, nrows+1)

url = 'http://www.youdao.com/w/eng/'

for index in count:
    word = sh.cell_value(index, 0)
    html = load_html(url, word)
    print_key(html.text)






