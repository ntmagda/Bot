import os
from selenium import webdriver
import time


def login(driver, username, password):
    UN = driver.find_element_by_id('email')
    UN.send_keys(username)

    PS = driver.find_element_by_id('pass')
    PS.send_keys(password)

    LI = driver.find_element_by_id('loginbutton')
    LI.click()

    time.sleep(3)