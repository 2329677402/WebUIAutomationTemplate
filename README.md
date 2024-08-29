[toc]



# WebUIAutomation

> **目标：基于 `Python 3.12.4 + Selenium 4.23.1` 实现当下最流行且易于维护的 WebUI 自动化测试**



## 一、技术栈介绍

1. **浏览器驱动管理**：
   - `webdriver-manager`：自动下载和管理浏览器驱动。

2. **测试框架**：
   - `pytest`：用于编写和运行测试用例。
   - `unittest`：Python自带的单元测试框架。

3. **页面对象模式（POM）**：
   - `selenium`：用于浏览器自动化。
   - `selenium.webdriver.common.by`：用于定位页面元素。

4. **报告生成**：
   - `pytest-html`：生成HTML格式的测试报告。
   - `allure-pytest`：生成Allure格式的测试报告。

5. **日志记录**：
   - `logging`：Python自带的日志记录模块。

6. **数据驱动测试**：
   - `pandas`：用于处理数据驱动测试的数据。
   - `openpyxl`：用于读取和写入Excel文件。

7. **浏览器选项和配置**：
   - `selenium.webdriver.chrome.options`：配置Chrome浏览器选项。
   - `selenium.webdriver.firefox.options`：配置Firefox浏览器选项。

8. **等待机制**：
   - `selenium.webdriver.support.ui.WebDriverWait`：显式等待。
   - `selenium.webdriver.support.expected_conditions`：预期条件。

9. **环境管理**：
   - `conda`：创建独立的Python环境。
   - `pip`：安装和管理Python包。

10. **持续集成**：
    - `jenkins`：持续集成工具。
    - `docker`：容器化测试环境。



## 二、项目结构介绍

以下是一个当下最流行且易于维护的WebUI自动化测试项目的目录结构示例：

```python
WebUIAutomation/
├── config/
│   ├── config.yaml
│   └── driver_manager.py
├── logs/
│   └── test_log.log
├── pages/
│   ├── base_page.py
│   └── baidu_page.py
├── reports/
│   └── test_report.html
├── tests/
│   ├── test_baidu.py
│   └── conftest.py
├── utils/
│   ├── data_reader.py
│   └── logger.py
├── .gitignore
├── requirements.txt
└── README.md
```

> 目录结构说明

- `config/`：存放配置文件和浏览器驱动管理脚本。
  - `config.yaml`：配置文件，存放测试环境、浏览器类型等配置信息。
  - `driver_manager.py`：浏览器驱动管理脚本。

- `logs/`：存放日志文件。
  - `test_log.log`：测试日志文件。

- `pages/`：存放页面对象类。
  - `base_page.py`：基础页面类，封装常用的页面操作方法。
  - `baidu_page.py`：具体页面类，继承自基础页面类，封装百度页面的操作方法。

- `reports/`：存放测试报告。
  - `test_report.html`：测试报告文件。

- `tests/`：存放测试用例。
  - `test_baidu.py`：具体测试用例文件。
  - `conftest.py`：Pytest配置文件，存放fixture等配置。

- `utils/`：存放工具类。
  - `data_reader.py`：数据读取工具类，处理数据驱动测试的数据。
  - `logger.py`：日志工具类，封装日志记录方法。

- `.gitignore`：Git忽略文件，配置不需要提交到版本控制的文件和目录。

- `requirements.txt`：依赖包文件，列出项目所需的第三方库。

- `README.md`：项目说明文件，介绍项目的功能、使用方法等。