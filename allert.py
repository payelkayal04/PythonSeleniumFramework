import time

from selenium import webdriver

ValidateText = "Option3"
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys("Option3")
driver.find_element_by_id("alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
alertText = alert.text
print(alert.text)
assert ValidateText in alertText
alert.accept()      #accept method select ok and then alert will automatically get closed
alert.dismiss()     #accept method select cancel and then alert will automatically get closed
