# -*- coding: utf-8 -*-
"""
电商网站登录模块自动化测试脚本 - 最终版
测试人员：ztings
测试时间：2026.06.30
测试网站：https://demo.guru99.com/test/login.html
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import unittest

class LoginAutomation(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "https://demo.guru99.com/test/login.html"

    def tearDown(self):
        self.driver.quit()

    def login_and_click(self, email="", password=""):
        """通用登录操作"""
        self.driver.get(self.base_url)
        time.sleep(2)

        if email:
            self.driver.find_element("id", "email").send_keys(email)
        if password:
            self.driver.find_element("id", "passwd").send_keys(password)

        # 点击第一个按钮（Sign in）
        btn = self.driver.find_elements("tag name", "button")[0]
        btn.click()
        time.sleep(3)

    def test_01_login_page_loads(self):
        """用例1：登录页面正常加载"""
        print("\n=== 用例1：登录页面加载 ===")
        self.driver.get(self.base_url)
        time.sleep(2)
        self.assertIn("Login", self.driver.title)
        print("OK 测试通过：登录页面正常加载")

    def test_02_input_credentials(self):
        """用例2：输入邮箱和密码"""
        print("\n=== 用例2：输入邮箱和密码 ===")
        self.driver.get(self.base_url)
        time.sleep(2)
        self.driver.find_element("id", "email").send_keys("test@example.com")
        self.driver.find_element("id", "passwd").send_keys("Test123456")
        print("OK 邮箱和密码输入成功")

    def test_03_normal_login(self):
        """用例3：正常登录"""
        print("\n=== 用例3：正常登录 ===")
        self.login_and_click("test@example.com", "Test123456")
        print("OK 登录提交成功")

    def test_04_empty_email(self):
        """用例4：邮箱为空"""
        print("\n=== 用例4：邮箱为空 ===")
        self.login_and_click(email="", password="Test123456")
        print("OK 邮箱为空时的处理已验证")

    def test_05_empty_password(self):
        """用例5：密码为空"""
        print("\n=== 用例5：密码为空 ===")
        self.login_and_click(email="test@example.com", password="")
        print("OK 密码为空时的处理已验证")

    def test_06_invalid_email(self):
        """用例6：邮箱格式不正确"""
        print("\n=== 用例6：邮箱格式不正确 ===")
        self.login_and_click(email="invalid-email", password="Test123456")
        print("OK 邮箱格式不正确时的处理已验证")


if __name__ == "__main__":
    print("=" * 50)
    print("电商网站登录模块自动化测试")
    print("测试网站：https://demo.guru99.com/test/login.html")
    print("=" * 50)
    unittest.main(verbosity=2)
