import requests


def download(page: int, filepath: str = "./JsonDownload") -> None:
    url = (f"https://www.uaa.com/api/novel/app/novel/search?category="
           f"&excludeTags=&orderType=2&page={page}&searchType"
           f"=1&size=40")
    res = requests.get(url)
    print(res.text)
    if res.status_code == 200:
        print(f"{page} 获取成功")
        with open(filepath + f"/Page{page}.json", encoding="utf-8", mode="w") as file:
            file.write(res.text)
    else:
        print(f"{page} 获取失败")
