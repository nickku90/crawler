from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages=set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj,includeUrl):
    internalLinks=[]
    for link in bsObj.findAll("a",href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in internalLinks:
                internalLinks.append(link.attrs["href"])
    return internalLinks

def getExternalLinks(bsObj,excludeUrl):
    externalLinks=[]
    for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in externalLinks:
                externalLinks.append(link.attrs["href"])
    return externalLinks

def splitAddress(address):
    addressParts=address.replace("http://","").split("/")
    return addressParts


allExtLinks=set()
allIntLinks=set()
def getAllExternalLinks(siteUrl):
    html=urlopen(siteUrl)
    bsObj=BeautifulSoup(html)
    internalLinks=getInternalLinks(bsObj,splitAddress(siteUrl)[0])
    externalLinks=getExternalLinks(bsObj,splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("About to get link: "+link)
            allIntLinks.add(link)
            getAllExternalLinks(link)
    getAllExternalLinks("http://oreilly.com")


siteUrl="https://www.ntu.edu.tw/"
getAllExternalLinks(siteUrl)

