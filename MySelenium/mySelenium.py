from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import csv

class mySelenium():
    
    def __init__(self,driver_path, url, isHeadless = False):
        self.url = 'https://'+ url
        self.driver_path = driver_path
        self.isHeadless = isHeadless
        self.driver = None
    
    def init_and_get_chrome_selenium_driver(self):
        
        options = None
        if self.isHeadless is True:
            options = webdriver.ChromeOptions('headless')
            
        self.driver = webdriver.Chrome(executable_path = self.driver_path, chrome_options = options)
    
    def open_instagram(self):
        self.driver.get(self.url)
        
    def logIn_instagram(self, user_data_path):
        userdata = None
        with open(user_data_path,'r') as csvFile:
            userdata = list(csv.reader(csvFile))
            userdata = sum(userdata, [])
        
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.NAME,'username')))
        self.driver.find_element_by_name('username').send_keys(userdata[0])
        self.driver.find_element_by_name('password').send_keys(userdata[1])
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').submit()
        
    def search_on_instagram_by(self,topic):
        self.driver.get(self.url + '/explore/tags/'+topic)
        
    def click_first_article_on_popularList(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div').click()
        
    def get_name_and_img(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'e1e1d')))
        
        pageSource = self.driver.page_source
        bs = BeautifulSoup(pageSource,'html.parser')
        
        user_name = bs.find('div', {'class':'e1e1d'}).find('a', href = re.compile('^/.')).attrs['href']
        img = bs.find('div', {'class': 'KL4Bh'}).find('img')['src']
        
        return user_name,img
    
    def click_next(self):
        self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
        