import json
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains




options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
driver.get("https://e.mail.ru")
actions = ActionChains(driver)

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
#   сохраняем колличество писем
mails_count_all = int(driver.find_element(By.XPATH, '//a[@class="nav__item js-shortcut nav__item_active '
                                                    'nav__item_shortcut nav__item_child-level_0"]').get_attribute(
                                                    'title').split(" ")[1])
#   создаём множество писем для избежания дубликатов
all_mails = set()

#   ищем все письма
while len(all_mails) < mails_count_all:
    mails = driver.find_elements(By.XPATH, '//div[@class="ReactVirtualized__Grid__innerScrollContainer"]/a')
    time.sleep(0.5)
    #   добавляем ссылки на письма в множество
    for mail in mails:
        #   иногда не находит ссылки, поэтому избегпаем ошибки
        try:
            all_mails.add(mail.get_attribute('href'))
        except Exception:
            continue
    #   берём последнее ннайденое письмо для прокрутки страницы до него
    lust_mail = mails[-1].get_attribute('data-id')
    #   лог по колличеству обработанных писем
    print(f'Обработанно {len(all_mails)} из {mails_count_all}')
    # прокрутка страницы до последнего найденного письма
    driver.execute_script(f'document.querySelector("[data-id=\'{lust_mail}\']").scrollIntoView(false)')

#   создаём список с письмами
letters = []
#   обрабатываем все письма
for link in all_mails:
    driver.get(link)
    info_from = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'letter-contact')))
    info_from = info_from[0].get_attribute('title')
    info_title = driver.find_element(By.XPATH, '//h2').text
    info_date = driver.find_element(By.CLASS_NAME, 'letter__date').text
    info_body = driver.find_elements(By.CLASS_NAME, 'letter-body')[0].text
    #   добавляем информацию в словарь
    letters.append({'from': info_from,
                    'date': info_date,
                    'title': info_title,
                    'body': info_body})


with open(os.getcwd() + "/news.json", "w", encoding="utf-8") as f:
    json.dump(letters, f, ensure_ascii=False)


