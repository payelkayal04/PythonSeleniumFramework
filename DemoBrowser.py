from selenium import webdriver

#browser exposes an executable file
#through selenium test we need to invoke the executable file which will then invoke actual browser

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.maximize_window()

driver.get("https://www.facebook.com/photo?fbid=3640438252848929&set=a.1412010902358353")
#get method to hit url on browser

print(driver.title)
print(driver.current_url)
driver.get("https://mail.google.com/mail/u/0/#inbox")
driver.minimize_window()
driver.back()
driver.refresh()
#driver.close()