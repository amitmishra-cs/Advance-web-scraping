import time

from  selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service("C:/Users/Engineer/OneDrive/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service = s)

driver.get('https://www.smartprix.com/mobiles')
time.sleep(1)

driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()

time.sleep(2)

old_height = driver.execute_script('return document.body.scrollHeight')
while True:

    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(1)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source

with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)

input("Press Enter to close the browser...")
driver.quit()



# driver.get("https://www.smartprix.com/mobiles")
# time.sleep(2)
#
# driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
# time.sleep(2)
# driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
# driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[3]/div[3]').click()
# time.sleep(2)
# driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[3]/div[3]').click()



