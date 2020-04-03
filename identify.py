import json
import csv
import re


#enter .json file name below in the place of students.json with the directories involved if any
myjsonfile=open('students.json','r')
jsondata=myjsonfile.read()


obj=json.loads(jsondata)
list=obj






def run1(string):
    regex=re.compile('[@_!#$%^&*()<>?/\|}{~:0123456789]')
    if (regex.search(string)==None):
        return 1
    else:
        return 0
    
def run2(string):
    regex=re.compile('[ ]')
    if (regex.search(string)==None):
        return 0
    else:
        return 1

def run3(string):
    regex=re.compile('[ABCDEFGHIJKLMNOPQRSTUVWXYZ]')
    if (regex.search(string)==None):
        return 0
    else:
        return 1
def fake(string):
    z=run1(string)
    x=run2(string)
    c=run3(string)
    sum=z+x+c
    if sum==3:
        return 1
    else :
        return 0
        


#enter .csv file name below in the place of large.csv with directories involved if any
with open('large.csv','r',encoding="latin-1") as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for line in csv_reader:
        #print(line[0],'\n')
        i=fake(line[0])
        #print(i)
        if i==1 :
            for j in range(len(list)):
                if(list[j].get("n"))==line[0]:
                    print (line[0],',',list[j].get("i"),',',list[j].get("d"),',',line[1],',',line[2])
                    break
                else:
                    continue
                
                
            
            


    





#for i in range(len(list)):
    #print(list[i].get("n"))
