from selenium import webdriver

driver = webdriver.Edge(executable_path="C:\\Users\\a875026\\Downloads\\edgedriver_win64\\msedgedriver.exe")

# Go to the site
driver.get("https://academybugs.com")

# Click on the x on the tutorial pop up
driver.find_element("xpath", "//*[@id='TourTip0']/button").click()

# Click on the Find Bugs button
driver.find_element("xpath", "//*[@id='menu-item-561']").click()

# Click on the button 50 on the pagination section
driver.find_element("xpath", "//*[@id='ec_product_page']/div[1]/span[1]/a[3]").click()
