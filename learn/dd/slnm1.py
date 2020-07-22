from selenium import webdriver
import time

try:
    browser = webdriver.Chrome("chromedriver.exe")
except:
    print("Error!")

browser.get("https://www.forbes.com/powerful-brands/list/#tab:rank")
browser.maximize_window()
time.sleep(3)
browser.get(
    "https://www.forbes.com/companies/apple/?list=powerful-brands#2cc564585355")
time.sleep(3)
browser.back()
time.sleep(10)
browser.quit()
