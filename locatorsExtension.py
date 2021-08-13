from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=in")
driver.maximize_window()

driver.find_element_by_css_selector('#username').send_keys("Payel")
driver.find_element_by_css_selector('.password').send_keys('000000')

#driver.find_element_by_css_selector('.password').clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
#//tagname[text()='xxx']
#   driver.find_element_by_link_text("Cancel").click()
driver.find_element_by_xpath("//a[text()='Cancel']").click()

#//div[@id='usernamegroup']/label ----xpath(traverse from parent to child)
#//form[@name='login']/div[1]/label ----Xpath(traverse from grand parent to grand child)
#//div[@id='usernamegroup'] label ----CSS(traverse from parent to child)

#form[name='login'] label:nth-child(4)  ----CSS locator
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(4)").text)





