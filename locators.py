from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://en-gb.facebook.com/campaign/landing.php?&campaign_id=973072061&extra_1=s%7Cc%7C231346502318%7Ce%7Cfacebook%7C&placement&creative=231346502318&keyword=facebook&partner_id=googlesem&extra_2=campaignid%3D973072061%26adgroupid%3D54006406691%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-297690534863%26loc_physical_ms%3D9303390%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMIoa6X2YXs8AIVyFBgCh36wgZ6EAAYASAAEgIwc_D_BwE")
driver.find_element_by_name("firstname").send_keys("Payel")
driver.find_element_by_name("lastname").send_keys("Roy")
driver.find_element_by_name("reg_email__").send_keys("8892385927")
driver.find_element_by_name("reg_passwd__").send_keys("Roy@1234")
driver.find_element_by_id("u_0_4_5x._8esa").click()
