# # Importing traceback to catch xml button not found errors in the future
# import traceback
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
# import time
# import datetime
# import os
# import argparse
# import platform
import os
from urllib import request
from urllib.request import urlopen
import datetime
import requests
from bs4 import BeautifulSoup
import pdfkit
import certifi
import urllib3
from urllib3.exceptions import InsecureRequestWarning
import validators


try:
    import autoit
except ModuleNotFoundError:
    pass

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)

import config as cfg
url = cfg.drivers_config["URL"]
#url = ""




def convertToPdf():
    pdfkit.from_url(url,str(url.split(".")[1])+'_html2PdfFIle.pdf',verbose=True)
    pdfkit.from_string('Shaurya GFG','randomText2PdfFile.pdf')
    pdfkit.from_url(['google.com', 'geeksforgeeks.org', 'https://www.snapdeal.com/'], 'multipleHtml2PdfFile.pdf')
    pdfkit.from_file(['file1.html', 'file2.html'], 'multiHtmlfile2pdfFile.pdf')



#rr = ""
def getUrlStatus(urlLink):
    reqs = requests.get(urlLink, verify=False)  # verify=None
    return str(reqs.status_code)


uselessLinks = ['None','#']

def getAllLinks(soup):
    links = []
    for link in soup.findAll('a') :
        link1 = str(link.get('href'))
        if link1 not in uselessLinks:
            links.append(link1)
    for link in soup.findAll('link'):
        link1 = str(link.get('href'))
        if link1 not in uselessLinks:
            links.append(link1)
    links = "\n".join(links)
    writeToTxtFile("aLinks.csv", str(links))
    print("hello testing Vijay in getAllLinks() completed")

# Js file links extraction started
def getJsLinks(soup):
    links = []
    for link in soup.findAll('script'):
        link1 = str(link.get('src'))
        try:
            if link1 not in uselessLinks:
                links.append(link1)
        except Exception as e:
            print("Error seen in Jss file creation : ",e)
    links = "\n".join(links)
    writeToTxtFile("javaScript.csv", str(links))
    print("hello testing Vijay in getJsLinks() completed")


#Css file links extraction started
def getCssLinks(soup):
    links = []
    for link in soup.findAll('link'):
        try:
            links.append(str(link.get('href')))
        except Exception as e:
            print("Error seen in CSS file creation : ",e)
    links = "\n".join(links)
    writeToTxtFile("Css.csv", str(links))
    print("hello testing Vijay in getCssLinks() completed")

#Image file links extraction started
def getImageLinks(soup):
    links = []
    for link in soup.findAll('img'):
        link1 = str(link.get('src'))
        link2 = str(link.get('data-src'))
        try:
            if link1 not in uselessLinks:
                links.append(link1)
            if link2 not in uselessLinks:
                links.append(link2)
        except Exception as e:
            print("Error seen in Image file creation : ",e)
    links = "\n".join(links)
    writeToTxtFile("Images.csv", str(links))
    print("hello testing Vijay in getImageLinks() completed")

def getBadLinks(soup):
    print("to implement the functionality")
    pass


def getTextFromPage(soupData):
    txtData = ""
    # getting all the paragraphs
    for para in soupData.find_all("p"):
        # print(para.get_text())
        txtData = txtData + "\n" + para.get_text()

    for txt in soupData.find_all('div'):
        textData = textData + "\n" + soupData.find

    writeToTxtFile("TextDataOfWebPage.txt", txtData)
    print("hello testing Vijay in getTextFromPage() completed")


def getCurrentTime():
    return str(datetime.datetime.now())

# Pass
def writeToTxtFile(fileName, data):
    with open(fr'C:\Users\{os.getlogin()}\Desktop\{fileName}', 'w') as f:
    # if not os.path.exists('outputData'):
    #     os.makedirs('outputData')
    # print(os.getcwd())
    # if not "outputData" in os.getcwd():
    #     os.chdir('outputData')
    # with open(fileName, "w") as f:
    #     info = "File creation started at : " + getCurrentTime() +" \n\n"
    #     f.write(info)
        f.write(data)
        # info = "\n\n File creation ended at : " + getCurrentTime()
        # f.write(info)
    msg = "C:\\Users\\"+ os.getlogin() + "\\Desktop\\" + fileName
    print(msg)
    return msg

def readFile(fileName):
    if not "outputData" in os.getcwd():
        os.chdir('outputData')
    with open(fileName, "r") as f:
        data = f.readlines()
        return data


#Get http status of all links :: Pass
def httpStatusOfAllLinks(urls):
    status = ""
    statusData = []
    for urlLink in urls:
        print(urlLink)
        valid = validators.url(urlLink)
        if valid == True:
            status = getUrlStatus(urlLink)
            statusData.append(str(urlLink + "," + str(status))+"\n")
            print("url :" + urlLink + "," + str(status))
        else:
            print("Check the URL ",urlLink)
            statusData.append(str(urlLink + ", Check the Url"))
    statusData = '\n'.join(statusData)
    writeToTxtFile("urlStatus.csv", statusData)


urltmp = "https://www.google.com"


def setUrl(newUrl):
    global urltmp
    urltmp = newUrl

def getUrl():
    return urltmp

soupData1 = ""

#Get all links on the page
def getSoupData():
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url = getUrl()
    reqs = requests.get(url, verify=False,headers=header)   # verify=None
    soupData = BeautifulSoup(reqs.text,  'html.parser')
    return soupData





def getAllLinksInSoup():
    soupData1 = getSoupData()
    getAllLinks(soupData1)



def getJsLinksInSoup():
    soupData1 = getSoupData()
    getJsLinks(soupData1)


def getCssLinksInSoup():
    soupData1 = getSoupData()
    getCssLinks(soupData1)


def getImageLinksInSoup():
    soupData1 = getSoupData()
    getImageLinks(soupData1)

def getBadLinksInSoup():
    soupData1 = getSoupData()
    getBadLinks(soupData1)

8
def getAllLinkStatus():
    print(os.getcwd())
    with open("aLinks.csv") as f:
        url_lst = f.read().split()
        writeToTxtFile("urlsToList_WIP.csv", str(url_lst))
        print(url_lst)
        httpStatusOfAllLinks(url_lst)

def getDuplicateLinks():
    print("Implement the functionality")
    pass


def getPageText():
    soupData1 = getSoupData()
    getTextFromPage(soupData1)
    pass


# httpStatusOfAllLinks(allUrls)


#get analytics of links and their corresponding status
    #Get duplicate count of URL's on a page
    #

