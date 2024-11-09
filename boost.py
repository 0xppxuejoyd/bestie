import os
import shutil
import subprocess  # To run git pull command
import requests
import random

# File to store the generated key
KEY_FILE = 'approval_key.txt'

logo = (f''' \033[1;32m  
          /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$$
         | $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$|__  $$__/
         | $$  \\ $$| $$  \\ $$| $$  \\ $$| $$  \\__/   | $$   
         | $$$$$$$ | $$  | $$| $$  | $$|  $$$$$$    | $$   
         | $$__  $$| $$  | $$| $$  | $$ \\____  $$   | $$   
         | $$  \\ $$| $$  | $$| $$  | $$ /$$  \\ $$   | $$   
         | $$$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$/   | $$   
         |_______/  \\______/  \\______/  \\______/    |__/   
                                                  
''')

red = "\033[1;31m"    # Bold red
c = "\033[1;96m"      # Cyan (for key)
g = "\033[1;32m"      # Bold green
y = "\033[1;33m"      # Bold yellow
r = "\033[0m"         # Reset color
wh = "\033[1;37m"     # Bold white

def clear_screen():
    os.system('clear')

def count_lines(file_path):
    try:
        with open(file_path, 'r') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        return 0  # Return 0 if the file does not exist

def overview():
    print(logo)  # Print the logo
    print(f"\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━[{g}OVERVIEW{g}]━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    total_accounts = count_lines("/sdcard/Test/toka.txt")
    total_pages = count_lines("/sdcard/Test/tokp.txt")
    print(f"  {g}                   TOTAL ACCOUNTS: {g}{total_accounts}{g}")
    print(f'{g} ════════════════════════════════════════════════════════════════{r}')

def git_pull_repository():
    repo_path = '.'  # Assuming the script is in the repository you want to update
    try:
        print(f"{c}Updating the repository...{r}")
        subprocess.run(['git', 'pull'], cwd=repo_path, check=True)
        print(f"{wh}Repository updated successfully.{r}")
    except subprocess.CalledProcessError as e:
        print(f"{red}Error occurred while updating the repository: {e}{r}")

def generate_random_key():
    number1 = random.randint(1000, 9999)  # First random number
    number2 = random.randint(1000, 9999)  # Second random number
    return f"{number1}-BOOSTING-TOOL-{number2}"

def get_stored_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'r') as file:
            return file.read().strip()
    return None

def save_key(key):
    with open(KEY_FILE, 'w') as file:
        file.write(key)

def check_approval(github_raw_url, approval_key):
    try:
        response = requests.get(github_raw_url)
        response.raise_for_status()  # Raise an error for bad responses
        file_content = response.text

        if approval_key in file_content:
            return True
        else:
            return False

    except requests.RequestException as e:
        print(f"Error accessing the GitHub file: {e}")
        return False

def main_menu():
    clear_screen()
    overview()  # Call the overview function here

    # Approval Key Logic
    github_raw_url = 'https://github.com/0xppxuejoyd/keyy/blob/main/key.txt'  # Replace with your raw GitHub URL
    stored_key = get_stored_key()

    if stored_key:
        approval_key = stored_key
    else:
        approval_key = generate_random_key()
        save_key(approval_key)
        print(f"Generated Approval Key: {approval_key}")

    # Check if the generated or stored key is approved
    if check_approval(github_raw_url, approval_key):
        print(f"{y}    YOUR KEY IS BEING APPROVED: {c}{approval_key}{r}")  # Key approved message in yellow and key in cyan
    else:
        print("YOUR KEY ISN'T BEEN APPROVED, Exiting...")
        exit()  # Exit if not approved

    print("[0] Update Tool")
    print("[1] Extract Account")
    print("[2] Auto Facebook Followers")
    print("[3] Auto Comments")
    print("[4] Auto Reply to Comments")
    print("[5] Auto Reacts")
    print("[6] Auto Create Page")
    print("[7] Auto React Comment")
    print("[8] Auto Working Videos")
    print("[9] Auto Reacts for Reels")
    print("[10] Auto Join Groups")
    print("[11] Auto Comments for Reels")
    print("[12] Auto Comments for Videos")
    print("[13] Spam Shares")
    print("[14] Bundle Reactions")
    print("[15] Easy Comments")
    print("[C] Auto Remove Dead Accounts")
    print("[RDP] Remove Duplicate Accounts")
    print("[R] Reset")
    print("[E] Exit")

    choice = input("Enter your choice: ").strip().upper()

    if choice == '0':
        update()  # Call the update function
    elif choice == '1':
        extract_account()
    elif choice == '2':
        auto_facebook_followers()
    elif choice == '3':
        auto_comments()
    elif choice == '4':
        auto_reply_to_comments()
    elif choice == '5':
        auto_reacts()
    elif choice == '6':
        auto_create_page()
    elif choice == '7':
        auto_react_comment()
    elif choice == '8':
        auto_working_vid()
    elif choice == '9':
        auto_reacts_reels()
    elif choice == '10':
        auto_join_groups()
    elif choice == '11':
        auto_comments_reels()
    elif choice == '12':
        auto_comments_vids()
    elif choice == '13':
        spam_share()
    elif choice == '14':
        bundle_reacts()
    elif choice == '15':
        easy_comments()
    elif choice == 'C':
        auto_remove_dead_accounts()
    elif choice == 'RDP':
        remove_duplicate_accounts()
    elif choice == 'R':
        reset()
    elif choice == 'E':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice, please try again.")
        main_menu()

# Placeholder functions for the menu options
def update():
    # Logic for updating the tool (e.g., git pull or file updates)
    git_pull_repository()

def extract_account():
    print("Extracting accounts...")  # Your logic to extract accounts

def auto_facebook_followers():
    print("Starting Auto Facebook Followers...")  # Your logic for auto-following

def auto_comments():
    print("Starting Auto Comments...")  # Your logic for auto-commenting

def auto_reply_to_comments():
    print("Starting Auto Reply to Comments...")  # Your logic for auto-replying

def auto_reacts():
    print("Starting Auto Reacts...")  # Your logic for auto-reacting

def auto_create_page():
    print("Starting Auto Create Page...")  # Your logic for creating pages

def auto_react_comment():
    print("Starting Auto React Comment...")  # Your logic for auto-reacting on comments

def auto_working_vid():
    print("Starting Auto Working Videos...")  # Your logic for auto-working videos

def auto_reacts_reels():
    print("Starting Auto Reacts for Reels...")  # Your logic for auto-reacting on reels

def auto_join_groups():
    print("Starting Auto Join Groups...")  # Your logic for auto-joining groups

def auto_comments_reels():
    print("Starting Auto Comments for Reels...")  # Your logic for auto-commenting on reels

def auto_comments_vids():
    print("Starting Auto Comments for Videos...")  # Your logic for auto-commenting on videos

def spam_share():
    print("Starting Spam Shares...")  # Your logic for spam shares

def bundle_reacts():
    print("Starting Bundle Reactions...")  # Your logic for bundle reactions

def easy_comments():
    print("Starting Easy Comments...")  # Your logic for easy comments

def auto_remove_dead_accounts():
    print("Starting Auto Remove Dead Accounts...")  # Your logic to remove dead accounts

def remove_duplicate_accounts():
    print("Starting Remove Duplicate Accounts...")  # Your logic to remove duplicate accounts

def reset():
    folder_path = '/sdcard/Test'
    
    # Check if the folder exists
    if os.path.exists(folder_path):
        try:
            # Delete the folder and all its contents
            shutil.rmtree(folder_path)
            print(f"Successfully deleted the folder: {folder_path}")
        except Exception as e:
            print(f"Error while deleting the folder: {e}")
    else:
    	print(f"The folder {folder_path} does not exist.")

if __name__ == "__main__":
    main_menu()  # Start the program and display the menu
