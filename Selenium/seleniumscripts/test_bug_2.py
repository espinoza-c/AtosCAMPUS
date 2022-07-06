from selenium import webdriver
from pyautogui import write

driver = webdriver.Edge(executable_path="C:\\Users\\a875026\\Downloads\\edgedriver_win64\\msedgedriver.exe")

# Go to the site
driver.get("https://academybugs.com")

# Click on the x on the tutorial pop up
driver.find_element("xpath", "//*[@id='TourTip0']/button").click()

# Click on the Find Bugs button
driver.find_element("xpath", "//*[@id='menu-item-561']").click()

# Click on the DNK Yellow shoes
driver.find_element("xpath", "//*[@id='ec_product_image_effect_dnk-yellow-shoes']/a").click()

# Click on the CURRENCY button
driver.find_element("xpath", "//*[@id='currency']").click()

# Select EUR value, these are keyboard controls
write(['down'])
write(['enter'])