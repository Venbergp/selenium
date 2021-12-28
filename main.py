from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.avito.ru/'

driver = webdriver.Chrome(executable_path='/Users/artem/PycharmProjects/pythonProject/upravlenie_kachestvom/selenium/chromedriver/chromedriver')

# ТК-1 проверка ввода на сайте

try:
    driver.get(url=url)
    time.sleep(5)
    data_input = driver.find_element_by_tag_name('input')
    data = 'Ararara'
    data_input.send_keys(data + Keys.ENTER)
    driver.save_screenshot("tk1.png")
    time.sleep(5)
    print('Sucsess! ТК-01')
except Exception as Ex:
    print(Ex)

# ТК-2 проверка работоспособности выбора города
try:
    driver.get(url=url)
    choose = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/a[2]')
    choose.click()
    driver.save_screenshot("tk2.png")
    print('Sucsess! ТК-02')
    time.sleep(5)
except Exception as Ex:
    print(Ex)

# ТК-3 проверка выбора недвижимости

try:
    choose = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/a[2]')
    choose.click()
    driver.save_screenshot("tk3.png")
    print('Sucsess! ТК-03')
    time.sleep(5)
except Exception as Ex:
    print(Ex)

# ТК-4 Проверка перехода к анкетам только с фото

try:
    choose = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[4]/div/label[2]/span')
    choose.click()
    driver.save_screenshot("tk4.png")
    print('Sucsess! ТК-04')
    time.sleep(5)
except Exception as Ex:
    print(Ex)

# ТК-5 Проверка перехода к трансопрту

try:
    choose = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div[1]/div[2]/a')
    choose.click()
    driver.save_screenshot("tk5.png")
    print('Sucsess! ТК-05')
    time.sleep(5)
except Exception as Ex:
    print(Ex)

# ТК-6 Проверка входа

try:
    choose = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[1]/div[2]/a')
    choose.click()
    driver.save_screenshot("tk6.png")
    print('Sucsess! ТК-06')
    time.sleep(5)
except Exception as Ex:
    print(Ex)
