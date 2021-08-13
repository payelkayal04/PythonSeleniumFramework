"""
1. Validate whether products selected in page 1 are showing in page 2 check page
2. Verify if price decreases on discount
3. Verify sum products in checkout page mathches with total amount

Assignment:
verify is serach functionlity in home page is working
Search ber
3 Products : x,y,z
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

list = []
list2 = []
ValidateText = "Option3"
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

#//div[@class='product-action']/button/parent::div/parent::div/h4    #traverse from down to up(NAvigate back
#from child to parent
for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list)


driver.find_element_by_css_selector("a.cart-icon").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input.promocode")))

veggies = driver.find_elements_by_css_selector("p.product-name")
for veg in veggies:
    list2.append(veg.text)
print(list2)

assert list == list2

Total_Amt = driver.find_element_by_css_selector("span.totAmt").text

driver.find_element_by_css_selector("input.promocode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))

Discount_Amt = driver.find_element_by_css_selector("span.discountAmt").text
assert float(Discount_Amt) < int(Total_Amt)

print(driver.find_element_by_css_selector("span.promoInfo").text)


amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)
print(sum)

assert sum == int(Total_Amt)