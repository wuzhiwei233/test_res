# from selenium import webdriver
import time

from quote.base.usebrowser import UseBrowser


class BrowserOperation:
    def __init__(self,driver):
        self.driver=driver
        # self.driver = webdriver.Chrome('../chromedriver.exe')
    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e,'url address error')


    def send_keys(self,xpath,content):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(content)
        except Exception as e:
            print(e,'element not find')
    def click_element(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e,'click error')
    def get_text(self,xpath):
        try:
            text=self.driver.find_element_by_xpath(xpath).text
            return text
        except Exception as e:
            print(e,'get text error')
    def change_frame(self,frame):
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(frame)
    def change_window(self,window_name):
        for window_hd in self.driver.window_handles:
            self.driver.switch_to.window(window_hd)
            if self.driver.title==window_name:
                break
# if __name__=='__main__':
#     ub=UseBrowser()
#     bo=BrowserOperation(UseBrowser.driver)
#     bo.open_url('http://172.17.4.216:8080/crm/')
#     bo.send_keys('/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/input','admin')
#     bo.send_keys('/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/input','123456')
#     bo.click_element('//*[@id="in1"]')
#     time.sleep(2)
#     UseBrowser.quit()



