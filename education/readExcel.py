import openpyxl
from bs4 import BeautifulSoup
import urllib.request


wb = openpyxl.Workbook()

wb = openpyxl.load_workbook('C:\\Users\\codef\\Documents\\temp\\ceshi.xlsx')
sh = wb['Sheet1']
for i in range(1,3):
    ce = sh.cell(row = i,column = 1)
    url ="http://dict.youdao.com/search?q=" + ce.value
    request = urllib.request.Request(url)
    soup = BeautifulSoup(urllib.request.urlopen(url=request),features='html.parser')
    yinbiao = soup.select(".phonetic")[0].text
    sh.cell(row = i,column = 2).value = yinbiao
    yinbiao = soup.select(".phonetic")[1].text
    sh.cell(row = i,column = 3).value = yinbiao
    # print( soup.title)
    yinbiao = soup.select(".trans-container")[0].text
    sh.cell(row = i,column = 4).value = yinbiao

wb.save('C:\\Users\\codef\\Documents\\temp\\ceshi2.xlsx')
wb.close()