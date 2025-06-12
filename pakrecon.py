
import phonenumbers
import requests
import json
import re
from bs4 import BeautifulSoup
from phonenumbers import geocoder, carrier

def validate_number(number):
    try:
        parsed = phonenumbers.parse(number, "PK")
        if not phonenumbers.is_valid_number(parsed):
            return None
        return parsed
    except:
        return None

def get_carrier_and_region(parsed_number):
    sim_carrier = carrier.name_for_number(parsed_number, "en")
    region = geocoder.description_for_number(parsed_number, "en")
    return sim_carrier, region

def check_gmail(number):
    headers = {
        "Content-Type": "application/json"
    }
    # Google account recovery check (simulate)
    # Real check would require scraping and is sensitive to changes
    if number.startswith("+92"):
        return "Possible Gmail association (based on format)"
    return "Unknown"

def check_whatsapp(number):
    url = f"https://wa.me/{number.replace('+', '')}"
    try:
        r = requests.get(url)
        if "WhatsApp" in r.text:
            return True
    except:
        pass
    return False

def google_dork_search(number):
    query = f'"{number}" site:pastebin.com OR site:github.com OR site:facebook.com'
    return f"https://www.google.com/search?q={requests.utils.quote(query)}"

def main():
    target = input("Enter Pakistani phone number (e.g., +923001234567): ").strip()
    parsed_number = validate_number(target)
    if not parsed_number:
        print("[!] Invalid Pakistani number.")
        return

    print("[+] Valid number.")
    sim_carrier, region = get_carrier_and_region(parsed_number)
    print(f"[+] Carrier: {sim_carrier}")
    print(f"[+] Region: {region}")

    gmail_status = check_gmail(target)
    print(f"[+] Gmail: {gmail_status}")

    is_on_whatsapp = check_whatsapp(target)
    print(f"[+] WhatsApp: {'Yes' if is_on_whatsapp else 'No or Unknown'}")

    google_dork = google_dork_search(target)
    print(f"[+] Google Dork Search URL:
    {google_dork}")

    result = {
        "number": target,
        "carrier": sim_carrier,
        "region": region,
        "gmail_association": gmail_status,
        "whatsapp": is_on_whatsapp,
        "google_dork_url": google_dork
    }

    with open("pakrecon_report.json", "w") as f:
        json.dump(result, f, indent=4)
    print("[+] Report saved to pakrecon_report.json")

if __name__ == "__main__":
    main()
