# 📱 PakRecon – Pakistan Phone Number OSINT Tool

**PakRecon** is a powerful open-source intelligence (OSINT) tool built for investigating **Pakistani phone numbers**. It gathers public and passive data about a given number, including carrier information, region, WhatsApp presence, Google association, and more — all from public sources.

---

## 🚀 Features

- ✅ Validates if the number is a valid Pakistani mobile number
- 📡 Detects the SIM carrier (Jazz, Zong, Telenor, Ufone, etc.)
- 🗺️ Estimates region/location of the number
- 📧 Checks for potential Gmail/Google account association
- 📱 Detects WhatsApp usage based on number activity
- 🔍 Generates Google Dorks to find leaked data or mentions (Pastebin, Facebook, GitHub)
- 💾 Saves all results in a clean `pakrecon_report.json` file

---

## 🛠 Installation

### Requirements

- Python 3.7+
- The following Python packages:

```bash
pip install phonenumbers requests beautifulsoup4
[+] Valid number.
[+] Carrier: Jazz
[+] Region: Lahore
[+] Gmail: Possible Gmail association (based on format)
[+] WhatsApp: Yes
[+] Google Dork Search URL:
    https://www.google.com/search?q="%2B923001234567"+site%3Apastebin.com+OR+site%3Afacebook.com
[+] Report saved to pakrecon_report.json
