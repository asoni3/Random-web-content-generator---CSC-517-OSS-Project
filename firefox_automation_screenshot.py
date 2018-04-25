from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import os
import sys
import getopt  # for command line interaction
from PIL import Image


def main(argv):
    try:
        # input options defined here.
        opts, args = getopt.getopt(argv, "w:h:n:", ["width=","height=", "numOfFiles="])
    except getopt.GetoptError:
        # an error is generated if the options provided in commandline are wrong.
        # The help statement is printed on how to input command line arguments.
        print('python3 firefox_automation_screenshot.py  -w <width> -h <height> -n <numOfFiles>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-w", "--width"):  # store the value provided with the option -r in resolution variable.
            global width
            width = int(arg)
        if opt in("-h","--height"):
            global height
            height= int(arg);
        elif opt in ("-n", "--numOfFiles"):  # store the value provided with the option -n in num_of_files variable.
            global num_of_files
            num_of_files = int(arg)
    browser = webdriver.Firefox()  # path to geckodriver
    for x in range(num_of_files):
        file = os.path.abspath("file" + str(x) + ".html")
        browser.get("file:///" + file)  # go to html page withe firefox
        set_viewport(browser, width, height,x)
        browser.save_screenshot("screen" + str(x) + ".png")  # saves the current screen
    browser.close()


def set_viewport(driver, width, height,num_file):
    driver.set_window_position(0,0)
    driver.set_window_size(width,height)
    driver.save_screenshot("screen" + str(num_file) + ".png")
    img= Image.open("screen" + str(num_file) + ".png")
    img_width, img_height=img.size
    if img_width!=width:
        width=width-(img_width-width)#correction to width length
    if img_height!=height:
        height=height-(img_height-height) #correction to height length
    driver.set_window_size(width,height)
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Argument input is required in the format')
        print(
            'python3 etc/servo_automation_screenshot.py -w <width> -h <height> -n <numOfFiles>')
        sys.exit()
    else:
        main(sys.argv[1:])
