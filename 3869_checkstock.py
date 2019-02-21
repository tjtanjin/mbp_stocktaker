from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import platform, time, subprocess, os, sys, sendgrid, json
from sendgrid.helpers.mail import *
os.chdir(os.path.realpath(sys.path[0]))

class Stocktaker():
    def __init__(self):
        #instantiate options for chrome browser
        chromeoptions = Options()
        #execute code for hiding window
        chromeoptions.add_argument("window-size=1440x900")
        chromeoptions.headless = True
        #initialize
        self.driver = webdriver.Chrome(options=chromeoptions)
        self.driver.implicitly_wait(30)
        self.url = ""

    def stocktake(self):
        """
        Function to check the macbook stock.
        Args:
            None
        """
        driver = self.driver
        #navigate and search for desired macbook by price
        driver.get("https://www.apple.com/sg/shop/refurbished")
        time.sleep(5)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Shop Refurbished'])[1]/following::img[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Memory'])[3]/following::span[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Memory'])[4]/following::label[4]").click()
        time.sleep(5)
        #execute if price of that macbook in page source
        if "S$3,869.00" in driver.page_source:
            try:
                #try to click on the macbook with desired specs
                driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Refurbished 15.4-inch MacBook Pro 2.6GHz 6-core Intel Core i7 with Retina display - Space Grey'])[1]/following::div[1]").click()
                time.sleep(5)
                #tally with price to make sure it is definitely the macbook desired
                if "S$3,869.00" in driver.page_source:
                    #screenshot and save to folder
                    driver.save_screenshot("./screenshots/3869_AVAILABLE_MBP.png")
                    time.sleep(3)
                    #get url of page
                    self.url = driver.current_url
                    time.sleep(3)
                    #stop/comment out the cron schedule
                    subprocess.run(["sed -i '2s/^/#/' /var/spool/cron/path_to_directory"], shell=True)
                    #send email to notify that macbook is available!
                    self.email_notification()
            except:
                pass
        self.driver.quit()

    def email_notification(self):
        """
        Function to send email to notify once macbook is available.
        Args:
            None
        """
        content_body = "Check out the macbook here: " + self.url
        from_email = Email(email)
        to_email = Email(email)
        subject = "Desired MacBook Pro is here!"
        content = Content("text", content_body)
        sg = sendgrid.SendGridAPIClient(sendgrid_api_key)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())

stocktaker = Stocktaker()
try:
    stocktaker.stocktake()
except:
    #create file to notify failure of code
    subprocess.run(["touch 3869_STOCKTAKE_FAILED.txt"], shell=True)
finally:
    #end all chrome processes
    subprocess.run(["killall chromedriver"], shell=True)
    subprocess.run(["killall chrome"], shell=True)
