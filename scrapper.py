#/usr/bin/python
# -*- coding: utf-8 -*-


"""
This modolue generates list of publically avaiable proxy servers.

It uses free api given by gimmeproxy.com

Since the api has a rate limit so dont exceed for more than 30 ip's at a single time

Requirements : requests library

How to use : python scrapper.py count filename


"""

import requests
import sys
import time

class proxylist:

    def __init__(self,count,filename):
        self.count = count
        self.filename=filename;

    def store_ip_port(self):

        base_url = "https://gimmeproxy.com/api/getProxy"
        F = open(self.filename + ".txt", "w")
        ip_list = []

        for i in range(self.count):

            try:
                time.sleep(5)
                page= requests.get(base_url)
                response = page.json()
                ip_port=response['ip']+":"+response['port']

                print(ip_port)

                if(ip_port not in ip_list):
                    ip_list.append(response['ip'] + ":" + response['port'])
                    F.write(ip_port+"\n")
            except:
                print("error")

        F.close()


obj1 = proxylist(100,"proxylist_3")
obj1.store_ip_port();


if __name__ == "__main__":
    obj1 = proxylist(sys.argv[1],sys.argv[2])
    obj1.store_ip_port()