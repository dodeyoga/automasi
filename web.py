from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def web_start():
    driver = webdriver.Firefox(executable_path=r'E:\automasi\geckodriver.exe')
    keywords = "START.TSM"
    driver.get("url")
    driver.maximize_window()
    time.sleep(5)

    driver.find_element_by_link_text("Execute servlet").click()
    time.sleep(3)
    search_box = driver.find_element_by_name("command")
    search_box.send_keys(keywords)
    search_box = driver.find_element_by_id("submit").click()
    time.sleep(3)
    
#web_start()