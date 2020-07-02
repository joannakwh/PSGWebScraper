import key
import requests
import pandas
import json
from pandas import Series, DataFrame
from lxml import html

def makeRequest(year, make, model):
    url = 'http://www.plussizingguide.com/cgi-bin/ultimate_guide_online.cgi'
    params = {'host': 'HTTP_HOST', 'userName': 'cariboo',
              'password': key.password, 'licenseKey': key.licenseKey}
    if (year is not None and len(year) != 0):
        params.update({'selectYear': year})
    if (year is not None and len(year) != 0):
        params.update({'selectMake': make})
    if (year is not None and len(year) != 0):
        params.update({'selectModel': model})
    result = requests.post(url, data=params)
    tree = html.fromstring(result.content)
    return tree

def getYears():
    tree = makeRequest(None, None, None)
    years = tree.xpath('//select[@name="selectYear"]/option/text()')
    # remove 'Select Year' option
    years.pop(0)
    return years

# print(makeRequest(year, make, model))
print(getYears())
