import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# 1. 自动下载/匹配对应的 Chrome 驱动，并初始化浏览器对象
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 2. 访问目标网址 (就像 API 测试里的 url)
driver.get("https://www.baidu.com")

# 3. 窗口最大化 (防止有些元素被遮挡导致无法点击)
driver.maximize_window()

# 强制等待 3 秒让你看清楚效果 (后续我们会用更优雅的显式等待替换它)
time.sleep(3)

# 4. 退出浏览器并释放资源
driver.quit()