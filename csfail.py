import requests
import threading
import random
import json

def f():
    test_list = config["test_list"]
    token = config['token']
    token_prof = config['token_prof']
    version = 5.131
    domain = config["domain_group"]
    idgruppy = config["id_group"]
    massage = "абоба"
    i = 0

    respons = requests.get("https://api.vk.com/method/wall.get",
                           params={
                               "access_token": token,
                               "v": version,
                               "domain": domain
                           }
                           )
    data = respons.json()["response"]["items"][0o0]["id"]
    zak = respons.json()["response"]["items"][0o0]
    if "is_pinned" in zak:
        respons = requests.get("https://api.vk.com/method/wall.get",
                               params={
                                   "access_token": token,
                                   "v": version,
                                   "domain": domain
                               }
                               )
        data = respons.json()["response"]["items"][0o1]["id"]
    proverka = data
    while i<100:
        massage = random.choice(test_list)
        if proverka == data:
            respons = requests.get("https://api.vk.com/method/wall.get",
                                params={
                                    "access_token": token,
                                    "v": version,
                                    "domain": domain
                                }
                                )
            data = respons.json()["response"]["items"][0o1]["id"]
        else:
            proverka = data
            i+=1
            token_tg = "5064919937:AAHY8Kk7NsBfWOMsPuHPcQfFKpqY8MYH2JQ"
            chat_id = "825524132"
            text_tg = respons.json()["response"]["items"][0o1]["text"]
            url_req = "https://api.telegram.org/bot" + token_tg + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text_tg
            results = requests.get(url_req)

while True:
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    try:
        f()
    except:
        token_tg = "5064919937:AAHY8Kk7NsBfWOMsPuHPcQfFKpqY8MYH2JQ"
        chat_id = "825524132"
        text_tg = "перезапуск"
        url_req = "https://api.telegram.org/bot" + token_tg + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text_tg
        results = requests.get(url_req)