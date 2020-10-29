# import time

from selenium.webdriver.common.alert import Alert

from quote.base.browseroperation import BrowserOperation
from quote.base.usebrowser import UseBrowser
from quote.config.log_crm import AutoLog
# from quote.util.excel_operation import OperationExcel
from quote.util.yaml_operation import YamlOperation


class LoginPage:
    def __init__(self):
        self.log = AutoLog()
        self.ub = UseBrowser()
        self.bo = BrowserOperation(UseBrowser.driver)
        self.ya=YamlOperation('../../config/locator.yaml')


    def login(self,username='',password=''):
        self.log.set_mes('---登录功能开始---', 'info')
        self.bo.send_keys(self.ya.get_locator('LoginPage','username'),username)
        self.log.set_mes('-输入用户名-', 'info')
        self.bo.send_keys(self.ya.get_locator('LoginPage','password'),password)
        self.log.set_mes('-输入密码-', 'info')
        self.bo.click_element(self.ya.get_locator('LoginPage','submit'))
        self.log.set_mes('-点击登录-', 'info')

    def login_correct_text(self,frame_name,xpath):
        self.bo.change_frame(frame_name)
        return  self.bo.get_text(xpath)

    def alert_text(self):
        alert = Alert(self.ub.driver)
        return alert.text
# if __name__=='__main__':
#     lp=LoginPage()
#     lp.login()
#     time.sleep(2)
#     UseBrowser.quit()