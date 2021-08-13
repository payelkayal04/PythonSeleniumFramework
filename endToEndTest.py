"""

"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

#//div[@class='card h-100']/div/h4
#products=//div[@class='card h-100'
#for add to card button = //div[@class='card h-100']/div[2]/button
for product in products:
    ProductName = product.find_element_by_xpath("div/h4/a").text
    if ProductName == "Blackberry":
        #Add item into card
        product.find_element_by_xpath("div[2]/button").click()
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_css_selector("#country").send_keys("Ind")
wait = WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
success_msg = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
print(success_msg)
assert "Success!" in success_msg
#take screenshot
driver.get_screenshot_as_file("screen.png")