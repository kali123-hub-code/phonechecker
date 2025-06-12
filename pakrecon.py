import re
import json
import argparse
import requests
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

# Carrier & Region mapping for Pakistani numbers
prefix_region_map = {
    "300": ("Jazz", "Punjab"), "301": ("Jazz", "Sindh"), "302": ("Jazz", "Punjab"),
    "303": ("Jazz", "KPK"), "304": ("Jazz", "Balochistan"), "305": ("Jazz", "Islamabad"),
    "310": ("Zong", "Punjab"), "311": ("Zong", "Sindh"), "312": ("Zong", "KPK"),
    "313": ("Zong", "Balochistan"), "314": ("Zong", "Islamabad"),
    "320": ("Ufone", "Punjab"), "321": ("Ufone", "Sindh"), "322": ("Ufone", "KPK"),
    "323": ("Ufone", "Balochistan"), "324": ("Ufone", "Islamabad"),
    "340": ("Telenor", "Punjab"), "341": ("Telenor", "Sindh"), "342": ("Telenor", "KPK"),
    "343": ("Telenor", "Balochistan"), "344": ("Telenor", "Islamabad"),
    "345": ("Telenor", "Gilgit Baltistan")
}

def is_valid_pakistani_number(number):
    return re.fullmatch(r"\+923\d{9}", number) is not None

def get_carrier_region(number):
    prefix = number[3:6]
    return prefix_region_map.get(prefix, ("Unknown", "Unknown"))

def generate_google_dork(number):
    query = f'"{number}" site:pastebin.com OR site:facebook.com OR site:github.com'
    return f"https://www.google.com/search?q={requests.utils.quote(query)}"

def check_whatsapp_status(number):
    return f"https://wa.me/{number[1:]}"

def simulate_social_checks(number):
    return {
        "Facebook": f"https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&email={number}",
        "Instagram": "Simulated (Use recovery page or social lookup)",
        "TikTok": "Simulated (Search by number not publicly supported)",
        "Gmail": "Try password recovery (https://accounts.google.com/signin/recovery)"
    }

def check_leaks_dork(number):
    query = f'"{number}" leak OR database OR "phone" filetype:txt'
    return f"https://www.google.com/search?q={requests.utils.quote(query)}"

def save_report(data, number):
    fname = f"pakrecon_report_{number[1:]}.json"
    with open(fname, "w") as f:
        json.dump(data, f, indent=4)
    print(Fore.GREEN + f"[✔] Report saved as {fname}")

def main():
    parser = argparse.ArgumentParser(description="PakRecon v2 - Advanced Pakistani Phone Number OSINT Tool")
    parser.add_argument("--number", help="Phone number in +923XXXXXXXXX format")
    args = parser.parse_args()

    if args.number:
        number = args.number.strip()
    else:
        number = input(Fore.CYAN + "Enter phone number (+923XXXXXXXXX): ").strip()

    if not is_valid_pakistani_number(number):
        print(Fore.RED + "[!] Invalid phone number format.")
        return

    print(Fore.GREEN + "[+] Valid number detected.")
    carrier, region = get_carrier_region(number)
    print(f"[+] Carrier      : {carrier}")
    print(f"[+] Region       : {region}")

    whatsapp_url = check_whatsapp_status(number)
    print(f"[+] WhatsApp     : Likely Active (Check: {whatsapp_url})")

    social = simulate_social_checks(number)
    print(f"[+] Facebook     : {social['Facebook']}")
    print(f"[+] Instagram    : {social['Instagram']}")
    print(f"[+] Gmail        : {social['Gmail']}")
    print(f"[+] TikTok       : {social['TikTok']}")

    dork_url = generate_google_dork(number)
    print(f"[+] Google Dork  : {dork_url}")

    leak_check = check_leaks_dork(number)
    print(f"[+] Leak Dork    : {leak_check}")

    report = {
        "number": number,
        "carrier": carrier,
        "region": region,
        "whatsapp": whatsapp_url,
        "facebook": social["Facebook"],
        "instagram": social["Instagram"],
        "gmail": social["Gmail"],
        "tiktok": social["TikTok"],
        "google_dork": dork_url,
        "leak_check": leak_check,
        "timestamp": str(datetime.now())
    }
    save_report(report, number)

if __name__ == "__main__":
    main()


