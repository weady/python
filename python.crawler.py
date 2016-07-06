# -*- coding utf-8 -*-
import os
import re
import time
import random
import requests
import hashlib
import threading
import urllib.request
from bs4 import BeautifulSoup


class GetPic:
    def __init__(self):
        self.url_dow = []                       
        self.url_list = []                      
        self.count = 0
        self.pic_dow = []                       
        self.pic_list = []                      
        self.pic_txt = "pigurl.txt"
        self.path_name = "图片"
        self.ip_list = []
        self.page_num = 1
        self.start = False
        self.quit = False
        self.proxy_urls = 'http://www.xicidaili.com/wn/'
        self.root = "http://www.chunmm.com"
        self.lock_list = threading.Lock()
        self.lock_dow = threading.Lock()
        self.lock_num = threading.Lock()
        self.lock_ip = threading.Lock()
        self.lock_pic = threading.Lock()
        self.lock_work = threading.Lock()
        self.headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
                   "Accept-Encoding": "gzip",
                   "Accept-Language": "zh-CN,zh;q=0.8",
                   "Referer": "http://www.chunmm.com/",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
                   }
        self.create_path()

    def create_path(self):                                               # create path
        if not os.path.exists(self.path_name):
            print("mkdir", self.path_name)
            os.mkdir(self.path_name)
        os.chdir(self.path_name)
        if not os.path.exists(self.pic_txt):
            file = open(self.pic_txt, "w")
            file.close()

    def get_url_data(self, url, index):                                        
        try:
            print('- - ' * 5, url)
            response = requests.get(url, timeout=20)
            if response.status_code != 200:
                print("get_url_data: error", url)
                return ""
            return response
        except:
           print('get_data error', url)
           return ""

    def move_url(self, root, index):                                     
        time.sleep(0.2)
        self.lock_list.acquire()
        try:
            self.url_list.remove(root)
        except:
            print("remove error",  index)
        self.lock_list.release()

    def add_url(self, root, index):                                      
        time.sleep(0.2)
        self.lock_list.acquire()
        try:
            self.url_list.append(root)
            self.url_list = set(self.url_list)
            self.url_list = list(self.url_list)
        except:
            print("add_url error", index)
        self.lock_list.release()

    def get_pic(self, pic_url):                                   
        pic_url.replace('min', 'max')
        self.lock_num.acquire()
        try:
            response = urllib.request.urlopen(pic_url, timeout=30).read()
            pic_name = str(self.count) + '.jpg'
            print("open file: ", pic_name)
            f = open(pic_name, 'wb')
            f.write(response)
            f.close()
            self.count += 1
            time.sleep(1)
        except:
            print("get pic error")
        self.lock_num.release()

    def get_children_url(self, root, index):                                 
        pic_url = []
        print('pic_len: ', len(self.pic_list), '  ...............  url_len: ', len(self.url_list) )
        time.sleep(0.1)
        response = self.get_url_data(root, index)
        if response == "":
            self.add_url(root, index)                                        
            return -1
        soup = BeautifulSoup(response.text, "html.parser")
        for a_url in soup.select('a[href^=/]'):
            ch_url = a_url["href"]
            ch_url = 'http://www.chunmm.com' + ch_url
            if (ch_url in self.url_dow) or (ch_url in self.url_list):
                pass
            else:
                self.add_url(ch_url, index)                           
        urls = soup.select('img[src$="max.jpg"]')

        if len(urls) == 0:
            return 0
        for img in urls:
            pic_url.append(img["src"])
        if len(pic_url) > 0:
            self.lock_pic.acquire()                                         
            file = open(self.pic_txt, "a")
            for pic_root in pic_url:
                # print("Í¼Æ¬ ", ": ", pic_root)
                if (pic_root not in self.pic_dow) and (pic_root not in self.pic_list):
                    print(pic_root)
                    self.pic_list.append(pic_root)
                    file.write(str(pic_root)+'\n')  
            file.close()
            self.lock_pic.release()

    def work(self, index):
        # print("work runing ", index)
        while not self.quit:
            self.lock_list.acquire()
            if len(self.url_list) > 0:
                root = self.url_list.pop(0)
                self.url_dow.append(root)                              
            else:
                root = "None"
            self.lock_list.release()
            if root != "None":
                self.get_children_url(root, index)
            else:
                time.sleep(2)

    def pic_work(self, index):
        # print("pic_work", index)
        time.sleep(index * 2)
        while not self.quit:
            self.lock_pic.acquire()
            if len(self.pic_list) > 0:
                pic = self.pic_list.pop(0)
                self.url_dow.append(pic)
            else:
                pic = "None"
            self.lock_pic.release()
            if pic != "None":
                self.get_pic(pic)
            else:
                time.sleep(2)

    def start_work(self):
        work_threads = []
        pic_threads = []
        self.url_list.append(self.root)
        for index in range(0,1000):
            th = threading.Thread(target=self.work, args=(index,))
            work_threads.append(th)
        for th in work_threads:
            th.start()

        for index in range(0,1000):
            th = threading.Thread(target=self.pic_work, args=(index,))
            pic_threads.append(th)
        for th in pic_threads:
            th.start()

        for th in work_threads:
            threading.Thread.join(th)
        for th in pic_threads:
            threading.Thread.join(th)

if __name__ == "__main__":
    os.system('color 02')
    print(" "*20, "美图爬虫")
    print("work start ...")
    time.sleep(3)
    Test = GetPic()
    Test.start_work()
