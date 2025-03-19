# open google.com
#  search campusx
# learnwith.campusx.in
# dsmp course page

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# s = Service("C:/Users/Engineer/OneDrive/Desktop/chromedriver.exe")
s = Service("C:/Users/Engineer/OneDrive/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get("https://www.google.com")
# time.sleep(2)

# fetch the search input box using xpath
user_input =driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea')
user_input.send_keys('Campusx')
time.sleep(3)

user_input.send_keys(Keys.ENTER)
time.sleep(20)

link = driver.find_element(by=By.XPATH, value="//a[@class='zReHs' and contains(@href, 'https://learnwith.campusx.in/')]")
link.click()
time.sleep(3)

# login click

link2 = driver.find_element(by=By.XPATH , value= "/html/body/div[1]/header/section[2]/a[8]")
link2.click()
time.sleep(3)

input("Press Enter to close the browser...")
driver.quit()




