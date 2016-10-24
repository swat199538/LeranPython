# _*_ encoding:utf-8 _*_
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


def print_key(text, words):
    soup = BeautifulSoup(text, "html.parser")

    # word
    span = soup.find('span', class_='keyword')

    # word's phonetic symbol
    span2 = soup.find('span', class_='phonetic')

    # word's Chinese meaning
    div = soup.find('div', class_='trans-container')
    try:
        li = div.find_all('li')
        strings = []
        for keywords in li:
            abc = keywords.get_text()
            strings.append(abc)

        a = span.get_text()
        b = span2.get_text()
        # c = li.get_text()

        str = ('<br>').join(strings)

        sql = 'INSERT INTO cet_words ( `word`, `phonetic_symbol`, `mean`) VALUES  ( "{0}", "{1}", "{2}" );'.format(a, b, str)
        print sql
        file_values = open('wordsql.txt', 'a')
        file_values.write(sql)
        file_values.write('\r\n')
        file_values.close()
    except:
        file_values = open('log.txt', 'w')
        file_values.write(words)
        file_values.write('\r\n')
        file_values.close()

fname = 'seed.xlsx'
bk = xlrd.open_workbook(fname)

try:
    sh = bk.sheet_by_name('Sheet1')
except:
    print 'no sheet1'

nrows = sh.nrows

count = range(0, nrows)

url = 'http://www.youdao.com/w/eng/'



for index in count:
    word = sh.cell_value(index, 0)
    html = load_html(url, word)
    print_key(html.text, words=word)

print 'success'
