import os
from selenium import webdriver
from make_connection import make_connection
import time
import write_post1

page = "http://www.facebook.com"
username = "graznowsop@gmail.com"
password = "graznowsop123"

driver = None
while driver is None:
    try:
        # connect
        driver = make_connection(page, username, password)
        time.sleep(5)
    except:
        print("cannot connect")
        pass

UN = driver.find_element_by_id('email')
UN.send_keys(username)

PS = driver.find_element_by_id('pass')
PS.send_keys(password)

LI = driver.find_element_by_id('loginbutton')
LI.click()

time.sleep(3)
# click profile
driver.find_element_by_xpath("//a[@title='Profil']").click()
time.sleep(3)

frineds = driver.find_element_by_xpath("//*[@data-tab-key='friends']").text
# count = Integer.parseInt(frinedsCount)
friendsCount = frineds[7:]
print("Liczba znajomych: ", friendsCount)
# click friends list
driver.find_element_by_xpath("//a[@data-tab-key='friends']").click()


#
# write_post()
# time.sleep(5)
# driver.close()