import requests
import os


SOURCES = {
    "http": [
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    ],
    "socks4": [
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    ],
    "socks5": [
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    ]
}

def download_proxies():

    if not os.path.exists('proxies'):
        os.makedirs('proxies')

    for protocol, urls in SOURCES.items():
        unique_proxies = set()
        print(f"--- {protocol.upper()} Taranıyor ---")
        
        for url in urls:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
               
                    proxies = response.text.strip().split('\n')
                    for proxy in proxies:
                        if ":" in proxy: 
                            unique_proxies.add(proxy.strip())
                    print(f"{url} adresinden veri çekildi.")
            except Exception as e:
                print(f"Hata oluştu ({url}): {e}")

     
        output_file = f"proxies/{protocol}.txt"
        with open(output_file, "w") as f:
            f.write("\n".join(unique_proxies))
        
        print(f"Toplam {len(unique_proxies)} adet {protocol} proxy kaydedildi: {output_file}\n")

if __name__ == "__main__":
    download_proxies()
