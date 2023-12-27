import re
import random
from time import sleep as sp
import requests as ses
from os import system as logo

class GetRandomUserAgent:

    def __init__(self):
        self.url = "https://www.useragentstring.com/pages/useragentstring.php"
        self.dalvikurl = "https://www.useragentstring.com/pages/useragentstring.php?name=Android"
        self.mysave = "user_agents.txt"
        self.total = []

    def get_RandomUa(self, limit, sav):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        iAmWriting = open(sav,"a")
        iAmWriting.write(f'dani_random_ua = random.choice([')
        try:
            iAmGettingData = ses.get(url=self.url, headers=headers).text
            for wAreRandomUserAgents in re.findall('href\=\"/string/(.*?)">(.*?)<',iAmGettingData):
                self.total.append(wAreRandomUserAgents[1])
                iAmWriting.write(f'"{wAreRandomUserAgents[1]}",')
                sys.stdout.write(f"\r [•] Getting UA: [{len(self.total)}] ");sys.stdout.flush();sp(0.009)
                print(f"Generated User Agent: {wAreRandomUserAgents[1]}") # Added this line to print the generated user agent
        except ConnectionError:
            print(f" [•] Please Check Your Internet Connection ..")
            exit()
        iAmWriting.write("])")
