import unittest

from reuse_func import GetData


class CqubeLogin(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.cal = GetData()
        self.driver = self.cal.get_driver()
        self.driver.implicitly_wait(30)

    def test_login_page(self):
        self.cal.open_cqube_appln(self.driver)
        self.cal.login_cqube(self.driver)
        self.assertEqual("cQube",self.driver.title,"cqube application is not working")


    @classmethod
    def tearDownClass(self):
        self.driver.close()