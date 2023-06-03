from statistics import mode
import requests
import time # prevent dos attack detection
from datetime import datetime

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68",
    "x-api-source": "pc"
}

limit = 100
offset = 0
total = 0
shopid = "6130784"
session = requests.Session()
fn = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
out = open(fn + '.txt', 'w', encoding='UTF-8')

def is_chinese(uchar):
    return True if (uchar >= "\u4e00" and uchar <= "\u9fa5") else False


def align(text, width, just="left"):
    stext = str(text)
    utext = stext
    # utext = stext.decode("utf-8")  # Transcoding the string
    cn_count = 0

    for u in utext:
        cn_count += 2 if is_chinese(u) else 1
    if just == "right":
        return " " * (width - cn_count) + stext
    elif just == "left":
        return stext + " " * (width - cn_count)


def string_ljust(text, width):
    return align(text, width, "left")


def string_rjust(text, width):
    return align(text, width, "right")


def getItemsListUrl(shopid: str) -> str:
    return f"https://shopee.tw/api/v4/recommend/recommend?bundle=shop_page_category_tab_main&item_card=2&limit={limit}&offset={offset}&section=shop_page_category_tab_main_sec&shopid={shopid}&sort_type=1&tab_name=popular"


def getModelDetails(shopid: str, itemid: str) -> str:
    url = f"https://shopee.tw/api/v4/item/get?itemid={itemid}&shopid={shopid}"
    r = session.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        return r.json()["data"]["models"]
    else:
        raise ValueError(f"Error request with: {url}")
    


if __name__ == "__main__":

    while True:
        url = getItemsListUrl(shopid)
        r = session.get(url, headers=headers)
        if r.status_code == requests.codes.ok:
            data = r.json()
            print(data)
            # if offset == 0:
            #     total = data["data"]["sections"][0]["total"]
            #     print(f"賣場總商品數: {total}", file=out)   

            # items = data["data"]["sections"][0]["data"]["item"]
            # total -= len(items)
        #     for item in items:
        #         itemid = item["itemid"]
        #         print(f"{'-'*100}", file=out)
        #         print(f"{'商品    '}| {item['name']}", file=out)
        #         print(f"{'當前折扣'}| {item['discount']}", file=out)
                
        #         models = getModelDetails(shopid, itemid)
        #         for model in models:
        #             name = string_ljust(model['name'], 30)
        #             print(f"{'子商品  '}| {name}| 價格 {int(model['price'])/100_000:6}$ | 庫存 {model['normal_stock']:2}", file=out)
        #             time.sleep(0.05)
        #         time.sleep(0.2)

        #     # 檢查剩餘商品數量
        #     if total <= 0:
        #         print("Done!")
        #         break
        #     else:
        #         offset += limit
        #     time.sleep(1)
