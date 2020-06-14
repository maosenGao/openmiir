import requests
from bs4 import BeautifulSoup
import lxml
import urllib
import os

BASE_PAGE_URL = 'http://www.doutula.com/article/list/?page='
PAGE_URL_LIST = []

for x in range(1, 2):
    url = BASE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)


def download_img(url):
    split_list = url.split('/')
    filename = split_list.pop()
    image_path = 'images'
    if image_path not in os.listdir():
        os.makedirs(image_path)
    path = os.path.join('images', filename)
    urllib.request.urlretrieve(url, filename=path)


def get_page(page_url):
    headers = {
        'Host': 'www.doutula.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    res = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    img_list = soup.find_all('img', attrs={'class': 'lazy image_dtb img-responsive'})
    for img in img_list:
        url = img['data-original']
        download_img(url)


def main():
    for page_url in PAGE_URL_LIST:
        get_page(page_url)


if __name__ == '__main__':
    main()
