"""
    实现功能：浏览器驱动管理脚本。
"""
import os
import yaml
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


def load_config():
    """
    功能：使用相对路径加载yaml配置文件
    """
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config


config = load_config()


def get_chrome_driver():
    """
    功能：获取Chrome浏览器驱动
    """
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver


def get_firefox_driver():
    """
    功能：获取Firefox浏览器驱动
    """
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    return driver


def get_edge_driver():
    """
    功能：获取Edge浏览器驱动
    """
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    return driver


def get_driver():
    """
    功能：根据配置文件中的浏览器类型获取对应的浏览器驱动
    """
    browser = config['browser'].lower()
    if browser == 'chrome':
        return get_chrome_driver()
    elif browser == 'firefox':
        return get_firefox_driver()
    elif browser == 'edge':
        return get_edge_driver()
    else:
        raise ValueError(f"Unsupported browser: {browser}")


if __name__ == '__main__':
    driver = get_driver()
    driver.get(config['base_url'])
    driver.quit()
