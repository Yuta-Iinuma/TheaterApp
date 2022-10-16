# ライブラリのインポート
import requests
from bs4 import BeautifulSoup
import time
import datetime
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Webdriverの初期設定
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')
options.add_argument('--start-maximized')
options.add_argument('--headless')
session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
}

# スクレイピングサイトのURL指定
target_url = 'https://www.cinemasunshine.co.jp/movie/'

# driverの立ち上げ
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(target_url)

# ページ更新待ち
WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located)
time.sleep(3)

# URLリンク先のhtml抽出
html = driver.page_source
time.sleep(1)
soup = BeautifulSoup(html, "html.parser")

# ポスター画像を保持するdivのセクションを抽出
img_class_list = soup.find_all(class_='movie-image')


img_name_list = []
output_folder_path = './storetest/'

for i in range(len(img_class_list)):
    #     作品名の取得
    title_name = img_class_list[i].find('img').get('alt')

    #    同じ作品のポスターを複数DLしないように条件分岐
    if title_name not in img_name_list:
        img_name_list.append(title_name)

        # 保存先、画像名の指定
        save_path = output_folder_path + title_name + '.jpeg'

        try:
            # 画像のDL
            img_src = img_class_list[i].find('img').get('src')
            image = session.get(img_src, headers=headers)
            open(save_path, 'wb').write(image.content)
            time.sleep(3)

        except ValueError:
            #  DL失敗した時の通知
            print('ValueError')
            print(title_name)
