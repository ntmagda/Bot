import os
from selenium import webdriver

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
#
# if driver.find_elements_by_partial_link_text(("home") ).exists():
#     print("Login succesful")