import time

from selenium.webdriver.common.alert import Alert
# from quote.base.browseroperation import BrowserOperation
# from quote.base.usebrowser import UseBrowser
from quote.config.log_crm import AutoLog
from quote.util.yaml_operation import YamlOperation
from quote.webpage.usermanager.loginpage import LoginPage


class CustomerPage:
    def __init__(self):
        self.log = AutoLog()
        self.lp=LoginPage()
        self.ya=YamlOperation('../../config/locator.yaml')

    def customer_add(self,customername='',customerEmail='',customerbrithday='',create=''):
        time.sleep(5)
        self.lp.bo.driver.switch_to.frame('topFrame')
        self.log.set_mes('topFrame success', 'info')
        self.lp.bo.click_element(self.ya.get_locator('CustormerPage','cusmessage'))
        self.lp.bo.driver.switch_to.default_content()
        self.lp.bo.driver.execute_script("document.getElementsByTagName('frameset')[1]")
        self.lp.bo.driver.switch_to.frame('mainFrame')
        self.lp.bo.click_element(self.ya.get_locator('CustormerPage', 'cusaddbutton'))
        self.lp.bo.send_keys(self.ya.get_locator('CustormerPage', 'customername'),customername)
        self.log.set_mes('username success', 'info')
        self.lp.bo.driver.execute_script("document.getElementById('customerBirthday').readOnly=false")
        self.lp.bo.send_keys(self.ya.get_locator('CustormerPage', 'customerbrithday'), customerbrithday)
        self.lp.bo.send_keys(self.ya.get_locator('CustormerPage', 'customerEmail'), customerEmail)
        self.lp.bo.send_keys(self.ya.get_locator('CustormerPage', 'create'), create)
        self.lp.bo.click_element(self.ya.get_locator('CustormerPage', 'addbutton'))
        self.log.set_mes('submit click', 'info')
        time.sleep(5)
    def customer_change(self,weibo):
        time.sleep(5)
        self.lp.bo.driver.switch_to.frame('topFrame')
        self.log.set_mes('topFrame success', 'info')
        self.lp.bo.click_element(self.ya.get_locator('CustormerPage', 'cusmessage'))
        self.lp.bo.driver.switch_to.default_content()
        self.lp.bo.driver.execute_script("document.getElementsByTagName('frameset')[1]")
        self.lp.bo.driver.switch_to.frame('mainFrame')
        self.log.set_mes('mainFrame success', 'info')
        time.sleep(5)
        self.lp.bo.click_element(self.ya.get_locator('CustormerPage', 'editor'))
        time.sleep(5)
        self.lp.bo.driver.find_element_by_xpath(self.ya.get_locator('CustormerPage','weibo')).clear()
        self.lp.bo.send_keys(self.ya.get_locator('CustormerPage', 'weibo'), weibo)
        self.lp.bo.click_element(self.ya.get_locator('CustormerPage', 'submit'))
        self.log.set_mes('submit click success', 'info')
        time.sleep(5)
    def alert_text(self):
        alert = Alert(self.lp.ub.driver)
        return alert.text
    # def customer_add(self,**kwargs):
    #     self.lp.bo.change_frame('Links')
    #     self.lp.bo.click_element('//*[@id="Bar_panel0_b0"]/img')
    #     self.lp.bo.change_frame('main')
    #     self.lp.bo.click_element('/html/body/center/table[2]/tbody/tr[2]/td[2]/a')
    #     self.lp.bo.change_window('新增客户信息')
    #     self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input',kwargs.get('id',''))
    #     self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[4]/input',kwargs.get('name', ''))
    #     self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input',kwargs.get('telephone', ''))
    #     self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[4]/input',kwargs.get('address', ''))
    #     self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input',kwargs.get('relationman', ''))
    #     self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[4]/input',kwargs.get('other_info', ''))
    #     self.lp.bo.click_element('/html/body/center/form/table[2]/tbody/tr/td/input[1]')

    # def get_add_sucess_text(self):
    #     self.lp.bo.change_window('添加记录成功')
    #     customer_add_text=self.lp.bo.get_text('/html/body/center')
    #     return customer_add_text
    # def customer_modify(self):
    #     pass
# if __name__ == '__main__':
#     cp=CustomerPage()
#     cp.customer_add('大一','21314123@qq.com','2020/2/2 22:22:22','大二')