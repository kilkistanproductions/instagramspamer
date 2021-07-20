import random
import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui

# setting up driver

driver = webdriver.Firefox(executable_path="/home/hgetis/Projects/Python/geckodriver")
driver.get('https://www.instagram.com/')

# log in
time.sleep(5)
button = driver.find_element_by_xpath("/html/body/div[3]/div/div/button[1]")
button.send_keys(Keys.ENTER)
time.sleep(5)

# take elements
username = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
password = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
submit = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")

# send keys
username.send_keys("6907788326")
password.send_keys("#T6!8eq63oy5TfkE")
submit.send_keys(Keys.ENTER)
time.sleep(10)

# go to the comment page
driver.get("https://www.instagram.com/p/CRguYXXMZub/")


# send comment
def spam():
    wait = random.randint(35, 120)
    time.sleep(wait)
    comment_area = driver.find_element_by_class_name('Ypffh')
    comment_area.click()
    time.sleep(5)
    comment_area = driver.find_element_by_class_name('Ypffh')
    comment_area.click()
    comment_area.send_keys("@_basilhsnastoulas")
    comment_area.send_keys(Keys.ENTER)


while True:
    spam()
