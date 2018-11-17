import csv
import re
import requests
from bs4 import BeautifulSoup
from urllib.request import urljoin

url = 'http://www.mizzimaburmese.com/'
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
lis = soup.findAll('div', class_='group group-1')
for li in lis:
    l = li.find('div', class_='news-info')
    span1 = l.find('span', class_='news-date')
    date = span1.find('span', class_='date-display-single')
    print("Date ====>", date.text, "news are")

    li1 = li.findAll('div', class_='news-title')
    for link in li1:
        title = link.find('a').text
        suburl = link.find('a').get('href')
        suburl = urljoin(url, suburl)
        suprequest = requests.get(suburl)
        soup = BeautifulSoup(suprequest.text, "html.parser")
        author = soup.find('div', {'class': 'news-details-author-by'})
        author = author.text
        print("Title ===>", title, "=====>", suburl, "Author ", author)
        paragraph = soup.find('div', {'class': 'field-item even'})

        for p in paragraph.findChildren():
            if p.name == 'div':
                p.clear()

        with open('F:\mizzimasavecsv\mizzima.csv', mode='a', encoding='utf-8') as mizzimadata:
            mizzimadatabase = csv.writer(mizzimadata, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            mizzimadatabase.writerow([str(title), str(suburl), str(author), paragraph.text])
            print("Saving successful ", title)



