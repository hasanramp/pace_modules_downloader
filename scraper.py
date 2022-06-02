from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import requests as req
import base64
import re
from download_pdf_from_links import download_pdf
import os
from PIL import Image
import json
from sys import platform
from alive_progress import alive_bar

def get_chapter_data():

    code = input('Enter chapter code:')
    subject = code[0]
    chapter = int(code[1:])
    print(chapter)
    if subject == 'P':
        file = 'physics_code.json'
    elif subject == 'M':
        file = 'maths_code.json'
    elif subject == 'C':
        file = 'chem_code.json'
    else:
        print('Invalid code. Exiting...')
        exit(1)
    file = open(file, 'r').read()
    code_json = json.loads(file)
    index = 1
    # indexes through keys, on reaching the index of subject, returns subject, code, and number of pages
    for sub in code_json:
        if chapter == index:
            print(sub)
            return sub, code_json[sub]
        index += 1
    



def save_pdf(dir_, pages):
    print('saving pdf....')
    img_list = []
    im1 = Image.open(f'{dir_}/page0.jpg').convert('RGB')

    # parses images one by one and appends to img_list list
    with alive_bar(pages, title="parsing images...") as bar:
        for x in range(1, pages):
            xstr = str(x)
            img = Image.open(f'{dir_}/page{xstr}.jpg').convert('RGB')
            img_list.append(img)
            bar()

    # saves all images as one pdf file
    im1.save(f'{dir_}.pdf', save_all=True, append_images=img_list)

    # moves pdf to modules folder
    try:
        os.rename(f'{dir_}.pdf', f'modules/{dir_}.pdf')
    except FileNotFoundError:
        os.mkdir('modules')


# I don't know how the fuck this shit works. Copied from stackoverflow. It works so I ain't touching it
def decode_base64(data, altchars=b'+/'):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    print('decoding image data...')
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'='* (4 - missing_padding)
    return base64.b64decode(data, altchars)

def save_in_temp(link):
    with open('temp', 'a') as f:
        f.write(link + '\n')
    return

def login():
    print('logging in...')
    # email_input = driver.find_element_by_id('edit-name-1')
    email_input = driver.find_element(By.ID, 'edit-name-1')
    email_input.send_keys('rampurawalahasan4@gmail.com')

    # password_input = driver.find_element_by_id('edit-pass-1')
    password_input = driver.find_element(By.ID, 'edit-pass-1')
    password_input.send_keys('Istudyinpace1!')

    # login_button = driver.find_element_by_id('edit-submit-1')
    login_button = driver.find_element(By.ID, 'edit-submit-1')
    login_button.click()

option = webdriver.ChromeOptions()


# to use brave instead of chrome just make a file named usebrave in this directory
if os.path.isfile('usebrave'):
    option.binary_location = '/usr/bin/brave'


# gets absolute path to chromedriver
chromedriver_executable_path = os.path.join(os.getcwd(), 'chromedriver')    

driver = webdriver.Chrome(executable_path=chromedriver_executable_path, chrome_options=option, service_log_path=os.devnull)
driver.get("https://online.digitalpace.in")

# login to digitalpace
login()

time.sleep(2)

# subjects_link = driver.find_element_by_xpath('//*[@id="mysubs-menu"]/a')
subjects_link = driver.find_element(By.XPATH, '//*[@id="mysubs-menu"]/a')
subjects_link.click()

# subjects = driver.find_elements_by_class_name('course_title')
subjects = driver.find_elements(By.CLASS_NAME, 'course_title')
subjects[7].click()

input('enter: ')
time.sleep(5)

# try:
#     login()
# except NoSuchElementException:
#     pass


# chapter, code_and_npages = get_chapter_data()
# code = code_and_npages[0]
# print(code)
# n_pages = code_and_npages[1]

chapter = input('chapter: ')
n_pages = int(input("number of pages: "))

code = ''
code_found = False

try:
    os.mkdir(chapter)
except FileExistsError:
    pass

page_links: list = []
page_no = 1
refreshed = False
break_while = False
n=1

while not break_while:
    print('entering while loop')
    index = 0
    with alive_bar(n_pages, title="Getting links") as bar:
        for x in range(1, n_pages + 2):
            xstr = str(x)
            if page_no >= n_pages + 1:
                break_while = True
                break
            for t in driver.execute_script('return window.performance.getEntries()'):
                link = t['name']
                if page_no == 1:
                    if link.find('https://videos.online.digitalpace.in') != -1 and not code_found:
                        link_parts = link.split('/')
                        code = link_parts[4][0:16]
                        print(code)
                        code_found = True
                        driver.execute_script('window.PlayerManager.seekVideo(1)')
                if code_found:
                    if page_no > n*59 and not refreshed:
                        n+=1
                        refreshed = True
                        driver.execute_script('location.reload()')
                        time.sleep(4)
                        driver.execute_script('window.PlayerManager.seekVideo(60)')
                    if link.find(code + str(page_no)) != -1:
                        save_in_temp(link)
                        page_links.append(link)
                        if page_no == n_pages +1:
                            break
                            print('downloading all images...')
                        page_no += 1
                        break
                index += 1
            driver.execute_script(f'window.PlayerManager.seekVideo({xstr})')
            time.sleep(3)
            bar()
        #find_element(by=By.XPATH, value=xpath)
        

download_pdf(page_links, chapter)
save_pdf(chapter, n_pages)
exit()