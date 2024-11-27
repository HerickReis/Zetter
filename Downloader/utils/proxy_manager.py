import sys

import random
import requests
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils.paths_manipulation import verificar_arquivo

class ProxyManager:
    def __init__(self, proxy_list):
        self.proxy_list = proxy_list

    def get_random_proxy(self):
        return random.choice(self.proxy_list)

    def request_new_proxies(proxy_list_url):
         with open(verificar_arquivo(nome_arquivo="proxies.txt",diretorio_raiz=r"..\Zetter\Downloader", criar_arquivo=True), "w") as proxy:
            r =  requests.get(proxy_list_url)
            proxy.write(r.text)

ProxyManager.request_new_proxies(proxy_list_url="https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=text")
