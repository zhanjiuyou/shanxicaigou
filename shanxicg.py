# 2020.9.13日
# 本次爬虫主要是实现陕西政府采购网的爬虫
# 该爬虫以技术交流为准，切勿用于任何非法用途，后果自负
# 我的个人博客：https://jiaokangyang.com

from selenium import webdriver
import time

from pyquery import PyQuery as pq

# 由于该网站是javascript来异步加载的，而且requests不能正常获取，这里我们使用selenium爬取

url = 'http://ccgp-shaanxi.gov.cn/notice/list.do?noticetype=3&province=province'
shuru = '宝鸡市'
shuru2 = input('请输入上述城市中要筛选的区域名：\n （如不需要筛选则直接敲击回车键开始抓取）')
# 打开谷歌浏览器
brower = webdriver.Chrome()
# 打开采购信息的网页
brower.get(url)
# 打开网页后，点击对应城市的标签，然后异步加载的内容进行加载。
brower.find_element_by_link_text(shuru).click()
# 这块由于代码自动操作太快，有时出现内容没更新的情况，所以我们等待两秒
time.sleep(2)
html = brower.page_source

# 该函数完成单页内容的采集输出
def get_onepage(html):
    html = pq(html)
    a = '[' + shuru2 + ']'
    lists = html('.list-box table tbody tr').items()
    for list in lists:
        if shuru2 != '':
            b = list('td:nth-child(2)').text() # 使用pyquery的伪类用法查找第二个元素内的名字
            if b == a:  # 对比分析，如果和我们输入的区域名字相同，则打印出来
                print(list('td a ').text())
                print(list('td a ').attr('href'))
        else:
            print(list('td a ').text())
            print(list('td a ').attr('href'))

# 上面完成单页信息的采集，现在进行前十页的信息采集。

get_onepage(html)
