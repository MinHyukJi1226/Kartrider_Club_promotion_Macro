from tkinter.font import families
from typing import Collection
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from tkinter import *
import time

from selenium.webdriver.remote import command
from urllib3.packages.six import u

def runMecro():

    userId = idTxt.get()
    userPw = pwTxt.get()
    postTitle = titleTxt.get()

    driver = webdriver.Chrome()
    url = 'https://kart.nexon.com/Kart/Guild/Story/List.aspx'
    driver.get(url)

    xpath = "//img[@src='https://ssl.nx.com/s2/game/kart/v2/common/btn_gc_login.jpg']"

    driver.find_element_by_xpath(xpath).click()

    driver.find_element_by_id('txtNexonID').send_keys(userId)
    driver.find_element_by_id('txtPWD').send_keys(userPw)
    driver.find_element_by_class_name('button01').click()

    time.sleep(0.8) #페이지가 제대로 열릴때 까지 기다림

    xpath = "//img[@src='https://ssl.nx.com/s2/game/kart/v2/community/btn_write.gif']"

    driver.find_element_by_xpath(xpath).click()

    time.sleep(0.5)

    driver.find_element_by_name('ctl00$ContentPlaceHolder1$m_txtTitle').send_keys(postTitle)

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

    xpath="//img[@src='https://ssl.nx.com/s2/game/kart/v2/community/btn_list.gif']"

    driver.find_element_by_xpath(xpath).click()

    time.sleep(1)

root = Tk()
root.title("카트라이더 클럽 홍보 프로그램")
root.resizable(False, False)

title = Label(root, text="카트라이더 클럽 홍보 매크로")

idLable = Label(root, text="아이디")
pwLable = Label(root, text="비밀번호" )
titleLable = Label(root, text="게시물 제목")

idTxt = Entry(root, width=30)
pwTxt = Entry(root, width=30)
titleTxt = Entry(root, width=30)
pwTxt.config(show='*')

photo = Button(root, text="사진 업로드")
run = Button(root, text="실행", command = lambda : runMecro())

title.pack(pady=10)
idLable.pack(pady=8)
idTxt.pack(padx=10)
pwLable.pack(pady=8)
pwTxt.pack(padx=10)
titleLable.pack(pady=8)
titleTxt.pack(padx=10)
photo.pack(pady=10)
run.pack()

root.mainloop()