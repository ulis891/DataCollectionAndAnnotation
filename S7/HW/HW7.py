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

mails_count_all = int(driver.find_element(By.XPATH, '//a[@class="nav__item js-shortcut nav__item_active '
                                                    'nav__item_shortcut nav__item_child-level_0"]').get_attribute(
                                                    'title').split(" ")[1])
all_mails = set()
actions = ActionChains(driver)
print()

while len(all_mails) < mails_count_all:
    mails = driver.find_elements(By.XPATH, '//div[@class="ReactVirtualized__Grid__innerScrollContainer"]/a')
    time.sleep(0.5)
    for mail in mails:
        try:
            all_mails.add(mail.get_attribute('href'))
        except Exception:
            print(mail)
            print()
            continue

    lust_mail = mails[-1].get_attribute('data-id')
    print(len(all_mails))
    driver.execute_script(f'document.querySelector("[data-id=\'{lust_mail}\']").scrollIntoView(false)')

    print()

for link in all_mails:
    driver.get(link)
    print()
    info_from = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'letter-contact')))
    info_from = info_from[0].get_attribute('title')
    # info_from = driver.find_element(By.CLASS_NAME, 'letter-contact').get_attribute('title')
    print(info_from)
    print()



