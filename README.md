# 🌐 Free Proxy List (Auto-Updated)

![Update Frequency](https://img.shields.io/badge/Update-Every%202%20Hours-blue?style=flat-square&logo=clock)
![Proxy Types](https://img.shields.io/badge/Protocols-HTTP%20%7C%20SOCKS4%20%7C%20SOCKS5-orange?style=flat-square)
![Build Status](https://github.com/[YOUR_USERNAME]/[YOUR_REPO_NAME]/actions/workflows/update_proxies.yml/badge.svg)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

> A completely automated, free proxy list repository. Scraped from public sources, validated, and updated every 2 hours via GitHub Actions.

---

## 🚀 Features

* **Automated Updates:** The list is refreshed every **2 hours** automatically.
* **Multiple Protocols:** Includes HTTP, SOCKS4, and SOCKS5 proxies.
* **Clean Format:** Proxies are saved in `IP:PORT` format, ready to use in any software.
* **High Availability:** Hosted on GitHub, ensuring fast and reliable access to the raw text files.

---

## 📥 Download / Usage

You can use the **Raw** links below to integrate these lists directly into your software, bots, or scripts.

| Protocol | Status | Raw Link (Click to Copy) |
| :--- | :---: | :--- |
| **HTTP** | 🟢 Active | `https://raw.githubusercontent.com/[YOUR_USERNAME]/[YOUR_REPO_NAME]/main/proxies/http.txt` |
| **SOCKS4** | 🟢 Active | `https://raw.githubusercontent.com/[YOUR_USERNAME]/[YOUR_REPO_NAME]/main/proxies/socks4.txt` |
| **SOCKS5** | 🟢 Active | `https://raw.githubusercontent.com/[YOUR_USERNAME]/[YOUR_REPO_NAME]/main/proxies/socks5.txt` |

### 💻 Example Usage (Python)

```python
import requests

url = "[https://raw.githubusercontent.com/](https://raw.githubusercontent.com/)[YOUR_USERNAME]/[YOUR_REPO_NAME]/main/proxies/http.txt"
proxies = requests.get(url).text.split("\n")

print(f"Loaded {len(proxies)} proxies.")
🛠️ How It Works
Scraping: The scraper.py script collects public proxies from various open-source API endpoints and repositories.

Filtering: It deduplicates the list and separates them by protocol.

Automation: A GitHub Action triggers the script every 2 hours (Cron: 0 */2 * * *).

Deployment: The updated lists are automatically committed and pushed to this repository.

⚠️ Disclaimer
This repository is for educational and research purposes only.

The proxies listed here are gathered from public sources widely available on the internet.

I do not own, operate, or control any of these proxy servers.

Please use these proxies responsibly. Do not use them for illegal activities, spamming, or attacking targets.

The reliability/uptime of these free proxies is not guaranteed.

🤝 Contributing
Feel free to fork this repository and submit a Pull Request if you want to add more proxy sources to the scraper.py file!

Fork the Project

Create your Feature Branch (git checkout -b feature/NewSources)

Commit your Changes (git commit -m 'Add new proxy sources')

Push to the Branch (git push origin feature/NewSources)

Open a Pull Request

<p align="center"> Made with ❤️ using Python & GitHub Actions </p>


### Yapman Gereken Düzenlemeler:

1.  **URL Değişimi:** Koddaki `[YOUR_USERNAME]` ve `[YOUR_REPO_NAME]` kısımlarını mutlaka değiştir (Örn: `tugcan/proxy-list` gibi).
2.  **Dosya Yolu:** Eğer dosyaların `proxies/` klasörü yerine ana dizinde duruyorsa linklerdeki `/proxies/` kısmını silmen gerekebilir. (Ama benim verdiğim kodda `proxies/` klasörü altına kaydediyordu, o yüzden bu hali doğru.)

**Senin için bir sonraki adım:**
Bu `README.md` dosyasını oluşturduktan sonra, projenin daha güvenilir görünmesi için bir de `LICENSE
