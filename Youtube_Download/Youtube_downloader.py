from selenium import webdriver
from time import sleep
import time
from random import randint
import requests
from pytube import Youtube

# open browser
driver = webdriver.Firefox()

# youtube channel url
url = "channel_url"

#get youtube video
def get_video_youtube(driver,url):
    driver.get(url)
    time.sleep(randint(5,9))
    driver.get(url+"/videos")
    
    ht = driver.execute_script("return document.documentElement.scrollHeight;")
    while True :
        prev_ht = driver.execute_script("return document.documentElement.scrollHeight;")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight;")
        time.sleep(2)
        ht = driver.execute_script("return document.documentElement.scrollHeight;")
        if prev_ht == ht :
            break
    links = driver.find_element_by_xpath('//*[@id="video-title"]')
    with open('f:\\somefile.txt', 'w') as the_file:
        for link in links:
            print(link.get_attribute("title"))
            print(link.get_attribute("href"))
            yt = Youtube(link.get_attribute("href"))
            hd = yt.streams.get_highest_resolution()
            hd.download("f:\\youtube\\")
            the_file.writelines(link.get_attribute("href")+'\n')
            sleep(3)


get_video_youtube(driver,url)




