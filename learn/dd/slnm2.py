from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

try:
    browser = webdriver.Chrome("chromedriver.exe")
except:
    print("Error!")

browser.get("https://www.linkedin.com/")
browser.maximize_window()

login = browser.find_element_by_xpath("/html/body/nav/a[3]")
login.click()
time.sleep(3)

email = browser.find_element_by_xpath('//*[@id="username"]')
email.send_keys("***")
time.sleep(1)
password = browser.find_element_by_xpath('//*[@id="password"]')
password.send_keys("***")
time.sleep(1)

login_button = browser.find_element_by_css_selector(
    "#app__container > main > div:nth-child(2) > form > div.login__form_action_container > button")
login_button.click()
time.sleep(5)

search_bar = browser.find_element_by_xpath('//*[@id="ember16"]/input')
search_bar.send_keys("#python")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

contacts = browser.find_element_by_xpath('//*[@id="ember23"]/span')
contacts.click()
time.sleep(5)

contact_button = browser.find_element_by_class_name(
    'mn-community-summary__entity-info')
contact_button.click()
time.sleep(5)

for i in range(1, 3):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)

followers = browser.find_elements_by_class_name("mn-connection-card__details")
followerList = list()
for follower in followers:
    followerList.append(follower.text)

with open("li.txt", "w", encoding="utf-8") as file:
    for flw in followerList:
        file.write(flw + "\n")
time.sleep(5)

# time.sleep(32)
# browser.quit()
