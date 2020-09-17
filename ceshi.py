import requests
from pyquery import PyQuery as pq
url = 'http://www.ccgp-shaanxi.gov.cn/notice/noticeDetail.do?noticeguid=8a85be337394d6bc017499d4094b5f89'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/',
}
html = requests.get(url,headers=headers)

b = pq(html.text)
lists = b('.annBox').text()
print(lists)



