#<-----------------------------------Completed give india------------------------------------------------------>
from bs4 import BeautifulSoup
import requests, json
from pprint import pprint

def give_india_list():
    list1,list2,list3,main_list,d=[],[],[],[],{}
    give_india="https://www.giveindia.org/certified-indian-ngos"
    res = requests.get(give_india)
    soup = BeautifulSoup(res.text,"html.parser")
    divs = soup.find("div",class_="d-flex f-d-col w-100 p-0 container")
    dd=divs.find("div",class_="nonprofit-card-container d-flex py-2 container")
    
    for i in divs:
        list1.append(i.find('h5',class_="nonprofit-name mb-0").get_text())
        v=(i.find('span').get_text().split('|')[:2])
        for j in v:
            if j == v[0]:
                list2.append(j)
                
            else:
                list3.append(j)
                
    for a,b,c in zip(list1,list2,list3):
        d["Name"]=a
        d["Cause"]=b
        d["Location"]=c
        main_list.append(d.copy())
    file=open("give-india.json","w")
    json.dump(main_list,file,indent=4)
    file.close()
    # return main_list
give_india_list()

#...................................................................................................................#