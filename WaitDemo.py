#Implicit wait
#Explicit Wait
#Pause the test for few seconds using time class
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

ValidateText = "Option3"
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#driver.implicitly_wait(5)
# wait untill 5 seconds if object is not displayed
#Global wait
#1.5 second to reach next page - execution will resume in 1.5 seconds

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_css_selector("a.cart-icon").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input.promocode")))
driver.find_element_by_css_selector("input.promocode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))

print(driver.find_element_by_css_selector("span.promoInfo").text)
