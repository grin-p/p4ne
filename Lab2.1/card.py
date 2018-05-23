import requests
import pprint
import json
import sys
import argparse
import random


URL = "https://lookup.binlist.net/45498765"

card_list=[]
card_list.append('45498765')
i=1
for i<10:
    card_list.append(random.randintinit(1000,9999))


# parser = argparse.ArgumentParser()
# parser.add_argument("list", nargs="*")
# args = parser.parse_args()
# card_list=args.list


for c_cardnum in card_list:
    c_URL = 'https://lookup.binlist.net/'+str(c_cardnum)
    r=requests.get(c_URL, headers={'Accept-Version': "3"})
    pprint.pprint(r.json())
    responce = r.json()
    bank_name=responce['bank']['name']
    print(bank_name)



