from bs4 import BeautifulSoup
import requests
import csv


urlstr=input("enter url:")

source=requests.get(urlstr)
soup=BeautifulSoup(source.text,'lxml')

with open('webcsv_scrap.csv','w') as f1:
    writer=csv.writer(f1,delimiter=',',lineterminator='\n',)
    for listed in soup.find_all('li'):
        cards=listed.find('md-card')
        if cards !=None:
            headdiv=cards.find('div')
            if headdiv !=None :
                names=headdiv.h4.a.text
                i=0
                for divisor in headdiv.find_all('div'):
                    if i==0 :
                        metadata1=divisor.text
                        i=i+1
                    if i==1:
                        organisation=divisor.text
                print(names,metadata1,organisation)
                writer.writerow([names,organisation,metadata1])
