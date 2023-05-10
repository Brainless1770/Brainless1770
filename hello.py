from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time



driver = webdriver.Chrome("E:\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.get("https://orteil.dashnet.org/cookieclicker/")


driver.implicitly_wait(5)

langEng = driver.find_element(By.ID,"langSelect-EN") 
langEng.click()


cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice0" + str(i)) for i in range(1,-1,-1)]




actions = ActionChains(driver)
actions.click(cookie)


for i in range(5000):
    actions.click(cookie)
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
   