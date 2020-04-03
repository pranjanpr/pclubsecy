# pclubsecy
have a scrapper and a identifier python file
-------------------problem statement--------------------
Write a program to take a URL as an input. You should assume the the URL will lead to a page that has this layout: https://summerofcode.withgoogle.com/archive/2019/projects/
Your program should scrape this page and extract the name, organization and projects for all the people selected. It should then print the output to a CSV file the following format:
Name1, Organisation1, Project1
Name2, Organisation2, Project2
Name3, Organisation3, Project3
...

Write another program that takes a CSV file and a JSON file as input. The CSV file has the same format as above. This program should first find names that do not look like official names and print them. The rules for checking non-official names are:
1) The name contains any of the special symbols or numbers.
2) The name consists of only one word.
30 The name contains only lowercase letters.
The remaining names (that are official names) should be matched against the JSON file that we provide. You should print (to stdout) the details of all the names that are present both in the JSON file and in the CSV file, in the following format:
Name(common to both JSON and CSV), Roll No(from JSON), Branch(from JSON), Organisation(from CSV), Project(from CSV)


----------------------directions to use-------------------------------
for first one there is the scrapper program which takes input of the url and output a csv file naming webcsvscrap.csv
note that the website must be of the same form as provided


for the identifier file 
to give the input a csv and a json run the identifier as idle and pass the names of csv and json file to their respective places along
with their directories with respect to identifier file
i have uploaded test json and csv files to check them
after adding file name run it(f5)

******there is some bug in url 
******for webscrapper
 the given url opens on  page 1 by default though it has 12 pages in it
 each page have its own url so this program will only give a csv file for page 1
 for other pages you can input their urls to get their csv files
 ******also note that when url:https://summerofcode.withgoogle.com/archive/2019/projects/?page=4 is entered in program 1 (webscra.py) then it will make a csv file containing the name of Avik Pal but when we run the program 2(identify.py) by taking that csv file as input it does not show the name of Avik pal(he is from iitk ) the reason being that in students.json file his name is written with 2 spaces instead of one. 
