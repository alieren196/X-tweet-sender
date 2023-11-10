from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
with open("tweet.txt", "r") as f:
    tweet = f.read()
driver = webdriver.Chrome()
driver.get("https://twitter.com/i/flow/login")
username_field = driver.find_element_by_name("session[username_or_email]")
password_field = driver.find_element_by_name("session[password]")
username_field.send_keys("Kullanıcı adı")
password_field.send_keys("Şifre")
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
time.sleep(5)
tweet_box = driver.find_element_by_xpath("//div[@class='public-DraftEditor-content']")
tweet_box.send_keys(tweet)
tweet_button = driver.find_element_by_xpath("//button[@type='submit']")
tweet_button.click()
time.sleep(5)
driver.close()