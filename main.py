from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep
import random

class Google:

    def __init__(self, username, password):

        self.driver = webdriver.Firefox()
        self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get('Insert Google Doc link you use for sharing the meet link')
        sleep(5)
        try:
            def link_check():
                link = self.driver.find_element_by_css_selector('.kix-lineview-content').text
                if 'meet.google' in link:
                        sleep(2)
                        self.driver.get(link)
                        sleep(10)           
                        self.driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/span').click()
                        sleep(90)
                        self.driver.find_element_by_class_name('HKarue').click()
                        sleep(15)
                        pyautogui.typewrite('Present!')
                        pyautogui.typewrite(['enter'])
                        sleep(15)
                        excuses = ['My mic seems to be not working.', 'Having some connection issues', '']
                        pyautogui.typewrite(random.choice(excuses))
                        pyautogui.typewrite(['enter'])
                else:
                    sleep(10)
                    link_check()
            link_check()
        finally:
            sleep(3600)
            self.driver.quit()

                

username = 'Enter your mail here'
password = 'Enter your google password here'
Google(username, password)
