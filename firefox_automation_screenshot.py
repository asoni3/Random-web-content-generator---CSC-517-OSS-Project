
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import os


browser = webdriver.Firefox(executable_path=r'C:\geckodriver-v0.20.1-win64\geckodriver.exe') # path to geckodriver.exe, to get instance of firefox
for x in range(5):
        file= os.path.abspath("file"+str(x)+".html")
        browser.get("file:///"+file) #go to html page withe firefox
        browser.set_window_size(1229,881) #set size to 1229x881(includes the border of browser) to get resolution 1200x800
        browser.save_screenshot("screen"+str(x)+".png") #saves the current screen
browser.close()

