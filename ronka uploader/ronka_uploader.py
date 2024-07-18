from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import os
import time

print(
    """
    A RONKA'S GREAT SERPENT IS APPEAR!!!
⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠊⠉⠉⠉⠓⠲⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡰⠋⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⡶⣠⠏⣦⠀⢀⣄⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⢣⣄⣠⠇⠈⠉⠀⠀⠀⠀⠀⠀⣰⣿⢦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣇⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠃⢸⠘ ⡷⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡿⡀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠔⠋⠀⠀⡸⠀⡇ ⢹⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠈⠑⠒⠒⠒⠒⠋⠉⠀⠀⠀⠀⠀⢠⠃⠀⡇ ⢸⢳⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠃⠀⡸⠀⢸   ⢸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀⠀⢀⡠⠔⠊⠀⢀⠜⠁⠀⡏  ⡜⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⡓⠤⠤⠤⠤⠒⠊⠉⠀⠀⢀⡴⠋⠀⢀⡜ ⡰⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢤⣀⣀⣀⣀⣀⣀⠤⠒⠉⠀⢀⣠ ⠾⠊⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠭⠤⠤⠤⠤⠤⠴⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀
    """
)

race = {
    '남가딘':1, '남고휴':2, '남라펠':3, '남레젠':4, '남우라':5, '남중휴':6, '남코테':7, '남로스갈':8,
    '여가딘':9, '여고휴':10, '여라펠':11, '여비에라':12, '여레젠':13, '여우라':14, '여중휴':15, '여코테':16,
    '남비에라':17, '여로스갈': 18
}

try:
    driver = wb.Chrome()
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)
    driver.get('https://ronkacloset.com/admin')
    driver.implicitly_wait(60)

    id_input = driver.find_element(By.CSS_SELECTOR, 'div.input_form>input[type=text]')
    pw_input = driver.find_element(By.CSS_SELECTOR, 'div.input_form>input[type=password]')
    login_btn = driver.find_element(By.CSS_SELECTOR, '#cocoaModal > div > div > article > form > p > button')
    id_input.send_keys('upload_savior')
    pw_input.send_keys('Sa54910gr-')
    login_btn.send_keys(Keys.ENTER)
    time.sleep(5)

    item_list = os.listdir('./ronka')
    path = os.getcwd().replace('\\', '/')
    success_list = []
    fail_list = []

    for i in item_list:
        driver.get('https://ronkacloset.com/admin/shopping/product')
        driver.implicitly_wait(10)
        img_list = os.listdir(f'./ronka/{i}')

        search = driver.find_element(By.CSS_SELECTOR, '#keyword_search_input')
        search.send_keys(i)
        search.send_keys(Keys.ENTER)
        driver.implicitly_wait(10)
        search_list = driver.find_elements(By.CSS_SELECTOR, 'div.item-tit.inline-blocked > a:nth-child(1)')

        if len(search_list) != 1:
            fail_list.append(f'{i}: 전체')
            break
        search_list[0].click()
        driver.implicitly_wait(10)
        
        table = driver.find_elements(By.CSS_SELECTOR, 'table.noBorder')[1]
        tds = table.find_elements(By.CSS_SELECTOR, 'td')
        for td in tds:
            if td.text == '':
                continue
            idx = race.get(td.text)
            name = td.text
            if idx == None:
                fail_list.append(f'{i}: {name}')
                continue
            img_input = driver.find_elements(By.CSS_SELECTOR, 'input[type=file]')[3]
            if not os.path.isfile(f'{path}/ronka/{i}/{idx}.jpg'):
                continue
            td.clear()
            td.click()
            img_input.send_keys(f'{path}/ronka/{i}/{idx}.jpg')
            if f'{idx}.jpg' in img_list:
                img_list.remove(f'{idx}.jpg')

            success_list.append(f'{i}: {name}')
            time.sleep(1.5)
            td.send_keys(Keys.ENTER)
            td.send_keys(name)

        driver.find_element(By.CSS_SELECTOR, '#header > div > div.headerbar-right > ul > li:nth-child(2) > a').click()
        fail_list += [f'{i}: {img}' for img in img_list]
        time.sleep(5)
    driver.quit()
    
except Exception as e:
    with open(f"./error log {time.strftime('%Y%m%d %H%M%S')}.txt", 'w') as f:
        f.write(e+'\n')

finally:
    with open(f"./log {time.strftime('%Y%m%d %H%M%S')}.txt", 'w') as f:
        f.write(time.strftime('%Y/%m/%d %H:%M:%S')+'\n')
        f.write('////SUCCESS LIST'+'\n')
        for i in success_list:
            f.write(i+'\n')
        f.write('////FAIL LIST'+'\n')
        for i in fail_list:
            f.write(i+'\n')