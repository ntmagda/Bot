import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import write_post

page = "http://www.facebook.com"
username = "graznowsop@gmail.com"
password = "graznowsop123"

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', os.getcwd())
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv/xls')
driver = webdriver.Firefox(profile)
driver.get(page)

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

