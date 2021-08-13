from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

radio = driver.find_elements_by_xpath("//input[@name='radioButton']")
radio[2].click()
assert radio[2].is_selected()

#related web object should not be in html format
#print(driver.find_element_by_css_selector("#displayed-text").is_displayed())\
assert driver.find_element_by_css_selector("#displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
#print(driver.find_element_by_css_selector("#displayed-text").is_displayed())
assert not driver.find_element_by_css_selector("#displayed-text").is_displayed()