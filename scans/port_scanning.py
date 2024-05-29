from colorama import Fore, Back, Style

def port_scanning():
    print(Fore.CYAN, "\n Hedef ip adresini veya url sini giriniz:", Style.RESET_ALL)

    while True:
        ip_url = str(input())