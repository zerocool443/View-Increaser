#/usr/bin/python
# -*- coding: utf-8 -*-


"""
This module sends request to a given url from various proxies to avoid blocking of  requests originating from same ip.

How to use : Modify the code  and give your url .
            python sbooster.py

Requirements :
    pip install requests
    pip install requests[socks]
"""
import requests

proxies = {
    'http' : 'socks5://0.0.0.0:8080',
}

url = "https://alchemyofnotions.wordpress.com/2017/05/27/the-crises-of-identities"



ips = list(open("proxylist_1.txt",'r'));

for ip in ips:
    try:
        proxies['http']=ip[0:-1] # Can also use: proxies['http']="socks5://"+str(ip[0:-1])
        print(proxies)
        response = requests.get(url, proxies=proxies);
        print(response)
    except:
        print("error")


ips = list(open("proxylist_2.txt",'r'));

for ip in ips:
    try:
        proxies['http']=ip[0:-1]  # Can also use: proxies['http']="socks5://"+str(ip[0:-1])
        print(proxies)
        response = requests.get(url, proxies=proxies);
        print(response)
    except:
        print("error")

