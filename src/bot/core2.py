#!/usr/bin/env python
# -*- coding: utf8 -*-
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

import helpers
#driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver')
#driver = webdriver.Firefox()
driver = webdriver.PhantomJS()
driver.get("https://medium.com/top-100/december-2013")
time.sleep(1)
elem = browser.find_element_by_tag_name("body")
no_of_pagedowns = 20
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1
print(driver.current_url)
driver.quit()

ACCESS_TOKEN = 'AbVZ6pBecrXC9afBG9mahRCxS8NuFM2MA50rraBEIg4xUYA_VwAAAAA'

class pinBot():
    def __init__(self):
        self.baseUrl = 'https://in.pinterest.com'
        self.apiUrl = 'https://api.pinterest.com/v1/'
        pass

    def search(self,keyword,searchType):
        ids = []
        if(searchType=='pin'):
            print(self.baseUrl + r'/search/pins/?q=' + keyword )
            data = urlopen(self.baseUrl + r'/search/pins/?q=' + keyword ).read()
            soup = BeautifulSoup(data,"html.parser")
            pins = soup.find_all("a", {'class':['pinLink','pinImageWrapper']})
            for pin in pins:
            	ids.append(re.search('\d+',pin.get('href')).group())
            return ids
        elif(searchType=='board'):
            data = urlopen(self.baseUrl + r'/search/boards/?q=' + keyword ).read()
            soup = BeautifulSoup(data,"html.parser")
            boards = soup.find_all("a", {'class':['boardLinkWrapper']})
            for board in boards:
            	ids.append(board.get('href'))
            return ids
        else:
            raise "something happened"

    def followUser(self,userId):
        params = [ 'access_token='+ACCESS_TOKEN, 'user='+userId]
        r = requests.post(self.apiUrl+'me/following/users/?'+'&'.join(params))
        print(r.status_code)

    def unfollowUser(self,userId):
        params = [ 'access_token='+ACCESS_TOKEN ]
        r = requests.post(self.apiUrl+'me/following/users/'+userId+'?'+'&'.join(params))
        print(r.status_code)

    def followBoard(self,boardId):
        params = [ 'access_token='+ACCESS_TOKEN, 'board='+boardId]
        r = requests.post(self.apiUrl+'me/following/boards/?'+'&'.join(params))
        print(r.status_code)

    def unfollowBoard(self,boardId):
        params = [ 'access_token='+ACCESS_TOKEN ]
        r = requests.post(self.apiUrl+'me/following/boards/'+boardId+'?'+'&'.join(params))
        print(r.status_code)

    def savePin(self,pinId):
        # save pin method is not implemented yet
        params = [ 'access_token='+ACCESS_TOKEN ]
        r = requests.patch(self.apiUrl+'me/following/users/'+userId+'?'+'&'.join(params))

    def createPost(self,imageUrl):
        pass



"""
Requirements:
    1. search a topic
    2. get 10 results
    3. follow those boards, save those pins(if pins), follow board creators
    4. if already followed, unfollow them and skip.
    repeat this 3 times in a day.
API endpoints provided :
1. fetch user data (not needed)
2. create user follow and board follow
	/v1/me/following/boards/ POST
	/v1/me/following/users/ POST
2. delete user follow and board follow
	/v1/me/following/boards/<board>/
	/v1/me/following/users/ POST
FOLLOW example
https://api.pinterest.com/v1/me/following/users/?access_token=AbVZ6pBecrXC9afBG9mahRCxS8NuFM2MA50rraBEIg4xUYA_VwAAAAA&user=rdturner31
https://api.pinterest.com/v1/me/following/boards/?access_token=AbVZ6pBecrXC9afBG9mahRCxS8NuFM2MA50rraBEIg4xUYA_VwAAAAA&board=janew/happy
UNFOLLOW
https://api.pinterest.com/v1/me/following/users/rdturner31?access_token=AbVZ6pBecrXC9afBG9mahRCxS8NuFM2MA50rraBEIg4xUYA_VwAAAAA

Search urls:
1. boards search: https://in.pinterest.com/search/boards/?q=happy
1. pin search: https://in.pinterest.com/search/pins/?q=cool
"""