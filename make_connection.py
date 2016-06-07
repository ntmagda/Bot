from selenium import webdriver
import os


def make_connection(page):
    chromedriver = r"C:\Users\ntmagda\Anaconda2\Scripts\chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(page)
    return driver

def make_firefox_connection(page):
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.folderList', 2)
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    profile.set_preference('browser.download.dir', os.getcwd())
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv/xls')
    driver = webdriver.Firefox(profile)
    driver.get(page)
    return driver
