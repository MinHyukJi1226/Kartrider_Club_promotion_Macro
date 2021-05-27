from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://kart.nexon.com/Kart/Guild/Story/List.aspx'
driver.get(url)