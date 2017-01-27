# coding=utf-8
import requests
from bs4 import BeautifulSoup
import json

from django.http import HttpResponse


def find_data(fio, d, m, y):
    response = requests.post(url='http://www.ssm.gov.kg/blacklist/',
                             data=dict(fio=fio, d=d, m=m, y=y))
    soup = BeautifulSoup(response.content, "lxml")
    strong = soup.find_all('strong')
    str1 = str(strong[0])
    str2 = str1[8:-9]
    if str2 == 'Указанная фамилия в «Чёрном списке» не найдена!':
        return str2
    else:
        c = []
        for a in soup.find_all('a', href=True):
            url = a['href']
            if url[0:11] == '/blacklist/':
                res = requests.get(url='http://www.ssm.gov.kg' + url)
                soup1 = BeautifulSoup(res.content, "lxml")
                p = soup1.find_all('p')
                p1 = str(p[0])
                context = {
                    'name': a.text,
                    'nakaz': p1[3:-4]
                }
                c.append(context)
        return c
#
# fio = "Кенешов Мирлан Абдыразакович"
# d = "19"
# m = "10"
# y = "1984"
# response = requests.post(url='http://www.ssm.gov.kg/blacklist/',
#                          data=dict(fio=fio, d=d, m=m, y=y))
# soup = BeautifulSoup(response.content, "lxml")
# strong = soup.find_all('strong')
# str1 = str(strong[0])
# str2 = str1[8:-9]
# if str2 == 'Указанная фамилия в «Чёрном списке» не найдена!':
#     print str2
# else:
#     c = []
#     for a in soup.find_all('a', href=True):
#         url = a['href']
#         if url[0:11] == '/blacklist/':
#             res = requests.get(url='http://www.ssm.gov.kg' + url)
#             soup1 = BeautifulSoup(res.content, "lxml")
#             p = soup1.find_all('p')
#             p1 = str(p[0])
#             context = {
#                 'name': a.text,
#                 'nakaz': p1[3:-4]
#             }
#             c.append(context)
#     l = {
#         'object': c,
#     }
#     print str(json.dumps(l, separators=(',', ':')))
