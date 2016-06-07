import time

def go_to_profil(driver):
    driver.find_element_by_xpath("//a[@title='Profil']").click()
    time.sleep(3)

def count_friends(driver):
    friends = driver.find_element_by_xpath("//*[@data-tab-key='friends']").text
    friendsCount = friends[7:]
    return friendsCount


def write_post(driver, text):
    driver.find_element_by_tag_name("textarea").click()
    driver.find_element_by_tag_name("textarea").send_keys(text)
    time.sleep(5)
    driver.find_element_by_xpath("//button[contains(.,'Opublikuj')]").click()
    time.sleep(5)