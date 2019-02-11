 #criptbnq
 #coding: utf-8

import json 
import csv 
import requests
#import selenium

fichier = "banque.csv"

for i in range(1000, 2001):
    l=[]
    l.append(i)

a = "http://collections.banq.qc.ca/api/service-notice?handle=52327/"

for elem in l:
    b = l(elem)

url = a + b


entete = {
    "User Agent":"Theo Sardaigne - 438 927 4031",
    "From":"sardaigne.theo@courrieluqam.ca"
}

req = requests.get(url,headers=entete)

if req.status_code != 200:
    print("ca marche pas")

else:
    chansons = req.json()

for chanson in chansons:
    if type != "audio":
        {

        }

else:
    if "titre" in chanson:
        print(chanson["titre"])
    if "createurs" in chanson:
        #print(chanson["createurs"][0])
    if "dateCreation" in chanson:
        #print(chanson["dateCreation"])
    if "descriptionMat" in chanson:
        #print(chanson["descriptionMat"])
    if "liens" in chanson:
        #print(chanson["liens"]["url"][0])

for chanson in chansons:
    l = []

if "titre" in chanson:
    l.append(chanson["titre"])
if "createurs" in chanson:
    l.append(chanson["createurs"][0])
if "dateCreation" in chanson:
    l.append(chanson["dateCreation"])
if "descriptionMat" in chanson:
    l.append(chanson["descriptionMat"])
if "liens" in chanson:
    l.append(chanson["liens"]["url"][0])
    #print(l)
    #print("~"*80)

lebron = open(fichier,"a")
james = csv.writer(lebron)
james.writerow(l)
