from utils.functions import clear

import socket
from colorama import Fore, Style

def url_parsing():
    clear()

    print(Fore.CYAN, "Hedef URL'yi girin: ", Style.RESET_ALL)
    url = input("https://")
    ip = resolve_url(url)
    if ip:
        print(f"{url} çözümlendi, IP adresi: {ip}")
    else:
        return
    
def resolve_url(url):
    try:
        ip = socket.gethostbyname(url)
        return ip
    except socket.gaierror:
        print("URL çözümlenirken bir hata oluştu.")
        return None