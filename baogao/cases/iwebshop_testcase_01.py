import unittest
from selenium import webdriver
from time import sleep
import time
import sys


class IWebShop(unittest.TestCase):
    def setUp(self):
        url = 'http://localhost/iwebshop/index.' \
              'php?controller=site&action=index'
        self.driver = webdriver.Firefox()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self):

        driver = self.driver
        driver.quit()

    def test_01_login(self):
        driver = self.driver
        driver.find_element_by_link_text('登录').click()
        # driver.find_element_by_css_selector('[name="login_info"]').send_keys('liqing')
        driver.find_element_by_name("login_info").send_keys('liqing')
        driver.find_element_by_css_selector('[name="password"]').send_keys('123456')
        driver.find_element_by_class_name('submit_login').click()

        # driver.find_element_by_link_text('安全退出').click()
        try:
            result = driver.find_element_by_class_name("loginfo").text
            # print(result)
            self.assertIn('liqing',result)
        except AssertionError:
            now = time.strftime("%Y-%m-%d %H_%M_%S")

            exc_info = sys.exc_info()

            # print(exc_info)
            # print(type(exc_info))

            driver.get_screenshot_as_file('./Images1/bug%s-%s.png' %(now, exc_info[1]))
            raise



if __name__ == '__main__':
    # 该方法由UnitTest框架提供，专门来调试测试用例
    unittest.main()
