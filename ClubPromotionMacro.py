from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
driver.find_element_by_id('txtPWD').send_keys(userId)
driver.find_element_by_class_name('button01').click()