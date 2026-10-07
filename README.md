# Webpwn

> Python ile yazılmış, konsol tabanlı çok amaçlı ağ güvenliği aracı.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Lisans](https://img.shields.io/badge/license-MIT-green)

Webpwn; temel ağ güvenliği testlerini tek bir konsol arayüzünde toplar.
Eğitim, laboratuvar ve yetkili sızma testleri için tasarlanmıştır.

## Özellikler

- **TCP port taraması** — hedefteki açık portları tarar.
- **URL çözümleme** — bir URL'yi çözümleyip IP adresini gösterir.
- **Brute force** — sözlük tabanlı deneme modülü.

## Kurulum

Gereksinim: **Python 3.10+**

```bash
git clone https://github.com/burhankaratas/webpwn.git
cd webpwn
pip install -r requirements.txt
python main.py
```

Çalıştırınca menüden yapmak istediğiniz işlemi seçersiniz:

```
1 - Port Tarama (TCP)
2 - Brute Force
3 - URL Çözümleme
```

## Dizin Yapısı

```
webpwn/
├── main.py                    # Menü ve giriş noktası
├── scans/
│   ├── port_scanning.py       # TCP port taraması
│   ├── brute_force.py         # Sözlük tabanlı deneme
│   └── url_parsing.py         # URL → IP çözümleme
└── utils/
    ├── functions.py           # Banner, temizleme vb.
    └── wordlists/passwords.txt
```

## ⚠️ Yasal Uyarı

Bu araç **yalnızca sahibi olduğunuz sistemlerde veya açıkça izin verilmiş
hedeflerde** kullanılmalıdır. İzinsiz sistemlere yönelik kullanım yasa dışıdır
ve geliştirici hiçbir sorumluluk kabul etmez. Yalnızca eğitim ve yetkili
güvenlik testleri içindir.

## Lisans

[MIT](LICENSE) © 2026 Mahmut Burhan Karataş