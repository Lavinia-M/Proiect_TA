import unittest
import HtmlTestRunner

from test_alerts import Alerts
from test_file_download import FileDownload
from test_form_auth import FormAuthentication
from test_geolocation import Geolocation
from test_forgot_password import ForgotPassword

class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(FileDownload),
            unittest.defaultTestLoader.loadTestsFromTestCase(FormAuthentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(Geolocation),
            unittest.defaultTestLoader.loadTestsFromTestCase(ForgotPassword)

        ])
        runner = HtmlTestRunner.HTMLTestRunner(log=True,title='Test Suite ',
                            description='Result of tests', open_in_browser=True , tested_by= "Manolea Lavinia")

        runner.run(tests_to_run)
