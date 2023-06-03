import time
import requests
import zlib_state
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

shop_info_url = 'https://shopee.tw/api/v4/shop/get_shop_detail?shopid=6130784'

service = Service("D:\shopee_demo\Shopee-Tracker\chomedriver.exe")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
getPacket = ''
for request in driver.requests:
    if request.response:
        # 挑出商品詳細資料的json封包
        if 'https://shopee.tw/api/v4/item/get?itemid=' + str(item_id) + '&shopid=' + str(shop_id) in request.url:
            # 此封包是有壓縮的，因此需要解壓縮
            getPacket = zlib.decompress(
                request.response.body,
                16+zlib.MAX_WBITS
                )
            break
# driver.get(shop_info_url)
# Cookie = ';'.join(['{}={}'.format(item.get('name'), item.get('value')) for item in driver.get_cookies()])

# print(Cookie)


time.sleep(10)

# headers = {
#     'cookies': Cookie,
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57',
#     'referer': 'https://shopee.tw',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'content-type': 'application/json',
#     'set-cookies': 'SPC_SI=xWVsZAAAAABYRlFmTlI5Utn0hQEAAAAAN1NDbHN0TzE=; Path=/; Domain=.shopee.tw; Max-Age=86400; HttpOnly; Secure',
#     'set-cookies':'SPC_F=DuZ3Phpl9b2SXzsi2zF1O43v4xo1fmVx; REC_T_ID=70ce7b47-9d1c-11ed-b6e4-d0946659d874; SPC_CLIENTID=RHVaM1BocGw5YjJTwbhlierpjluxhgmn; SC_DFP=UGYkdmgCUVmyeiSiOCDjJXEkYoTPYLSg; __stripe_mid=1cece67a-e637-4c34-bc40-326c7fda8c7e2cf71c; _gcl_au=1.1.22788994.1682488852; _ga_RPSBE3TQZZ=deleted; __LOCALE__null=TW; csrftoken=ZY72QnQoGrfY90jGh2xOwtYpBMpkxECa; SPC_IA=1; SPC_SI=xWVsZAAAAABYRlFmTlI5Utn0hQEAAAAAN1NDbHN0TzE=; _gcl_aw=GCL.1685407887.Cj0KCQjwmtGjBhDhARIsAEqfDEeFMlO-HXhdAN0AVrVQPw7QmFNRArzI5YDLIj1lk-1odJO4OzF0wKwaAmVZEALw_wcB; _gid=GA1.2.1058371145.1685407889; _gac_UA-61915057-6=1.1685407889.Cj0KCQjwmtGjBhDhARIsAEqfDEeFMlO-HXhdAN0AVrVQPw7QmFNRArzI5YDLIj1lk-1odJO4OzF0wKwaAmVZEALw_wcB; _med=refer; SPC_SC_TK=a57acd0854b5a078647cf492c99b3269; SPC_SC_UD=3778846; SPC_STK=B8+EF6EmPqUkQGboZFa8f6lis9+d/IzAlwxESkyy//1OmzdHyvIn3QLFb0XjFb1FJi8MKcRHcq/LKDoRln8luCkosCkGaUeW5sEBxZlVag1frvj5R2bnePK+Mb0LCYv/wxUDgrq7XneulazbfXi2StDZhjvKV+lGLsnALdRJhxs=; _ga_JD9WKB3ZNL=GS1.1.1685432589.3.0.1685432589.60.0.0; SPC_U=3778846; SPC_R_T_ID=zZ9JCeAY2NmxxYxep9jRfLWmQ/QRqtLwoJkme51CnsDfoF19GcWPVu0VNQqcWG6YmgoN8K6jhf7B67DZiUW0Ahs122K39++lAtlxQi77MWZQKmo3OpkHZqJ7IPQjlZ7nvK3mUS3hqRMIWhTBvwZmn+jH2k3Qb3P9zR6OJhGSdpQ=; SPC_R_T_IV=N0haZm5vWXMyMndWVnZzQw==; SPC_T_ID=zZ9JCeAY2NmxxYxep9jRfLWmQ/QRqtLwoJkme51CnsDfoF19GcWPVu0VNQqcWG6YmgoN8K6jhf7B67DZiUW0Ahs122K39++lAtlxQi77MWZQKmo3OpkHZqJ7IPQjlZ7nvK3mUS3hqRMIWhTBvwZmn+jH2k3Qb3P9zR6OJhGSdpQ=; SPC_T_IV=N0haZm5vWXMyMndWVnZzQw==; _QPWSDCXHZQA=bced92e2-0082-4f78-d4e0-340006889f01; AMP_TOKEN=$NOT_FOUND; shopee_webUnique_ccd=o8NrDbgPAuRzG9pYhaPKNA==|C7pTz85mFFD2gq5CyCOFbO3/r8ahDOCk/ZbweD3hNYynoAocaQb4KBR+eS4W41sfXVMsPN2zPYpqHlHJsPznQotJSMy8FaXd2Qe1|s4/fLsXsyBPQ4dZY|06|3; ds=477e092b267930b2a38d343753c4a8b2; _ga=GA1.1.428565137.1674698101; _gali=stardust-popover1; _ga_RPSBE3TQZZ=GS1.1.1685515105.78.1.1685515779.60.0.0',
#     'set-cookies': 'SPC_R_T_IV=N0haZm5vWXMyMndWVnZzQw==; Path=/; Domain=.shopee.tw; Max-Age=630720000; Secure',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'x-api-source': 'pc',
#     'x-requested-with': 'XMLHttpRequest',
#     'cookies': 'SPC_F=DuZ3Phpl9b2SXzsi2zF1O43v4xo1fmVx; REC_T_ID=70ce7b47-9d1c-11ed-b6e4-d0946659d874; SPC_CLIENTID=RHVaM1BocGw5YjJTwbhlierpjluxhgmn; SC_DFP=UGYkdmgCUVmyeiSiOCDjJXEkYoTPYLSg; __stripe_mid=1cece67a-e637-4c34-bc40-326c7fda8c7e2cf71c; _gcl_au=1.1.22788994.1682488852; _ga_RPSBE3TQZZ=deleted; __LOCALE__null=TW; csrftoken=ZY72QnQoGrfY90jGh2xOwtYpBMpkxECa; SPC_IA=1; SPC_SI=xWVsZAAAAABYRlFmTlI5Utn0hQEAAAAAN1NDbHN0TzE=; _gcl_aw=GCL.1685407887.Cj0KCQjwmtGjBhDhARIsAEqfDEeFMlO-HXhdAN0AVrVQPw7QmFNRArzI5YDLIj1lk-1odJO4OzF0wKwaAmVZEALw_wcB; _gid=GA1.2.1058371145.1685407889; _gac_UA-61915057-6=1.1685407889.Cj0KCQjwmtGjBhDhARIsAEqfDEeFMlO-HXhdAN0AVrVQPw7QmFNRArzI5YDLIj1lk-1odJO4OzF0wKwaAmVZEALw_wcB; _med=refer; SPC_SC_TK=a57acd0854b5a078647cf492c99b3269; SPC_SC_UD=3778846; SPC_STK=B8+EF6EmPqUkQGboZFa8f6lis9+d/IzAlwxESkyy//1OmzdHyvIn3QLFb0XjFb1FJi8MKcRHcq/LKDoRln8luCkosCkGaUeW5sEBxZlVag1frvj5R2bnePK+Mb0LCYv/wxUDgrq7XneulazbfXi2StDZhjvKV+lGLsnALdRJhxs=; _ga_JD9WKB3ZNL=GS1.1.1685432589.3.0.1685432589.60.0.0; SPC_U=3778846; SPC_R_T_ID=zZ9JCeAY2NmxxYxep9jRfLWmQ/QRqtLwoJkme51CnsDfoF19GcWPVu0VNQqcWG6YmgoN8K6jhf7B67DZiUW0Ahs122K39++lAtlxQi77MWZQKmo3OpkHZqJ7IPQjlZ7nvK3mUS3hqRMIWhTBvwZmn+jH2k3Qb3P9zR6OJhGSdpQ=; SPC_R_T_IV=N0haZm5vWXMyMndWVnZzQw==; SPC_T_ID=zZ9JCeAY2NmxxYxep9jRfLWmQ/QRqtLwoJkme51CnsDfoF19GcWPVu0VNQqcWG6YmgoN8K6jhf7B67DZiUW0Ahs122K39++lAtlxQi77MWZQKmo3OpkHZqJ7IPQjlZ7nvK3mUS3hqRMIWhTBvwZmn+jH2k3Qb3P9zR6OJhGSdpQ=; SPC_T_IV=N0haZm5vWXMyMndWVnZzQw==; _QPWSDCXHZQA=bced92e2-0082-4f78-d4e0-340006889f01; AMP_TOKEN=$NOT_FOUND; shopee_webUnique_ccd=o8NrDbgPAuRzG9pYhaPKNA==|C7pTz85mFFD2gq5CyCOFbO3/r8ahDOCk/ZbweD3hNYynoAocaQb4KBR+eS4W41sfXVMsPN2zPYpqHlHJsPznQotJSMy8FaXd2Qe1|s4/fLsXsyBPQ4dZY|06|3; ds=477e092b267930b2a38d343753c4a8b2; _ga=GA1.1.428565137.1674698101; _gali=stardust-popover1; _ga_RPSBE3TQZZ=GS1.1.1685515105.78.1.1685515779.60.0.0'
# }    

# r = requests.get(shop_info_url, headers=headers)

# data = r.json()

# print(data)

#print(data['items'][0].keys())

# for item in data['items']:
#     print('name:', item['name'])
#     print('prince:', item['price'])
#     print('sold:', item['historical_sold'])
#     print('---')

# https://shopee.tw/api/v4/shop/get_shop_detail?shopid=6130784
# https://shopee.tw/api/v4/shop/search_items?limit=100&offset=0&order=desc&shopid=6130784
# 113.0.1774.57
