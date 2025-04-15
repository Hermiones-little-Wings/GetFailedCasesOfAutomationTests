import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

# 启动浏览器并打开登录页面
driver = webdriver.Edge()

# 手动粘贴网址
driver.get("https://msazure.visualstudio.com/RedisCache/_releaseProgress?_a=release-environment-extension&releaseId=13536&environmentId=34334&extensionId=ms.vss-test-web.test-result-in-release-environment-editor-tab")
time.sleep(10)
# 等待并选择之前登录的账户
account_to_select = 'v-junruma@microsoft.com'

# 增加等待时间，确保元素加载完成
accounts = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[role="button"]'))
)

time.sleep(10)
# 遍历所有符合条件的元素
for account in accounts:
    if account_to_select in account.text:
        account.click()
        break

# 等待一段时间，确保操作完成
time.sleep(10)

#点击进入主页面
accepted = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[2]/form[2]/div/input')

accepted.click()

time.sleep(40)

#点击展开所有错误测试
print("错误测试展开中.....")
tests = driver.find_elements(By.CLASS_NAME, "clickable-text")
time.sleep(8)
for test in tests:
    test.click()
time.sleep(20) 

#获取到所有错误测试
testshow = driver.find_elements(By.CLASS_NAME, "clickable-text")
time.sleep(10) 
print("初始错误测试如下:")
# 使用正则表达式提取每行倒数第二个.后的值
pattern = r'\.(?=[^.]*\.[^.]*$)(.*)'

# 将错误测试内容保存到txt文件
with open("test_results.txt", "w", encoding="utf-8") as file:
    for test in testshow:
        print(test.text)
        matches = re.findall(pattern, test.text)
        for matche in matches:
            if(len(matche)<=26):
                break;
            else:
                file.write(matche + "\n")
            
print("保存成功")

# 关闭浏览器
driver.quit()