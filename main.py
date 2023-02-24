from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import random
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:\ChromeDriver\chromedriver_win32\chromedriver")
driver.get("https://www.ratatype.com/typing-test/test/")


elem = driver.find_element("id","startButton")
elem.click()

in_elem = driver.find_element(By.CLASS_NAME,"mainTxt")
actions = ActionChains(driver)

def press_key(key):
    actions.send_keys(key)
    actions.perform()
    time.sleep(random.uniform(0.02, 0.06))
    
for i in in_elem.text:
    press_key(i)


for x in range(600000):
  print(x)