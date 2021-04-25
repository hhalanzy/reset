import requests
user = open('users.txt','r').read().splitlines()
def login ():
    headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '82',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=NaWgrRiEeItTH2eHNf8BC1jmdd5n7lWp; mid=YIS-KwALAAG7W1zpcFUSFyOG4Zl7; ig_did=6AFC6A3D-C72C-4FAD-BF75-FA63C302D4F4; ig_nrcb=1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/password/reset/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'x-csrftoken':'NaWgrRiEeItTH2eHNf8BC1jmdd5n7lWp',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '822bad258fea',
    'x-requested-with': 'XMLHttpRequest'

    }
    data = {
    'email_or_username': user,
    }
    req = requests.post('https://www.instagram.com/accounts/account_recovery_send_ajax/' , headers=headers ,data=data).text

    print(req, file=open("output.txt","a"))

login()




