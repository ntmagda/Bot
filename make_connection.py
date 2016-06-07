from selenium import webdriver
import os

def make_connection(page, username, password):
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.folderList', 2)
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    profile.set_preference('browser.download.dir', os.getcwd())
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv/xls')
    driver = webdriver.Firefox(profile)
    driver.get(page)
    return driver
