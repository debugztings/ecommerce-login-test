# -*- coding: utf-8 -*-
"""
快速测试：验证 Selenium + chromedriver 是否可用
"""
import sys
import io

# 解决中文输出编码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

print("=" * 50)
print("Selenium 环境快速验证")
print("=" * 50)

try:
    print("\n[1/4] 正在下载 chromedriver...")
    service = Service(ChromeDriverManager().install())
    print("OK chromedriver 安装成功")

    print("\n[2/4] 正在启动 Chrome 浏览器...")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    print("OK Chrome 启动成功")

    print("\n[3/4] 正在访问测试网站...")
    driver.get("https://demo.guru99.com/test/login.html")
    time.sleep(3)
    title = driver.title
    print("OK 页面加载成功")
    print("  标题:", title)

    print("\n[4/4] 正在测试输入功能...")
    username = driver.find_element("name", "uid")
    username.send_keys("mngr279644")
    print("OK 用户名输入成功")

    print("\n" + "=" * 50)
    print("全部测试通过！Selenium 环境正常")
    print("=" * 50)

except Exception as e:
    print("\n测试失败:", str(e))
    print("\n可能原因：")
    print("1. 网络问题导致无法下载 chromedriver")
    print("   解决：先手动下载 chromedriver 放到 Python 的 Scripts 目录")
    print("   下载地址：https://npm.taobao.org/mirrors/chromedriver/")
    print("2. 未安装 selenium")
    print("   解决：pip install selenium")

finally:
    try:
        driver.quit()
    except:
        pass
