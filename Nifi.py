import unittest

from reuse_func import GetData


class TestNifi(unittest.TestCase):
    def test_static_data_transformer(self):
        cal = GetData()
        nifi_componets = cal.get_nifi_status()
        for x in nifi_componets:
            if x.get('name') == "static_data_transformer":
                self.runningCount = x.get('runningCount')
                self.stoppedCount = x.get('stoppedCount')
                self.invalidCount = x.get('invalidCount')
                self.disabledCount = x.get('disabledCount')




if __name__ == '__main__':
    unittest.main()
