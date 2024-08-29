"""
    实现功能：具体测试用例文件。
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def take_screenshot(driver, file_name):
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_path = os.path.join(screenshots_dir, f"{file_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")


def test_example():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://www.example.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium")
        search_box.submit()
        assert "Selenium" in driver.title
    except Exception as e:
        take_screenshot(driver, "test_example_error")
        print(f"Error occurred: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_example()
