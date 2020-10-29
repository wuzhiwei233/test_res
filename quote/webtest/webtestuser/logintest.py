import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import sys
sys.path.append('F:\\Pycharmproject\\test')
from quote.base.browseroperation import BrowserOperation
from quote.base.usebrowser import UseBrowser
from quote.util.excel_operation import OperationExcel
from quote.webpage.usermanager.loginpage import LoginPage


class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.login=LoginPage()
        self.op = OperationExcel('../../config/test_case.xlsx', '用例参数')
        self.bo = BrowserOperation(UseBrowser.driver)
        self.bo.open_url(self.op.get_cell(1,1))

    def test_login_username_password_null(self):
        self.login.login(self.op.get_cell(1,2),self.op.get_cell(1,3))
        self.assertEqual(self.op.get_cell(1,4),self.login.alert_text())
        # error_text=self.bo.get_text('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[5]/td')
        # self.assertEqual(error_text,'请勿非法登录！')
    # def test_login_success(self):
    #     self.login.login(self.op.get_cell(2,2),self.op.get_cell(2,3))
    #     self.assertEqual(self.bo.driver.title, self.op.get_cell(2, 4))
    #     # correct_text=self.login.login_correct_text('main','/html/body/table/tbody/tr[1]/td/span')
    #     # self.assertEqual(correct_text,'欢迎使用报价管理系统')

    def tearDown(self) -> None:
        UseBrowser.quit()
if __name__=='__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    suite.addTests(test_case)
    date_now = time.strftime('%Y-%m-%d', time.localtime())
    with open('../../report/report.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=2, title='auto_test', description=None)
        runner.run(suite)