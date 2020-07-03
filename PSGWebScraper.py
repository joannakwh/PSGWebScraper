import key
import requests
import pandas as pd
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
    # print(result.text)
    tree = html.fromstring(result.content)
    return tree

def getYears():
    tree = makeRequest(None, None, None)
    years = tree.xpath('//select[@name="selectYear"]/option/text()')
    # remove 'Select Year' option
    years.pop(0)
    return years

def getMakes(year):
    tree = makeRequest(str(year), None, None)
    makes = tree.xpath('//select[@name="selectMake"]/option/text()')
    makes.pop(0)
    return makes

def getModels(year, make):
    tree = makeRequest(str(year), str(make), None)
    models = tree.xpath('//select[@name="selectModel"]/option/text()')
    models.pop(0)
    return models

def getInfo(year, make, model):
    info = {}
    tree = makeRequest(str(year), str(make), str(model))
    # bpmet = tree.xpath('//input[@name="BPMET"]/@value')
    # bpstd = tree.xpath('//input[@name="BPSTD"]/@value')
    # hub = tree.xpath('//input[@name="HUB"]/@value')
    # lug = tree.xpath('//input[@name="LUG"]/@value')
    # lugtype = tree.xpath('//input[@name="LUGTYPE"]/@value')
    # offset = tree.xpath('//input[@name="OFFSET"]/@value')
    # offsetmm = tree.xpath('//input[@name="OFFSETMM"]/@value')
    # info.append({ 'BPMET' : bpmet, 'BPSTD' : bpstd, 'HUB' : hub, 'LUG' : lug, 'LUGTYPE': lugtype, 'OFFSET': offset, 'OFFSETMM': offsetmm})
    fields = tree.xpath('//input/@name')
    for field in fields:
        values = tree.xpath('//input[@name="' + field + '"]/@value')
        for value in values: 
            info[field] = value
    print(info)
    return info

# df = pd.DataFrame()    
# years = getYears()
# for year in years:
#     makes = getMakes(year)
#     for make in makes:
#         models = getModels(year, make)
#         for model in models: 
#             infos = getInfo(year, make, model)
#             data = pd.DataFrame(infos)
#             print(data)
#             time.sleep(3)
            
df = pd.DataFrame()
info = getInfo(2020, 'ACURA', 'ILX')
data = pd.DataFrame(rows,)
print(df)

