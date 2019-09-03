# libraries================>>

try:
    from selenium import webdriver
    from selenium.common.exceptions import InvalidArgumentException
    from PIL import Image
    from datetime import datetime
    import os
    import csv
    import time
except ImportError:
    print(">>> Import Error - check the following libraries are installed:")
    print("selenium, PIL, datetime, os, time, csv")
    quit()


class screenGrabber(urlList):

    def __init__(self, urlList):
        self.driver = webdriver.Safari()
        # self.input = open("pages.csv", "r", newline="") # urlList
        # self.data = csv.reader(input)
        self.data = urlList

    # new directory and return file path
    def setDirectory(input):
        fpath = "/Users/lam/Desktop/seleniumTest/" + input
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        return fpath

    # screenshot function
    def saveFullGrab(driver=self.driver, url, outPath, tmp_suffix=".png"):
        try:
            driver.get(url)
            time.sleep(1)
        except InvalidArgumentException:
            print(">>> Driver Error: website not found: " + url)
            return

        # page dims
        height = 'return document.body.parentNode.scrollHeight'
        width = 'return document.body.offsetWidth'
        scroll_height = driver.execute_script(height)
        scroll_width = driver.execute_script(width)
        driver.set_window_size(scroll_width, scroll_height)

        # save screenshot
        t = datetime.now()
        path = t.strftime("%Y%m%d%H%M")
        driver.save_screenshot(outPath + path + tmp_suffix)

        # compare images
        f1 = os.listdir(outPath)[len(os.listdir(outPath)) - 1]
        img1 = Image.open(outPath + f1)
        try:
            f2 = os.listdir(outPath)[len(os.listdir(outPath)) - 2]
            img2 = Image.open(outPath + f2)
            if list(img1.getdata()) == list(img2.getdata()):
                os.remove(outPath + f1)
        except OSError:
            return

    def runScript(driver=self.driver, data=self.data):
        for line in data:
            fpath = setDirectory(line[2]) + "/"
            saveFullGrab(driver, line[1], fpath)
        driver.close()


# script===================>>

urls = []
sg = screenGrabber(urls)
sg.runScript()
