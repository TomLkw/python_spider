# -*- coding: utf-8 -*-
import requests
import json

def print_conten_test() :
    url = "https://m.weibo.cn/api/container/getIndex"
    querystring = {"uid": "1961640291", "t": "0", "luicode": "10000011", "lfid": "100103type=1&q=褚明宇", "type": "uid",
                   "value": "1961640291", "containerid": "1076031961640291"}

    headers = {
        'cache-control': "no-cache",
        'postman-token': "556a1283-b3b0-4595-f222-e04bb5f0b45a"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.status_code)
    res = response.text
    # print(res);
    json_res = json.loads(res)
    # print(json_res);
    # print(type(json_res));

    resCards = json_res['data']['cards']
    for card in resCards:
        print(card['card_type'])
        print(card['mblog']['pic_num']>1)
        try:
            print(card['mblog']['raw_text'])
        except KeyError:
            print('raw text is null')
        try:
            print(card['mblog']['retweeted_status'])
        except KeyError:
            print('retweeted is null')
        print(card['mblog']['isLongText'])
    print('----------------')
    # print(resCards[0])

    # testArray = re.findall("text",resText)
    # print(len(testArray))


if __name__ == '__main__':
    print_conten_test()
