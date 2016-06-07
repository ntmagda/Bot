from selenium import webdriver
import os


def make_connection(page):
    chromedriver = r"C:\Users\ntmagda\Anaconda2\Scripts\chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(page)
    return driver
