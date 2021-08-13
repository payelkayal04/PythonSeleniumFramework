from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element_by_css_selector("input[name='name']").send_keys("Payel Kayal")
driver.find_element_by_css_selector("input[name='email']").send_keys("payelkayal.04@gmail.com")
driver.find_element_by_css_selector("input[id='exampleInputPassword1']").send_keys("000000")
driver.find_element_by_id("exampleCheck1").click()
#select class provide the methods to handle the options in dropdowm
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()

driver.find_element_by_xpath("//input[@type='submit']").click()
#
# print(driver.find_element_by_class_name("alert-success").text)
#//*[contains(@class,'alert-success')] -Xpath
#[class*='alert-success]               -CSS

message = driver.find_element_by_class_name("alert-success").text

assert "success" in message




