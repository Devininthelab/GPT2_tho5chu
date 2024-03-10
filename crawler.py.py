from selenium import webdriver
from selenium.webdriver.common.by import By
url = 'https://www.google.com/'

driver = webdriver.Chrome()

driver.get(url)
img_url = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[2]/div/img'
).get_attribute('src')

print(img_url)