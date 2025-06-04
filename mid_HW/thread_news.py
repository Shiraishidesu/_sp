import requests
from bs4 import BeautifulSoup
import threading

# 模擬瀏覽器 headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# 想要爬的網址列表（可自行添加）
urls = [
    "https://tw.news.yahoo.com/world/",
    "https://tw.news.yahoo.com/archive/",
    "https://tw.news.yahoo.com/entertainment/"
]

# 執行緒鎖，避免多執行緒同時 print 出錯亂
# 只允許一次一個thread使用print
lock = threading.Lock()

# 爬蟲的部分
def fetch_keywords(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # 200 是請求成功
            soup = BeautifulSoup(response.text, "html.parser")
            # keywords = soup.find_all("svg", class_="a")
            titles = soup.find_all("h3")

            with lock:
            # 這個with自動上鎖和解鎖，一次只允許一個thread使用print
                print(f"\n 來自：{url}")
                for i, kw in enumerate(titles[:5], start=1): # 爬五筆
                    print(f"{i}. {kw.text.strip()}")
        else:
            with lock:
             # 這個with自動上鎖和解鎖，一次只允許一個thread使用print
                print(f"無法抓取 {url}，狀態碼：{response.status_code}")
    except Exception as e:
        with lock:
         # 這個with自動上鎖和解鎖，一次只允許一個thread使用print
            print(f"抓取 {url} 發生錯誤：{e}")

# 建立並啟動執行緒
threads = []
for url in urls:
    t = threading.Thread(target=fetch_keywords, args=(url,))
    t.start()
    threads.append(t)

# 等待所有執行緒完成
for t in threads:
    t.join()

print("\n網頁爬取完畢。")
