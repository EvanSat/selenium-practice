from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
s = Service(PATH)
browser = webdriver.Chrome(service=s)

url = "https://www.google.com"
browser.get(url)
print(browser.title)

search = browser.find_element(By.NAME, 'q')  # Finds Search Box
search.send_keys("test imput")
search.send_keys(Keys.RETURN)
# browser.close()     # closes tab |.quit() will close whole browser
