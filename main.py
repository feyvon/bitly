import os
from urllib.parse import urlparse
from dotenv import load_dotenv

import argparse
import requests



def shorten_link(token, link):
    url = "https://api-ssl.bitly.com/v4/shorten"
    print(link)
    headers = {
        "Authorization": "Bearer {}".format(token)
 }

    parametrs = {
        "long_url" : link
 }

    response = requests.post(url, headers = headers, json = parametrs)
    response.raise_for_status()
    bitlink = response.json()['link']
    return bitlink


def count_clicks(link, token):
    link = urlparse(link)
    bitlink = f"{link.netloc}{link.path}"
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    headers = {
        "Authorization": "Bearer {}".format(token)
 }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(link, token):
    link = urlparse(link)
    bitlink = f"{link.netloc}{link.path}"
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    headers = {
        "Authorization": "Bearer {}".format(token)
 }
    response = requests.get(url, headers = headers)
    return response.ok


def main():
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')
    parser = argparse.ArgumentParser(description='Выдает битлинк на указанную ссылку и показывает кол-во кликов на битлинк')
    parser.add_argument('link', help='Ваша ссылка')
    args = parser.parse_args()
    
    try:
        if is_bitlink(args.link, token):
            print("Количество кликов: ", count_clicks(args.link, token))
        else:
            print("Короткая ссылка: ", shorten_link(token, args.link))
    except requests.exceptions.HTTPError:
        print("Ссылка неправильная")


if __name__ == '__main__':
    main()