from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json

url = 'https://www.dnd-spells.com/spells'

driver = webdriver.Chrome()
driver.get(url)

spell_list = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/div[2]/table/tbody').find_elements(By.TAG_NAME, 'tr')

spells_urls = []

for spell_row in spell_list:
    spell_url = spell_row.find_element(By.TAG_NAME, 'a').get_attribute('href')
    spells_urls.append(spell_url)

spells_details = []

for spell_url in spells_urls:
    driver.get(spell_url)

    name = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/h1/span').text
    type = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/p[1]').text
    level = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/p[2]/strong[1]').text
    casting_time = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/p[2]/strong[2]').text
    range = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/p[2]/strong[3]').text
    components = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/p[2]/strong[4]').text
    duration = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/p[2]/strong[5]').text
    description = (driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/p[4]').text).replace('\n', '<br>')
    at_higher_level = ''
    source = ''

    has_extra_paragraph = False

    try:
        driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/h4[1]/span')

        has_extra_paragraph = True
    except NoSuchElementException:
        has_extra_paragraph = False

    classes_html = []

    if has_extra_paragraph:
        at_higher_level = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/p[5]').text
        source = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/p[6]').text
        classes_html = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/p[7]').find_elements(By.TAG_NAME, 'a')
    else:
        source = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/p[5]').text,
        classes_html = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/p[6]').find_elements(By.TAG_NAME, 'a')

    if not isinstance(source, str):
        source = source[0]

    classes = []

    for current_class in classes_html:
        classes.append(current_class.text)

    spell_data = {
    'name': name,
    'type': type,
    'level': level,
    'casting_time': casting_time,
    'range': range,
    'components': components,
    'duration': duration,
    'description': description,
    'at_higher_level': at_higher_level,
    'source': source,
    'classes': classes
    }

    spells_details.append(spell_data)

driver.quit()
    
with open('spells.json', 'w') as json_file:
    json.dump(spells_details, json_file)
