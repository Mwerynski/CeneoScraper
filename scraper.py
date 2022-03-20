from __future__ import print_function
from re import sub
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

urlpage=urlopen("https://www.ceneo.pl/104942408#tab=reviews").read()
bswebpage=BeautifulSoup(urlpage)
results=str(bswebpage.findAll("div",{'class':"user-post__text"}))
print(striphtml(results))