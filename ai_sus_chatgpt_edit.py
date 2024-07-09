from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException
import pyperclip as pc
import pyautogui
import pygetwindow as gw

# "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --profile-directory="Default" --remote-debugging-port=9222

def initialize_driver():
    options = Options()
    options.add_experimental_option("debuggerAddress", "localhost:9222")
    s = Service(r"C:\Users\underdog\PycharmProjects\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)
    return driver

def mouse():
    current_x, current_y = pyautogui.position()
    print(f"Current mouse position: ({current_x}, {current_y})")

def test(driver):
    driver.get('https://www.4gamers.com.tw/news/detail/55039/fire-emblem-engage-announced')

def navigate_and_ask_openai(driver):
    driver.get('https://chat.openai.com/')
    time.sleep(5)
    pyautogui.click(1241, 208)  # gpt4
    time.sleep(1.5)
    driver.find_element(By.XPATH, '//*[@id="prompt-textarea"]').send_keys(
        '一分鐘介紹一個已解決的真實懸疑案件,只有內容,多一點案件細節,不要加標題,不要其他多餘的介紹或對話')
    button_sus = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/main/div/div[2]/form/div/div[2]/div/button')
    button_sus.click()
    time.sleep(60)
    try:
        answer_sus = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div').text
        print(answer_sus)
        pc.copy(answer_sus)
    except NoSuchElementException:
        print('再等15秒')
        time.sleep(15)
        answer_sus = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div').text
        print(answer_sus)
        pc.copy(answer_sus)

def nevigate_test(driver):
    driver.get('https://chat.openai.com/c/6bbb03b5-6a4f-438d-b010-a6ff77fbdb3e')
    time.sleep(10)
    try:
        answer_test = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/main/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div').text
        print(answer_test)
        pc.copy(answer_test)
    except NoSuchElementException:
        print('再等15秒')
        time.sleep(15)
        answer_test = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/main/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div').text
        print(answer_test)
        pc.copy(answer_test)


def open_fliki_and_create_audio(driver):
    driver.execute_script("window.open('https://www.google.com', '_blank');")
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    driver.get('https://fliki.ai/')
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div/div/header/div/nav[2]/a[5]').click()  # 登入
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/button[1]').click()  # new file
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/div[3]/input').send_keys('懸疑故事230822')
    time.sleep(0.5)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/div[1]/select').click()  # 下拉
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/div[1]/select/option[14]').click()  # 中文
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/div[2]/select').click()  # 下拉dia
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/div[2]/select/option[4]').click()  # tw
    time.sleep(2)
    pyautogui.click(1105, 405)
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/div[4]/label[1]/div').click()  # audio
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[2]/button').click()  # submit
    time.sleep(10)

def select_audio(driver):
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[1]/div[3]/div[2]/div/div[2]/div/button').click()  # select_voice
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div/select').click()  # dia2
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div/select/option[8]').click()  # TW2
    time.sleep(2)
    pyautogui.click(973, 291)
    time.sleep(1.5)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div[9]/div/button').click()  # yun
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/label/input').click()  # all
    time.sleep(0.5)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button').click()  # select
    time.sleep(5)

def download_audio(driver):
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[1]/div/div[2]/div[1]/div[3]/div[2]/div/div[2]/div/div/div/div/p').send_keys(pc.paste())
    time.sleep(20)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[1]/div[3]/div[1]/div[2]/button[1]').click()  # play
    time.sleep(15)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/button').click()  # download
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="radix-:rr:"]/div[3]/button').click()  # export
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="radix-:r2b:"]/div/button[1]').click()  # confirm
    time.sleep(30)
    driver.find_element(By.XPATH, '//*[@id="radix-:rr:"]/div[2]/div[2]/button').click()  # download file
    time.sleep(20)

def aiprm_open():
    time.sleep(10)
    pyautogui.keyDown('alt')
    time.sleep(0.5)
    pyautogui.press('a')
    time.sleep(0.5)
    pyautogui.keyUp('alt')
    time.sleep(7)
    pyautogui.keyDown('alt')
    time.sleep(0.5)
    pyautogui.press('a')
    time.sleep(0.5)
    pyautogui.keyUp('alt')
    time.sleep(15)
    pyautogui.click(1071, 802)  # cancel
    time.sleep(2)
    for _ in range(3):
        pyautogui.click(1914, 336)
    time.sleep(5)
    pyautogui.click(828, 553)  # MIDjourney
    time.sleep(4)
    pyautogui.click(797, 924)  # textarea
    time.sleep(1)
    pyautogui.keyDown('ctrl')
    time.sleep(0.5)
    pyautogui.press('v')
    time.sleep(0.5)
    pyautogui.keyUp('ctrl')
    time.sleep(5)
    pyautogui.click(1633, 932)  # send

def activate_capcut():
    # 獲取所有窗口
    windows = gw.getWindowsWithTitle('')

    # 搜索與 Chrome 9222 相關的窗口
    for window in windows:
        if "CapCut" in window.title:  # 根据窗口的标题来判断
            window.activate()  # 将窗口带到最前端
            break


def activate_chrome_9222():
    # 獲取所有窗口
    windows = gw.getWindowsWithTitle('')

    # 搜索與 Chrome 9222 相關的窗口
    for window in windows:
        if "新分頁 - Google Chrome" in window.title:  # 根据窗口的标题来判断
            window.activate()  # 将窗口带到最前端
            break

def activate_chrome_Fliki():
    # 獲取所有窗口
    windows = gw.getWindowsWithTitle('')

    # 搜索與 Chrome 9222 相關的窗口
    for window in windows:
        if "Fliki - Turn text into videos with AI voices - Google Chrome" in window.title:  # 根据窗口的标题来判断
            window.activate()  # 将窗口带到最前端
            break

def window_title():
    windows = gw.getWindowsWithTitle('')
    for window in windows:
        print(window.title)

def main():
    driver = initialize_driver()
    activate_chrome_9222()
    navigate_and_ask_openai(driver)
    open_fliki_and_create_audio(driver)
    select_audio(driver)
    download_audio(driver)
    #aiprm_open()
    #activate_capcut()
    #nevigate_test(driver)
    #mouse()
    #test(driver)
    #driver.close()
    #window_title()

if __name__ == '__main__':
    main()


