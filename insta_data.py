import instaloader
import os
import sys
import time
import pyfiglet

def clear_screen():
    """Clear the screen for a fresh view."""
    os.system("clear" if os.name != "nt" else "cls")

def display_ascii_art(text, font="slant"):
    """Generate and display ASCII art for the given text and font."""
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print('\033[1;32m' + ascii_art + '\033[0m')  # Green and bold

def get_instagram_profile_info(username, login_username, login_password, output_directory="insta_data"):
    """Fetch and save Instagram profile information."""
    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(output_directory, f"{username}_profile_info.txt")

    L = instaloader.Instaloader()
    profile_info = {}
    errors = []

    try:
        print(f"\033[1;33mAttempting to log in as {login_username}...\033[0m")
        L.login(login_username, login_password)
        print(f"\033[1;32mLogged in as {login_username}\033[0m")

        print(f"\033[1;33mFetching data for the profile: {username}...\033[0m")
        profile = instaloader.Profile.from_username(L.context, username)

        print("\033[1;32mProcessing profile data...\033[0m")
        profile_info = {
            'Profile ID': profile.userid,
            'Username': profile.username,
            'Full Name': profile.full_name,
            'Biography': profile.biography,
            'Followers': profile.followers,
            'Following': profile.followees,
            'Posts': profile.mediacount,
            'Is Private': profile.is_private,
            'Is Verified': profile.is_verified,
            'External URL': profile.external_url,
            'Profile Picture URL': profile.profile_pic_url,
            'Business Category': getattr(profile, 'business_category_name', 'N/A'),
            'Category': getattr(profile, 'category_name', 'N/A'),
        }

    except instaloader.exceptions.ProfileNotExistsException:
        errors.append(f"Profile '{username}' does not exist.")
    except instaloader.exceptions.ConnectionException:
        errors.append("Network issue. Please check your connection and try again.")
    except instaloader.exceptions.BadCredentialsException:
        errors.append("Invalid login credentials. Please check your username and password.")
    except Exception as e:
        errors.append(f"An unexpected error occurred: {e}")

    print("\033[1;33mSaving profile information to file...\033[0m")
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("Instagram Profile Information:\n")
        file.write("=" * 30 + "\n\n")

        for key, value in profile_info.items():
            file.write(f"{key}: {value}\n")

        if errors:
            file.write("\nErrors:\n")
            file.write("=" * 30 + "\n")
            for error in errors:
                file.write(f"- {error}\n")

    print(f"\033[1;32mProfile information successfully saved to {output_file}\033[0m")
    input("\033[1;32mPress Enter to return to the main menu...\033[0m")

def main():
    """Main function to run the Instagram data tool."""
    while True:
        clear_screen()
        display_ascii_art("Insta-Data")

        print("\n\033[1;33m--- Instagram Data Tool ---\033[0m")
        print("\n\033[1;33mOptions:\033[0m")
        print("1. Fetch Instagram Profile Info")
        print("0. Exit")

        try:
            choice = int(input("\033[1;33mEnter your choice: \033[0m"))

            if choice == 0:
                print("\033[1;32mExiting...\033[0m")
                break

            elif choice == 1:
                username = input("\033[1;33mEnter the Instagram username: \033[0m").strip()
                login_username = input("\033[1;33mEnter your Instagram login username: \033[0m").strip()
                login_password = input("\033[1;33mEnter your Instagram login password: \033[0m").strip()

                if username and login_username and login_password:
                    get_instagram_profile_info(username, login_username, login_password)
                else:
                    print("\033[1;31m[!] All fields are required. Please try again.\033[0m")
                    time.sleep(2)
            else:
                print("\033[1;31m[!] Invalid option. Please choose a valid one.\033[0m")
                time.sleep(2)

        except ValueError:
            print("\033[1;31m[!] Invalid input. Please enter a number.\033[0m")
            time.sleep(2)

if __name__ == "__main__":
    main()
