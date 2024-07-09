from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException
import pyperclip as pc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --profile-directory="Default" --remote-debugging-port=9222



options = Options()
options.add_experimental_option("debuggerAddress", "localhost:9222")

s = Service(r"C:\Users\underdog\PycharmProjects\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=s, options=options)
driver.get('https://chat.openai.com/c/80785153-9f26-44c5-8a12-8de6d57840a2')
time.sleep(5)

driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/main/div[2]/form/div/div[2]/textarea').send_keys('一分鐘介紹一個已解決懸疑事件')
button_sus = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/main/div[2]/form/div/div[2]/button')
button_sus.click()
time.sleep(30)

try:
    button_sus = button_sus
    answer_sus = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/main/div[1]/div/div/div/div[4]/div/div[2]/div[1]/div/div').text
    print(answer_sus)
    pc.copy(answer_sus)
except NoSuchElementException:
    print('再等15秒')
    time.sleep(15)
    answer_sus = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/main/div[1]/div/div/div/div[4]/div/div[2]/div[1]/div/div').text
    print(answer_sus)
    pc.copy(answer_sus)

#創建fliki檔案
def open_fliki_and_create_audio():
    driver.execute_script("window.open('https://www.google.com', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])
    fliki_url = 'https://fliki.ai/?via=13021191&gclid=Cj0KCQjwib2mBhDWARIsAPZUn_l0-bF8qCkYsKd0DzyEXxLCbY12Ue4edvclGwKN8_hH1RpSgJVSpUMaAmf0EALw_wcB'
    driver.get(fliki_url)
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div/div/header/div/nav[2]/a[5]').click()  # 登入
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/button[1]').click()  # new file
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/div[1]/input').send_keys('懸疑故事230807')
    time.sleep(0.5)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/div[2]/select').click()  # 下拉
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/div[2]/select/option[14]')  # 中文
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/div[3]/label[1]/input').click()  # audio
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[2]/button').click()  # submit
    time.sleep(10)

#創建音頻(選聲音)
def select_audio():
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div[1]/div[3]/div[2]/div/div[2]/div/button').click()  # 選聲音
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div/select').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div/select/option[8]').click()  # 選TW
    time.sleep(0.5)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[3]/div/button').click()  # 男生
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/label/input').click()  # all
    time.sleep(0.5)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button').click()  # select
    time.sleep(5)


#創建音頻(創建)
def download_audio():
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[1]/div[3]/div[2]/div/div[2]/div/div/div/div/p').send_keys(pc.paste())
    time.sleep(20)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/button').click()  # download
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button').click()  # export
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]').click()  # confirm
    time.sleep(15)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/button').click()  # download file
    time.sleep(20)

#產生圖片
def aiprm():
    actions = ActionChains(driver)
    actions.key_down(Keys.ALT).send_keys("a").key_up(Keys.ALT).perform()
    time.sleep(6)
    actions.key_down(Keys.ALT).send_keys("a").key_up(Keys.ALT).perform()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div/div[2]/button[1]').click()  # cancel
    time.sleep(3)