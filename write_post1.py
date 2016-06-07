
def write_post():
    driver.find_element_by_tag_name("textarea").click()
    driver.find_element_by_tag_name("textarea").send_keys("cokolwiek")
    time.sleep(5)
    driver.find_element_by_xpath("//button[contains(@data-testid,'react-composer-post-button')]").click()