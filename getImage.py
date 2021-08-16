import requests
import os

def download_img(img_url, api_token):
    print (os.getcwd())
    # print (img_url)
    header = {"Authorization": "Bearer " + api_token} # 设置http header，视情况加需要的条目，这里的token是用来鉴权的一种方式
    r = requests.get(img_url, headers=header, stream=True)
    print(r.status_code) # 返回状态码
    if r.status_code == 200:
        open(os.getcwd()+'\images\\img.png', 'wb').write(r.content) # 将内容写入图片
        print("done")
    del r

if __name__ == '__main__':
    # 下载要的图片
    img_url = "https://tva3.sinaimg.cn/crop.0.0.1080.1080.180/74ec4163jw8entvhp354mj20u00u0n4u.jpg?KID=imgbed,tva&Expires=1629027581&ssig=EjHP4clGEf"
    api_token = "fklasjfljasdlkfjlasjflasjfljhasdljflsdjflkjsadljfljsda"
    download_img(img_url, api_token)