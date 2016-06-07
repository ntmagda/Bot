# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from make_connection import make_connection
from login import login
import time
from the_game import write_post, go_to_profil, count_friends, go_to_friends_list, click_friend, scroll, add_all_friends
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

login(driver, username, password)

go_to_profil(driver)
print(count_friends(driver))
write_post(driver, "costamfajnego")
go_to_friends_list(driver)
click_friend(driver, 'magda.nowaktrzos')
write_post(driver, "chyba_dziala")
go_to_friends_list(driver)
scroll(driver)
add_all_friends(driver)