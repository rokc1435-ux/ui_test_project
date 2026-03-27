\# UI Test Framework



基于 Selenium + Pytest 的 UI 自动化测试框架，采用 Page Object 模式，针对 SauceDemo 电商网站进行端到端测试。



\## 技术栈



\- Python 3 + Pytest

\- Selenium WebDriver

\- Page Object 设计模式

\- JSON 数据驱动（pytest.mark.parametrize）

\- Allure 测试报告



\## 项目结构



```

ui\_test\_project/

├── pages/ui/             # Page Object 层

│   ├── base\_page.py      # 基础页面类（通用操作封装）

│   ├── login\_page.py     # 登录页

│   ├── inventory\_page.py # 商品列表页

│   ├── cart\_page.py      # 购物车页

│   └── checkout\_page.py  # 结算页

├── data/                 # JSON 测试数据

├── testcase/             # 测试用例

├── conftest.py           # Pytest fixtures（浏览器初始化等）

├── test\_checkout.py      # 端到端下单流程测试

└── test\_login.py         # 登录功能测试

```



\## 核心功能



\- \*\*PO 模式分层\*\*：BasePage 封装通用操作，各业务页面继承 BasePage，测试用例只调用页面方法，三层职责分离

\- \*\*端到端测试\*\*：覆盖完整购物流程（登录 → 选品 → 加购 → 结算 → 完成订单）

\- \*\*数据驱动\*\*：测试数据抽离至 JSON 文件，支持多组数据参数化执行

\- \*\*Allure 报告\*\*：集成 epic / feature / story 三级标签，测试结果可视化展示

\- \*\*浏览器配置管理\*\*：通过 conftest.py 统一管理 ChromeOptions，支持无头模式、禁用弹窗等配置



\## 快速运行



```bash

\# 安装依赖

pip install selenium pytest allure-pytest



\# 执行测试

pytest test\_checkout.py -v



\# 生成 Allure 报告

pytest test\_checkout.py --alluredir=./allure-results

allure serve ./allure-results

```

