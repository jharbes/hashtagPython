from selenium import webdriver
from selenium.webdriver.common.by import By


options=webdriver.ChromeOptions()

# chrome://version
options.add_argument(r'user-data-dir=C:\Users\Jorge\AppData\Local\Google\Chrome\User Data\Profile Selenium')


navegador=webdriver.Chrome(options=options)

navegador.get('https://web.whatsapp.com')

import os, time







time.sleep(10)