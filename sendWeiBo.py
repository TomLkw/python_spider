# -*- coding: utf-8 -*-
import requests
import re
import json
url = "https://m.weibo.cn/api/container/getIndex"

querystring = {"uid":"1961640291","t":"0","luicode":"10000011","lfid":"100103type=1&q=褚明宇","type":"uid","value":"1961640291","containerid":"1076031961640291"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "556a1283-b3b0-4595-f222-e04bb5f0b45a"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

res = response.text
# print(res);
json_res=json.loads(res)
print(json_res);
print(type(json_res));

resCards = json_res['data']['cards']
for card in resCards :
    card['pic_num']
    try:
        print(card['mblog']['raw_text'])
    except KeyError:
        print('null')
        # print(card['mblog']['text'])

print('----------------')
print(resCards[0])



# testArray = re.findall("text",resText)
# print(len(testArray))

