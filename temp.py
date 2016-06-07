# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import re
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='email']").send_keys("XXXXX@gmail.com")
driver.find_element_by_xpath("//*[@id='pass']").send_keys("XXXXX")
driver.find_element_by_xpath("//*[@id='u_0_n']").click()
driver.find_element_by_xpath("//*[@id='checkpointSubmitButton']").click()
driver.find_element_by_xpath("//*[@id='profile_pic_welcome_1155995189']").click()
driver.find_element_by_xpath("//a[@data-medley-id='pagelet_timeline_medley_friends']").click()


#### scrolling the page till it gets refreshed
flag=True
uls_beforeScroll =len(driver.find_elements_by_xpath("//div[@id='pagelet_timeline_app_collection_1155995189:2356318349:2']/ul"))

while(flag):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(4)
    uls_afterScroll = len(driver.find_elements_by_xpath("//div[contains(@id,'pagelet_timeline_app_collection_')]/ul"))
    if(uls_afterScroll == uls_beforeScroll):
        flag = False
    else:
        uls_beforeScroll = uls_afterScroll

name=""
no=0

##printing names of friends
names = driver.find_elements_by_xpath("//div[@class='fsl fwb fcb']")
print "total no of friends   ",len(names)
for name in names:
       print name.find_element_by_tag_name("a").text