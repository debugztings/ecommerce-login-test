# -*- coding: utf-8 -*-
"""
探测页面上的所有元素
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://demo.guru99.com/test/login.html")
time.sleep(3)

print("页面标题:", driver.title)
print("\n页面上所有 input 元素:")
print("-" * 50)

inputs = driver.find_elements("tag name", "input")
for i, inp in enumerate(inputs):
    tag_name = inp.get_attribute("type")
    name_attr = inp.get_attribute("name")
    id_attr = inp.get_attribute("id")
    class_attr = inp.get_attribute("class")
    placeholder = inp.get_attribute("placeholder")
    value = inp.get_attribute("value")
    
    print(f"元素 {i}:")
    print(f"  type: {tag_name}")
    print(f"  name: {name_attr}")
    print(f"  id: {id_attr}")
    print(f"  class: {class_attr}")
    print(f"  placeholder: {placeholder}")
    print(f"  value: {value}")
    print()

# 也看看所有可点击元素
print("页面上所有可点击元素 (button/input[type=submit]/input[type=button]):")
print("-" * 50)
clickables = driver.find_elements("xpath", "//button | //input[@type='submit'] | //input[@type='button']")
for i, c in enumerate(clickables):
    print(f"元素 {i}:")
    print(f"  tag: {c.tag_name}")
    print(f"  text: {c.text}")
    print(f"  value: {c.get_attribute('value')}")
    print()

driver.quit()
