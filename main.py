from scans import brute_force, port_scanning
from reporting import report_generator
from utils.functions import display_banner

from colorama import Fore, Back, Style
import time

def main():
    display_banner()

    print("Web Pwn'e Hoşgeldiniz. Yapmak istediğiniz işlemi seçiniz.")

    print(Fore.YELLOW, """

    1 - Port Tarama (Port Scanning)
    2 - Zafiyet Taraması (Vulnerability Scanning)
    3 - Brute Force
    4 - Ağ Trafik Analizi
    
    """, Style.RESET_ALL)

    while True:
        islem = str(input())

        if islem == "1":
            port_scanning.port_scanning()
        
        elif islem == "2":
            pass

        elif islem == "3":
            pass

        elif islem == "4":
            pass

        else:
            print(Fore.RED, "Lütfen geçerli bir değer girip tekrar deneyin.", Style.RESET_ALL)
    

if __name__ == "__main__":
    main()