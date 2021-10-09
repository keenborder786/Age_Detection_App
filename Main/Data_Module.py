import numpy as np
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

class Google_download:
    
    
    def __init__(self):
        
        self.driver = webdriver.Chrome('C:/Software/chromedriver.exe')
        self.driver.get('https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl')
        
        
    def download_images(self,key_word,number_images):
        """
        This Method downloads images for the key_word from Google Images through selium created bot

        Parameters
        ----------
        key_word : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        box = self.driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
        if not os.path.isdir(f'data\{key_word}'):
           os.mkdir(f'data\{key_word}')
        box.send_keys(key_word)
        box.send_keys(Keys.ENTER)
        last_height = self.driver.execute_script('return document.body.scrollHeight')
        
        while True:
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            new_height = self.driver.execute_script('return document.body.scrollHeight')
            for i in range(1,10000000):
             try:
                self.driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot(f'data\{key_word}\key_word_image+{str(i)}.png')
                current_number_images=len([name for name in os.listdir(os.path.join(os.getcwd(),'data',key_word))])
                if current_number_images>=number_images:
                    break 
             except:
                 pass
   
                
            if new_height == last_height or current_number_images>=number_images:
                self.driver.close()
                break
            time.sleep(2)
            last_height = new_height
        
if __name__ == "__main__":
    GD=Google_download()
    GD.download_images("Female 20",number_images=100)