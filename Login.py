from selenium import webdriver
from getpass import getpass

user = "sani2315" #input('Enter your username or email id: ')
passwd = "ishuilu231535" #getpass('Enter your password : ')

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')

username = driver.find_element_by_id('email')
username.send_keys(user)

password = driver.find_element_by_id('pass')
password.send_keys(passwd)

login = driver.find_element_by_id('u_0_a')
login.submit()
