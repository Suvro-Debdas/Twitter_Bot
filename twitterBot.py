from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Defining a function to fetch the login credentials.

def account_info():
    with open('account_info.txt','r') as f:
        info=f.read().split()
        email=info[0]
        password=info[1]
    return email,password

email,password=account_info()

# Taking input of the message to be tweeted.

tweet=str(input("Enter the message here:\n"))

# Assigning the chrome driver.

driver=webdriver.Chrome("F:\\Twitter\\chromedriver_win32\\chromedriver")

# Assigning the website login url.

driver.get("https://twitter.com/i/flow/login")

# 

driver.find_element_by_name("text").send_keys(email)
time.sleep(5)
next_xpath='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]/div'
driver.find_element_by_xpath(next_xpath).click()
time.sleep(5)
driver.find_element_by_name("password").send_keys(password)
time.sleep(5)
login_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span'
driver.find_element_by_xpath(login_xpath).click()



















































# email_xpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]'
# time.sleep(15)
# driver.find_element_by_xpath(email_xpath).send.keys(email)
# time.sleep(15)
# next_xpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
# time.sleep(15)
# driver.find_element_by_xpath(next_xpath).click()
# time.sleep(15)
# password_xpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
# time.sleep(15)
# driver.find_element_by_xpath(password_xpath).send.keys(password)
# time.sleep(15)
# login_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span'
# time.sleep(15)
# driver.find_element_by_xpath(login_xpath).click()
