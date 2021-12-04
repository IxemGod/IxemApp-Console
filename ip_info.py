from couleur import *
from art import *
import os
import uuid
import requests
from bs4 import BeautifulSoup
import random
import webbrowser



  



def InfoIp():
    url ="https://mon-ip.io"
    IpPublique = "False"
    response = requests.get(url)
    if response.ok:
        links = []
        soup = BeautifulSoup(response.text)
        divs = soup.findAll('p')
        for div in divs:
            links.append(div)
        IpPublique = str(links[0])
        IpPublique = IpPublique[11:24]


    system("clear")
    print(Color.pink_bold)
    tprint("Info IP")

    #On récupère l'adresse mac
    AdresseMac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
    print(Color.blue_bold+"     [IP]"+Color.white_bold+" Adresse Mac : "+Color.red_bold+AdresseMac)

    print(Color.blue_bold+"     [IP]"+Color.white_bold+" Ip Publique : "+Color.red_bold+IpPublique)
    
    

    

    fin = input("")