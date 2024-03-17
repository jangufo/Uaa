import requests
import random
from time import sleep

# 下载错误的页码
err_page_collection: [int] = []


def download(page: int, filepath: str = "./JsonDownload") -> None:
    url = (f'https://www.uaa.com/api/novel/app/novel/search?category='
           f'&excludeTags=&orderType=2&page={page}&searchType'
           f'=1&size=40')
    try:
        res = requests.get(url)
    # 连接异常
    except requests.exceptions.ConnectionError:
        err_page_collection.append(page)
        print("Connection")
    # http的异常
    except requests.exceptions.HTTPError:
        err_page_collection.append(page)
        print("HTTPError")
    else:
        if res.status_code == 200:
            print(f"{page} 获取成功")
            fp = filepath + f"/Page{page}.json"
            write_json_file(fp, res.text)
        else:
            # 暂时未想到什么情况会来到这个分支
            # 规避了异常检查却返回状态码不是200
            # 但是还是添加了这个分支(保证程序健壮性
            print(f"{page} code is not 200")


def get_total_page() -> int:
    url = (f"https://www.uaa.com/api/novel/app/novel/search?category="
           f"&excludeTags=&orderType=2&page=1&searchType"
           f"=1&size=40")
    res = requests.get(url)
    write_json_file("./JsonDownload/Page1.json", res.text)
    return res.json()["model"]["totalPage"]


# 外部下载使用的方法
def download_all():
    page = get_total_page()
    for page in range(2, page + 1):
        download(page)
        # 正常休息 1-4 秒
        sleep(random.randint(1, 4))

    # 在正常下载完对下载失败的进行重试
    for err_page in err_page_collection:
        download(err_page)
        sleep(random.randint(1, 4))


def write_json_file(filepath: str, json_str: str) -> None:
    with open(filepath, encoding="utf-8", mode="w") as file:
        file.write(json_str)
