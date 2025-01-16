import urllib.parse
import os
import time
import pyfiglet
from datetime import datetime

def clear_screen():
    """Clear the screen for a fresh view."""
    os.system("clear" if os.name != "nt" else "cls")

def display_ascii_art(text, font="slant"):
    """Generate and display ASCII art for the given text and font."""
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print('\033[1;34m' + ascii_art + '\033[0m')  # Blue and bold

def generate_dork_query(name=None, email=None, contact_no=None, username=None, platform=None):
    """Generate Google Dork queries based on input parameters."""
    queries = []

    if name:
        queries.extend([
            f'intext:"{name}"',
            f'allintext:"{name}"',
            f'intitle:"{name}"',
            f'inurl:"{name}"',
            f'site:linkedin.com "{name}"',
            f'site:github.com "{name}"',
            f'"{name}" filetype:pdf OR filetype:doc OR filetype:txt',
            f'"{name}" ext:log OR ext:sql OR ext:db'
        ])

    if email:
        queries.extend([
            f'intext:"{email}"',
            f'allintext:"{email}"',
            f'intitle:"{email}"',
            f'inurl:"{email}"',
            f'site:linkedin.com "{email}"',
            f'site:facebook.com "{email}"',
            f'filetype:txt "{email}"',
            f'filetype:csv "{email}"',
            f'"{email}" ext:log OR ext:sql OR ext:db'
        ])

    if contact_no:
        queries.extend([
            f'intext:"{contact_no}"',
            f'allintext:"{contact_no}"',
            f'intitle:"{contact_no}"',
            f'inurl:"{contact_no}"',
            f'site:facebook.com "{contact_no}"',
            f'site:instagram.com "{contact_no}"',
            f'"{contact_no}" ext:xls OR ext:xlsx OR ext:csv',
            f'"{contact_no}" OR "{contact_no.replace("-", "")}"'
        ])

    if username and platform:
        queries.extend([
            f'site:{platform}.com inurl:"{username}"',
            f'site:{platform}.com intitle:"{username}"',
            f'site:{platform}.com intext:"{username}"',
            f'allintext:"{username}" site:{platform}.com',
            f'inurl:"{username}" site:{platform}.com',
            f'intitle:"{username}" site:{platform}.com'
        ])

    if username:
        queries.extend([
            f'intext:"{username}"',
            f'allintext:"{username}"',
            f'inurl:"{username}"',
            f'intitle:"{username}"',
            f'site:github.com "{username}"',
            f'site:linkedin.com "{username}"',
            f'site:twitter.com "{username}"',
            f'"{username}" ext:log OR ext:sql OR ext:db',
            f'"{username}" filetype:txt OR filetype:pdf OR filetype:doc',
            f'"{username}" OR "{username}"'
        ])

    return queries

def perform_google_dork(queries):
    """Print Google Dork queries and their search URLs, and save to a file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_directory = "dork"
    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(output_directory, f"{timestamp}.txt")

    with open(output_file, "w", encoding="utf-8") as file:
        for idx, query in enumerate(queries, start=1):
            encoded_query = urllib.parse.quote(query)
            url = f"https://www.google.com/search?q={encoded_query}&hl=en"
            output = f"Dork {idx}: {query}\nSearch URL: {url}\n\n"
            print(f"\033[1;33mDork {idx}: \033[0m{query}")
            print(f"\033[1;36mSearch URL: \033[0m{url}\n")
            file.write(output)

    print(f"\033[1;32mDork queries saved to {output_file}\033[0m")

def main():
    """Main function for the Dork Helper tool."""
    while True:
        clear_screen()
        display_ascii_art("Dork Helper")

        print("\n\033[1;33m--- Google Dork Helper ---\033[0m")
        print("\n\033[1;33mOptions:\033[0m")
        print("1. Generate Dork Queries")
        print("0. Exit")

        try:
            choice = int(input("\033[1;33mEnter your choice: \033[0m"))

            if choice == 0:
                print("\033[1;32mExiting...\033[0m")
                break

            elif choice == 1:
                name = input("\033[1;33mEnter name (or press Enter to skip): \033[0m").strip()
                email = input("\033[1;33mEnter email (or press Enter to skip): \033[0m").strip()
                contact_no = input("\033[1;33mEnter contact number (or press Enter to skip): \033[0m").strip()
                username = input("\033[1;33mEnter username (or press Enter to skip): \033[0m").strip()
                platform = input("\033[1;33mEnter platform for username (or press Enter to skip): \033[0m").strip()

                dork_queries = generate_dork_query(name, email, contact_no, username, platform)
                perform_google_dork(dork_queries)

                input("\033[1;32mPress Enter to return to the main menu...\033[0m")

            else:
                print("\033[1;31m[!] Invalid option. Please choose a valid one.\033[0m")
                time.sleep(2)

        except ValueError:
            print("\033[1;31m[!] Invalid input. Please enter a number.\033[0m")
            time.sleep(2)

if __name__ == "__main__":
    main()
