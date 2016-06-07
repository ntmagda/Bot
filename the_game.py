# -*- coding: utf-8 -*-
import time

def go_to_profil(driver):
    driver.find_element_by_xpath("//a[@title='Profil']").click()
    time.sleep(3)

def count_friends(driver):
    friends = driver.find_element_by_xpath("//*[@data-tab-key='friends']").text
    friendsCount = friends[7:]
    return friendsCount


def write_post(driver, text):
    text_encoded = text.encode('utf-8')
    driver.find_element_by_tag_name("textarea").click()
    time.sleep(2)
    driver.find_element_by_tag_name("textarea").send_keys("costamfajnego")
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(.,'Opublikuj')]").click()
    time.sleep(2)

def go_to_friends_list(driver):
    driver.find_element_by_xpath("//a[@data-tab-key='friends']").click()
    time.sleep(10)


def scroll_to_element(driver, element):
    driver.executeScript("return arguments[0].scrollIntoView();", element)

def scroll1(driver):
    fh = 0.1
    while fh < 9.9:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % fh)
        # driver.find_element_by_xpath("//a[@class='UFILikeLink _4x9- _4x9_ _48-k']").click()
        fh += 0.01




def click_friend(driver, friend_name):
    scroll1(driver)
    friend_name_encoded = friend_name.encode('utf-8')
    try:
        driver.find_element_by_xpath('//a[@href="https://www.facebook.com/'+friend_name_encoded+'?fref=pb&hc_location=friends_tab"]').click()
        time.sleep(3)
    except:
        print("Cannot find friend")

def add_all_friends(driver):
    names = driver.find_elements_by_xpath("//div[@class='fsl fwb fcb']")
    print ("total no of friends   ", len(names))
    for name in names:
        name_str = name.find_element_by_tag_name("a").text
        # try:
        name_encoded = name_str.encode('utf-8')
        str = "//button[@aria-label='Dodaj użytkownika "+name_encoded+" do znajomych']"
        print(str)
        try:
            driver.find_element_by_xpath(str).click()
            time.sleep(5)
        except:
            print("Cannot add %s" % name_str)


def click_all_likes(driver):
    scroll1(driver)
    likes = driver.find_elements_by_xpath("//a[contains(.,'Lubię to!')]")
    print ("posts to like   ", len(likes))
    for like in likes:
        try:
            like.click()
            time.sleep(1)
        except:
            print("cannot like that")
