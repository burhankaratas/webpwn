from scans import brute_force, port_scanning, url_parsing
from reporting import report_generator
from utils.functions import display_banner

from colorama import Fore, Back, Style
import time

def main():
    display_banner()

    print("Web Pwn'e Hoşgeldiniz. Yapmak istediğiniz işlemi seçiniz.")

    while True:
        print(Fore.YELLOW, """

        1 - Port Tarama (TCP)
        2 - Zafiyet Taraması (Vulnerability Scanning)
        3 - Brute Force
        4 - Ağ Trafik Analizi
        5 - URL çözümleme

        """, Style.RESET_ALL)
        
        islem = str(input())

        if islem == "1":
            port_scanning.port_scanning()
        
        elif islem == "2":
            pass

        elif islem == "3":
            pass

        elif islem == "4":
            pass

        elif islem == "5":
            url_parsing.url_parsing()

        else:
            print(Fore.RED, "Lütfen geçerli bir değer girip tekrar deneyin.", Style.RESET_ALL)
    

if __name__ == "__main__":
    main()