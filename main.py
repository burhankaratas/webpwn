from scans import brute_force, port_scanning, url_parsing
from utils.functions import display_banner, clear

from colorama import Fore, Back, Style
import time

def main():
    display_banner()

    print("Web Pwn'e Hoşgeldiniz. Yapmak istediğiniz işlemi seçiniz.")

    while True:
        print(Fore.YELLOW, """

        1 - Port Tarama (TCP)
        2 - Brute Force
        3 - URL çözümleme

        """, Style.RESET_ALL)
        
        islem = str(input())

        if islem == "1":
            port_scanning.port_scanning()

        elif islem == "2":
            brute_force.run_brute_force()

        elif islem == "3":
            url_parsing.url_parsing()

        elif islem == "clear":
            clear()

        else:
            print(Fore.RED, "Lütfen geçerli bir değer girip tekrar deneyin.", Style.RESET_ALL)
    

if __name__ == "__main__":
    main()