import pandas as pd
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from time import sleep
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

df = pd.read_csv("criptohito2.csv")
columna = ["email","password"]
x =df[columna]
for i in range(20):
  driver.get("https://www.educarchile.cl/user/login")
  #EMAIL
  driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div[6]/form/div[1]/input").send_keys(x.email[i])
  sleep(5)
  driver.save_screenshot("hito2/"+str(i)+'-email.png')
  #PASSWORD
  driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div[6]/form/div[2]/input").send_keys(x.password[i])
  sleep(5)
  driver.save_screenshot("hito2/"+str(i)+'-password.png')
  #INTENTAR LOGGEAR
  driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div[6]/form/div[4]/input").click()
  sleep(5)
  driver.save_screenshot("hito2/"+str(i)+'-clickLogin.png')
  sleep(5)
