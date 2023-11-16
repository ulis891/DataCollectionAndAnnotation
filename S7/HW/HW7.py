from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time


options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
driver.get("https://e.mail.ru")


time.sleep(2)
#   находим строку ввода логина
input = driver.find_element(By.XPATH, "//input[@name='username']")
#   вводим логин
input.send_keys("study.ai_172@mail.ru")
input.send_keys(Keys.ENTER)
time.sleep(2)
#   находим строку ввода пароля
input = driver.find_element(By.XPATH, "//input[@name='password']")
#   вводим пароль
input.send_keys("NextPassword172#")
input.send_keys(Keys.ENTER)

#   ожидаем загрузки элемента с колличеством писем
wait = WebDriverWait(driver, 30)
cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="badge__text"]')))
mails_count = int(driver.find_element(By.XPATH, '//span[@class="badge__text"]').text)
all_mails = set()
print()
actions = ActionChains(driver)

while len(all_mails) < mails_count:
    mails = driver.find_elements(By.XPATH, '//div[@class="ReactVirtualized__Grid__innerScrollContainer"]/a')
    for mail in mails:
        all_mails.add(mail.get_attribute('href'))
    print(len(all_mails))
    driver.execute_script(
        'document.getElementsByClassName("ReactVirtualized__Grid__innerScrollContainer")[0].scrollIntoView(0,5)')

    print()



