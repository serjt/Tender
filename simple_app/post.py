# coding=utf-8
import requests
from bs4 import BeautifulSoup


def find_data(fio, d, m, y):
    response = requests.post(url='http://www.ssm.gov.kg/blacklist/',
                             data=dict(fio=fio, d=d, m=m, y=y))
    soup = BeautifulSoup(response.content, "lxml")
    strong = soup.find_all('strong')
    str1 = str(strong[0])
    return str1[8:-9]
