import requests
from pyquery import PyQuery as pq
url = 'http://www.ccgp-shaanxi.gov.cn/notice/noticeDetail.do?noticeguid=8a85be327394d739017476a9d50f3b5b'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/',
}
html = requests.get(url,headers=headers)

b = pq(html.text)
lists = b('.inner-Box').text()
print(lists)



