import os
from selenium import webdriver
from make_connection import make_connection
import time
from the_game import write_post, go_to_profil, count_friends
from socket import error as socket_error

page = "http://www.facebook.com"
username = "graznowsop@gmail.com"
password = "graznowsop123"

driver = make_connection(page)
while driver is None:
    try:
        # connect
        driver = make_connection(page)
        time.sleep(5)
    except socket_error:
        print("cannot connect")
        time.sleep(50)
        pass

UN = driver.find_element_by_id('email')
UN.send_keys(username)

PS = driver.find_element_by_id('pass')
PS.send_keys(password)

LI = driver.find_element_by_id('loginbutton')
LI.click()

time.sleep(3)
# click profile

go_to_profil(driver)

print(count_friends(driver))


write_post(driver)