import time
from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import Counter

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://cn.bing.com/")
driver.maximize_window()

input_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="sb_form_q"]')  # 定位搜索框
        ))
input_box.send_keys('您的姓名') #搜索姓名
input_box.send_keys(Keys.RETURN)  # 再按回车
# serch_elm=driver.find_element(By.XPATH,'//*[@id="search_icon"]')
# serch_elm.click()
time.sleep(3)
driver.save_screenshot('./123.png') #截屏

driver.execute_script("window.scrollBy(0, 2000);") #滑动屏幕

page=driver.find_element(By.XPATH,'//*[@id="b_results"]/li[13]/nav/ul/li[2]/a')# 第2页

page.click()  #翻页
time.sleep(3)
driver.save_screenshot('./456.png')  #截屏

results = driver.find_elements(By.CSS_SELECTOR, "h2 > a")  # 定位所以h2得元素集
links=[]
for i, result in enumerate(results, 1):
    title = result.text
    link = result.get_attribute("href")
    if link:
        links.append(link)
    print("结果 :{i}".format(i=i))
    print("标题: {title}".format(title=title))
    print("链接: {link}".format(link=link))
    print("-" * 50)

print(links)

domains = [urlparse(link).netloc.replace("www.", "")
          for link in links if link and link.startswith(("http://", "https://"))]  # 提取域名
domain_counts = Counter(domains)
print("域名出现次数统计:")
for domain, count in domain_counts.most_common():  # 按次数从高到低排序
    print("{domain}: {count}次".format(domain=domain,count=count))


input_box1=driver.find_element(By.XPATH,'//*[@id="sb_form_q"]')
input_box1.clear()
input_box1.send_keys('selenium')
input_box.send_keys(Keys.RETURN)


driver.quit()