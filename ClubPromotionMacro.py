from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = 'https://kart.nexon.com/Kart/Guild/Story/List.aspx'
driver.get(url)

xpath = "//img[@src='https://ssl.nx.com/s2/game/kart/v2/common/btn_gc_login.jpg']"

driver.find_element_by_xpath(xpath).click()

# 코드에 아이디와 비밀번호를 저장하지 않기위해 따로 입력 받음
print('아이디를 입력해주세요.')
userId = input() 

print('비밀번호를 입력해주세요.')
userPw = input()

driver.find_element_by_id('txtNexonID').send_keys(userId)
driver.find_element_by_id('txtPWD').send_keys(userPw)
driver.find_element_by_class_name('button01').click()

time.sleep(0.8) #페이지가 제대로 열릴때 까지 기다림

xpath = "//img[@src='https://ssl.nx.com/s2/game/kart/v2/community/btn_write.gif']"

driver.find_element_by_xpath(xpath).click()

time.sleep(0.5)

title = "(매우빠름) Lv.2 Realize 길드원 모집"

driver.find_element_by_name('ctl00$ContentPlaceHolder1$m_txtTitle').send_keys(title)

time.sleep(0.5)

driver.find_element_by_class_name('uploadImage').click()

driver.switch_to.window(driver.window_handles[-1]) # 새로운 창으로 변경

time.sleep(0.5)

xpath = "//input[@type = 'file']"

driver.find_element_by_xpath(xpath).send_keys("C:/Users/Minhyuk/Downloads/img.png")

driver.find_element_by_id('btnUpload').click()

driver.switch_to.window(driver.window_handles[0]) # 원래 창으로 변경

time.sleep(1)

driver.find_element_by_id('ContentPlaceHolder1_btnWrite').click()