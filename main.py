
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
def text_with_newlines(elem):
     text = 'Lath \n'
     for e in elem.descendants:
         if isinstance(e, str):
             text += e.strip()
         elif e.name == 'br' or e.name == 'p':
             text += '\n'
     return text
file = open('MyNovel.txt', 'w', encoding= 'utf-8')
for i in range(1,3):                   # Page ranges
    slug = "mai-mai-la-bao-xa"          # Name of the novel
    url = "https://wattpad.vn/"+slug+"/chuong-"+str(i)+"/"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    htmlbyte = urlopen(req).read()
    html = htmlbyte.decode('utf-8')
    soup = BeautifulSoup(html, features="html.parser")
    fulltext = text_with_newlines(soup)
    header = 'Chương ' + str(i)
    footer = '(adsbygoogle = window.adsbygoogle || []).push({});arfAsync.push("l5t09e16")'
    chap = fulltext[fulltext.find(header)-20:fulltext.find(footer)]
    print("Chapter "+str(i)+" done")
    file.writelines(chap)
file.close()