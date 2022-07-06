# 02/27/22
import requests
import bs4
import os
import random
from bs4 import BeautifulSoup
rks = ''
os.system("clear")
count = 0
target = input(" [*] mbasic reaction url: ")
os.system('clear')
print('''\33[1;92m[ \33[1;91m::REACTIONS:: \33[1;92m]\33[1;96m
[1] Love.
[2] Care.
[3] Haha.
[5] Wow.
[6] Sad.
[7] Angry.
[8] Like.
[9] Love, Care.
[10] Love, Care, Like.

[0] Exit.''')
rtc = input("[?]: ")
if rtc == 0:
        exit()
elif rtc == '1':
        rks = 'reaction_type=2'
elif rtc == '2':
        rks = 'reaction_type=16'
elif rtc == '3':
        rks = 'reaction_type=4'
elif rtc == '4':
        rks = 'reaction_type=3'
elif rtc == '5':
        rks = 'reaction_type=0'
elif rtc == '6':
        rks = 'reaction_type=7'
elif rtc == '7':
        rks = 'reaction_type=1'
else:
        print('[*] Invalid Option.')

with open("cookie.txt", 'r') as fp:
    num_lines = sum(1 for line in fp)
    print('[*] Total Bots: ', num_lines)
    print()
cookie = open('cookie.txt', 'r').readlines()
for cook in cookie:
    rksd = random.choice(['reaction_type=2', 'reaction_type=4','reaction_type=16'])
    cookies = cook.strip()
    headers = {
        'authority': 'mbasic.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; V2102) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.60 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookies,
    }
    profile = requests.get('https://mbasic.facebook.com/profile.php', headers=headers).text
    user = BeautifulSoup(profile, 'lxml')
    name = user.title.text
#    first, *middle, last = user.title.text.split()
    if name in ['Page Not Found', 'Login to Facebook', 'Hindi Natagpuan ang Pahina']:
        print('[Wrong cookie]')

    elif name in ['Checkpoint', 'locked', 'Security Checkpoint']:
        print('[ Account Checkpoint ]')

    elif name in ['Log into Facebook | Facebook', 'Log into Facebook', 'Login approval needed']:
        print("[ Current Bot: \33[1;91mCheckpoint :)\33[0m ]")
    else:
        print("\33[1;92m[ Current Bot: \33[1;91m"+name+"\33[1;92m ]")
        url = requests.get(target, headers=headers).text
        parser = BeautifulSoup(url, "lxml")
        tag = parser.find_all('a', href=True)
        for reactions in tag:
            reactme = reactions['href']
            rbs = "reaction_type=4"
            if rbs in reactme:
                requests.get('https://mbasic.facebook.com'+reactme, headers=headers)
                count += 1
                print("\33[1;92m[ RECTIONS:"+str(count)+" ] \33[1;91m=> \33[1;93mreact success.\33[0m")