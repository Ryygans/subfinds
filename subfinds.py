import requests
import os

GREEN = "\033[32m"
RESET = "\033[0m"

ascii_art = GREEN + """
  /$$$$$$            /$$       /$$$$$$$$ /$$                 /$$          
 /$$__  $$          | $$      | $$_____/|__/                | $$          
| $$  \__/ /$$   /$$| $$$$$$$ | $$       /$$ /$$$$$$$   /$$$$$$$  /$$$$$$$
|  $$$$$$ | $$  | $$| $$__  $$| $$$$$   | $$| $$__  $$ /$$__  $$ /$$_____/
 \____  $$| $$  | $$| $$  \ $$| $$__/   | $$| $$  \ $$| $$  | $$|  $$$$$$ 
 /$$  \ $$| $$  | $$| $$  | $$| $$      | $$| $$  | $$| $$  | $$ \____  $$
|  $$$$$$/|  $$$$$$/| $$$$$$$/| $$      | $$| $$  | $$|  $$$$$$$ /$$$$$$$/
 \______/  \______/ |_______/ |__/      |__/|__/  |__/ \_______/|_______/ 
""" + RESET
print(GREEN + "Coded By : Zann" + RESET)
def get_subdomains_crtsh(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        subdomains = {entry["name_value"] for entry in data}
        return subdomains
    return []

def main():
    os.system('clear')
    print(ascii_art)
    
    domain = input(GREEN + "Enter your domain: " + RESET)
    subdomains = get_subdomains_crtsh(domain)
    print(GREEN + "\nSubdomain find!:" + RESET)
    for sub in subdomains:
        print(GREEN + sub + RESET)
    repeat()

def repeat():
    exit_choice = input(GREEN + 'want to search again? (y/n): ' + RESET)
    if exit_choice.lower() == 'y':
        main()
    else:
        print(GREEN + 'You have logged out.' + RESET)

if __name__ == "__main__":
    main()
