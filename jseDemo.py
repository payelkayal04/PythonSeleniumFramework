"""
JS DOM can access any elements on web page just liske how selenium does
Selenium have a method to execute Javascript code is None:
"""
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_name("name").send_keys("Hello")
#Error: if you enter some input from selenium script and you are trying to grab
#text what you enter that not possible using text method.
#print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))   #javacript


#use Javascript in your selenium:
#when selenium not able to click the operation in various reason then we can use it

shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click()",shopButton)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")