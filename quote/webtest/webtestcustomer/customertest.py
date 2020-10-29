import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import sys
sys.path.append('F:\\Pycharmproject\\test')
from quote.base.usebrowser import UseBrowser
from quote.util.excel_operation import OperationExcel
from quote.webpage.custormermanager.customerpage import CustomerPage


class CustomerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cp=CustomerPage()
        self.op = OperationExcel('../../config/test_case.xlsx', '用例参数')
        self.cp.lp.bo.open_url(self.op.get_cell(6,1))
        self.cp.lp.login(self.op.get_cell(6,2), self.op.get_cell(6,3))
    # def test_custemer_add_success(self):
    #     self.cp.customer_add(self.op.get_cell(6,5),self.op.get_cell(6,6),self.op.get_cell(6,7),self.op.get_cell(6,8))
    #     self.assertEqual(self.op.get_cell(6,4),self.cp.lp.alert_text())
    def test_custemer_modify_success(self):
        self.cp.customer_change(self.op.get_cell(7,9))
        self.assertEqual(self.op.get_cell(7,4),self.cp.lp.alert_text())
    # def test_customer_add_only_id(self):
    #     self.cp.customer_add(id='1237890')
    #     self.assertEqual(self.cp.get_add_sucess_text(),'添加记录成功！\n本窗口将在3秒后自动关闭')
    # def test_customer_add_id_name(self):
    #     self.cp.customer_add(id='123523',name='小二')



    def tearDown(self) -> None:
        UseBrowser.quit()
if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(CustomerTest)
    suite.addTests(test_case)
    date_now = time.strftime('%Y-%m-%d', time.localtime())
    with open('../../report/report.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=2, title='auto_test', description=None)
        runner.run(suite)