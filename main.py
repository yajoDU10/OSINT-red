import os
import time
import pyfiglet
import subprocess
import sys


def activate_venv():
    """Activate the virtual environment."""
    venv_path = os.path.join(os.getcwd(), "venv", "bin", "activate")
    if os.name == "nt":
        venv_path = os.path.join(os.getcwd(), "venv", "Scripts", "activate.bat")
    if not os.path.exists(venv_path):
        print("\033[1;31m[!] Virtual environment not found. Please create it first using 'python3 -m venv venv'.\033[0m")
        sys.exit(1)
    print("\033[1;32m[INFO] Activating virtual environment...\033[0m")
    if os.name == "nt":
        subprocess.call(venv_path, shell=True)
    else:
        os.system(f"source {venv_path}")


def display_ascii_art(text, font="slant"):
    """Generate and display ASCII art for the given text and font."""
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print('\033[1;31m' + ascii_art + '\033[0m')  # Red and bold


def display_menu():
    """Display the main menu."""
    print("\n\033[1;31m--- Information Gathering Framework ---\033[0m")  # Heading in red
    print("\n\033[1;33mOptions:\033[0m")
    print("1. Do you have an Email?")
    print("2. Do you have a Username?")
    print("3. Do you want any help for Dorking?")
    print("4. Phishing tools and Phishing mail maker here")
    print("5. Instagram Account Info")
    print("0. Exit")


def validate_email(email):
    """Validate email input for the presence of '@'."""
    return "@" in email and len(email) > 3


def validate_username(username):
    """Validate username input (non-empty)."""
    return bool(username.strip())


def clear_screen():
    """Clear the screen for a fresh view."""
    os.system("clear" if os.name != "nt" else "cls")


def execute_email_options(email):
    """Display email options and execute selected commands."""
    email_dir = os.path.join("email_data", email)
    os.makedirs(email_dir, exist_ok=True)

    while True:
        clear_screen()
        print("\033[1;33mEmail Analysis for:\033[0m", email)
        print("\033[1;33mWhat else do you want to do?\033[0m")
        print("1. Perform General Info (GHunt)")
        print("2. Check existence on the web (holehe)")
        print("3. Check if email is compromised (h8mail)")
        print("4. Check availability of email as username (sherlock)")
        print("0. Go Back")

        try:
            choice = int(input("\033[1;33mEnter your choice: \033[0m"))

            if choice == 1:
                output_file = os.path.join(email_dir, "ghunt.txt")
                print("\033[1;32m[INFO] Running GHunt...\033[0m")
                os.system(f"ghunt email {email} > {output_file}")
                print(f"\033[1;34m[+] Output saved in: {output_file}\033[0m\n")
                input("\033[1;33mPress Enter to continue...\033[0m")

            elif choice == 2:
                output_file = os.path.join(email_dir, "holehe.txt")
                print("\033[1;32m[INFO] Running Holehe...\033[0m")
                os.system(f"holehe {email} > {output_file}")
                print(f"\033[1;34m[+] Output saved in: {output_file}\033[0m\n")
                input("\033[1;33mPress Enter to continue...\033[0m")

            elif choice == 3:
                output_file = os.path.join(email_dir, "h8mail.txt")
                print("\033[1;32m[INFO] Running H8mail...\033[0m")
                os.system(f"h8mail -t {email} > {output_file}")
                print(f"\033[1;34m[+] Output saved in: {output_file}\033[0m\n")
                input("\033[1;33mPress Enter to continue...\033[0m")

            elif choice == 4:
                output_file = os.path.join(email_dir, "sherlock.txt")
                print("\033[1;32m[INFO] Running Sherlock...\033[0m")
                os.system(f"sherlock {email} > {output_file}")
                print(f"\033[1;34m[+] Output saved in: {output_file}\033[0m\n")
                input("\033[1;33mPress Enter to continue...\033[0m")

            elif choice == 0:
                return  # Exit to the main menu

            else:
                print("\033[1;31m[!] Invalid option. Please choose a valid one.\033[0m")
                time.sleep(2)

        except ValueError:
            print("\033[1;31m[!] Invalid input. Please enter a valid number.\033[0m")
            time.sleep(2)


def execute_username_option(username):
    """Handle username-related commands."""
    username_dir = os.path.join("username_data", username)
    os.makedirs(username_dir, exist_ok=True)

    clear_screen()
    print("\033[1;32m[INFO] Searching for username...\033[0m")
    output_file = os.path.join(username_dir, "sherlock.txt")
    print("\033[1;32m[INFO] Running Sherlock...\033[0m")
    os.system(f"sherlock {username} > {output_file}")
    print(f"\033[1;34m[+] Output saved in: {output_file}\033[0m\n")
    input("\033[1;33mPress Enter to continue...\033[0m")


def execute_dork_helper():
    """Run the dork helper."""
    clear_screen()
    print("\033[1;32m[INFO] Running Dork Helper...\033[0m")
    os.system("python3 dorkhelper.py")


def execute_email_format_generator():
    """Run the email format generator and related tools."""
    while True:
        clear_screen()
        print("\033[1;32m[INFO] Email Format Generator and Additional Tools\033[0m")
        print("\n\033[1;33mOptions:\033[0m")
        print("1. Generate Email Formats")
        print("2. Run Hound.sh")
        print("3. Run Camphish.sh")
        print("4. Run Zphisher.sh")
        print("0. Go Back")

        try:
            choice = int(input("\033[1;33mEnter your choice: \033[0m"))

            if choice == 0:
                return  # Exit to the main menu

            elif choice == 1:
                print("\033[1;32m[INFO] Running Email Format Generator...\033[0m")
                os.system("cd phishmailer; python3 PhishMailer.py")
            elif choice == 2:
                print("\033[1;32m[INFO] Running Hound...\033[0m")
                os.system("cd hound; bash hound.sh")
            elif choice == 3:
                print("\033[1;32m[INFO] Running Camphish...\033[0m")
                os.system("cd camphish; bash camphish.sh")
            elif choice == 4:
                print("\033[1;32m[INFO] Running Zphisher...\033[0m")
                os.system("cd zphisher; bash zphisher.sh")
            else:
                print("\033[1;31m[!] Invalid option. Please choose a valid one.\033[0m")
                time.sleep(2)

        except ValueError:
            print("\033[1;31m[!] Invalid input. Please enter a valid number.\033[0m")
            time.sleep(2)


def execute_instaloader():
    """Run insta_data.py to retrieve Instagram account info."""
    clear_screen()
    print("\033[1;32m[INFO] Running Instagram Data Tool...\033[0m")
    os.system("python3 insta_data.py")


def main():
    """Main function to run the program."""
    try:
        # Activate virtual environment
        activate_venv()

        while True:
            clear_screen()
            display_ascii_art("OSINT-RED")
            display_menu()

            try:
                choice = int(input("\nEnter your choice: "))

                if choice == 0:
                    print("\n\033[1;32mExiting...\033[0m")
                    break

                elif choice == 1:  # Email
                    email = input("\033[1;33 mEnter the email: \033[0m")
                    if not validate_email(email):
                        print("\033[1;31m[!] Invalid email. Please enter a valid email address.\033[0m")
                        time.sleep(2)
                        continue
                    execute_email_options(email)

                elif choice == 2:  # Username
                    username = input("\033[1;33mEnter the username: \033[0m")
                    if not validate_username(username):
                        print("\033[1;31m[!] Invalid username. Please enter a non-empty username.\033[0m")
                        time.sleep(2)
                        continue
                    execute_username_option(username)

                elif choice == 3:  # Dork Helper
                    execute_dork_helper()

                elif choice == 4:  # Phishing tools and email generator
                    execute_email_format_generator()

                elif choice == 5:  # Instagram Account Info
                    execute_instaloader()

                else:
                    print("\033[1;31m[!] Please enter a valid option.\033[0m")
                    time.sleep(2)

            except ValueError:
                print("\033[1;31m[!] Invalid input. Please enter a number.\033[0m")
                time.sleep(2)

    finally:
        # Deactivate virtual environment
        print("\033[1;32m[INFO] Exiting the program...\033[0m")


if __name__ == "__main__":
    main()
