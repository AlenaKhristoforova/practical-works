from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/Users/User/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru/")
driver.set_window_size(1600,800)
driver.find_element(By.NAME, "username").clear()
driver.find_element(By.NAME, "username").send_keys("demo")
driver.find_element(By.NAME, "password").clear()
driver.find_element(By.NAME, "password").send_keys("demo")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "otp-code").clear()
driver.find_element(By.ID, "otp-code").send_keys("0000")
driver.find_element(By.ID, "login-otp-button").click()
driver.find_element(By.ID, "payments-form").click()
driver.find_element(By.XPATH, "//*[@id='dashboard-payment-type-menu']/li[5]/a").click()
driver.find_element(By.ID, "filter").click()
driver.find_element(By.ID, "filter").send_keys("мтс")
time.sleep(5)
print("PASS")

