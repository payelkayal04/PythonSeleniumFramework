import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action = ActionChains(driver)
#At the end you have to give perform method then only chain operation will perfomed
menu = driver.find_element_by_id("mousehover")
action.move_to_element(menu).perform()
#time.sleep(4)
#childMenu = driver.find_element_by_link_text("Top")
childMenu = driver.find_element_by_link_text("Reload")
action.move_to_element(childMenu).click().perform()

