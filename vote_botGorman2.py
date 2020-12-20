#1st: in terminal type:
# pip install selenium
#instead of source, use . (the period)
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class VoteBot():
    def  __init__(self):
        self.driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
    def vote(self):
        #self.driver.get('http://myvote.remaxallpro.com/')
        self.driver.get('https://www.quiz-maker.com/poll3290558x992a4468-101')
        #button_elementVoteNow = self.driver.find_element_by_xpath("/html/body/div/center[1]/p/a")
        #button_elementVoteNow.click()
        #inspect the button
        #right click
        #copy full xPath
        #for xPath: words have to be surrounded by ' ' not " "
        button_elementGorman = self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div[1]/div/form/div[1]/table/tbody/tr/td[1]/div[11]")
        button_elementGorman.click()
        button_elementSubmit = self.driver.find_element_by_name('qp_b3290558')
        button_elementSubmit.click()

        button_elementNext = self.driver.find_element_by_xpath("//*[@id='pres-next']")
        button_elementNext.click()

        self.driver.close()

i = 0
while i<=12:
  bot = VoteBot()
  bot.vote()
  i += 1