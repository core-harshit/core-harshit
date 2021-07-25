import argparse 
import requests
from bs4 import BeautifulSoup
import csv
def file_read(o):
    with  open(o, "r") as fok:
        l = fok.readlines()
        return l
n = argparse.ArgumentParser()
n.add_argument('namefile',help="filename required")
args = n.parse_args()
print(args)
try:
    o = args.namefile
    p = file_read(o)
    for c in p:
        print(c.rstrip())
    def web_status():
        m = []
        csvlist = []
        for x in p:
            url = x.rstrip()
            r = requests.get(url)
            print(r)
            m.append(r)
            print(r.headers)
            soup = BeautifulSoup(r.text, 'html.parser')
            print("Title of the website is : ")
            for title in soup.find_all('title'):
                Title = title.get_text()
                print(Title)
                m.append(Title)
            csvlist.append(m)
            m = []
        return csvlist
    e = web_status()
    with open("response.csv", "w") as f:
        x = csv.writer(f)
        x.writerows(e)
except FileNotFoundError:
    print("FILE NOT EXIST,PLS ENTER CORRECT FILE NAME")
