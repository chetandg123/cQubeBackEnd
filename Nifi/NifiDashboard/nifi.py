import unittest

from reuse_func import GetData


class NifiDashboard(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.cal = GetData()
        self.nifi_domain = self.cal.get_domain_name()+"/nifi"
        self.driver = self.cal.get_driver()
        self.driver.implicitly_wait(30)

    def test_nifi_dashboard(self):

        self.driver.get(self.nifi_domain)
        self.assertEqual("NiFi Flow",self.driver.title,"Nifi dashboard is not working")

    @classmethod
    def tearDownClass(self):
        self.driver.close()
