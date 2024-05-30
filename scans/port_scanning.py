from colorama import Fore, Style
import socket
import os

from utils.functions import clear

def port_scanning():
    clear()

    print(Fore.CYAN, "\n Hedef ip adresini girin:", Style.RESET_ALL)
    ip_url = str(input())
    
    clear()
    print(Fore.CYAN, "Taramak istediğiniz portu girin:", Style.RESET_ALL)

    port = int(input())

    clear()

    result = tcp_port_scan(ip_url, port)

    if result == True or result == False:
        print("Farklı bir portu kontrol etmek için lütfen 1' e basın")

    else:
        print("Farklı bir portu kontrol etmek için lütfen 1' e basın")


def tcp_port_scan(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(Fore.GREEN, f"Port {port}: Açık", Style.RESET_ALL)
            sock.close()
            return True
        else:
            print(Fore.RED, f"Port {port}: Kapalı", Style.RESET_ALL)
            sock.close()
            return False

    except Exception as e:
        print(f"Hata oluştu: {e}")