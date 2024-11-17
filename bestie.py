import os
import shutil
import subprocess  # To run git pull command
import requests
import random
import time
from datetime import datetime, timedelta

# File to store the generated key and timestamp
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

# Colors for terminal output
red = "\033[1;31m"    # Bold red
c = "\033[1;96m"      # Cyan (for key)
g = "\033[1;32m"      # Bold green
y = "\033[1;33m"      # Bold yellow
r = "\033[0m"         # Reset color
wh = "\033[1;37m"     # Bold white

# Time constants
KEY_EXPIRATION_DAYS = 42  # Key expires after 42 days (6 weeks)

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

def clone_and_run(repo_url, script_name):
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    
    if not os.path.exists(repo_name):
        os.system(f'git clone {repo_url}')
    
    os.chdir(repo_name)
    os.system(f'python {script_name}')
    os.chdir('..')

def generate_random_key():
    number1 = random.randint(1000, 9999)  # First random number
    number2 = random.randint(1000, 9999)  # Second random number
    key = f"{number1}-BOOSTING-TOOL-{number2}"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return key, timestamp

def get_key_and_timestamp():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'r') as file:
            content = file.read().strip()
            if content:
                key, timestamp = content.split('|')
                return key, timestamp
    return None, None

def save_key_and_timestamp(key, timestamp):
    with open(KEY_FILE, 'w') as file:
        file.write(f"{key}|{timestamp}")

def check_key_expiration(timestamp):
    # Convert timestamp to a datetime object
    key_date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    expiration_date = key_date + timedelta(days=KEY_EXPIRATION_DAYS)

    if datetime.now() > expiration_date:
        return True
    return False

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

def check_subscription(github_raw_url, approval_key):
    # Check subscription status from GitHub raw URL (i.e., a file indicating if the user is subscribed)
    try:
        response = requests.get(github_raw_url)
        response.raise_for_status()
        file_content = response.text

        if "subscribed" in file_content and approval_key in file_content:
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"Error accessing the GitHub subscription file: {e}")
        return False

def main_menu():
    clear_screen()
    overview()  # Call the overview function here

    # Approval Key Logic
    github_raw_url = 'https://github.com/0xppxuejoyd/keyy/blob/main/key.txt'  # Replace with your raw GitHub URL
    github_subs_url = 'https://github.com/0xppxuejoyd/subscription.txt'  # URL to check subscription status
    stored_key, timestamp = get_key_and_timestamp()

    if stored_key:
        # Check if the key has expired
        if check_key_expiration(timestamp):
            print(f"{red}Your key has expired! Please obtain a new key.{r}")
            exit()  # Exit if the key has expired
    else:
        stored_key, timestamp = generate_random_key()
        save_key_and_timestamp(stored_key, timestamp)
        print(f"Generated Approval Key: {stored_key}")

    # Check if the generated or stored key is approved
    if check_approval(github_raw_url, stored_key):
        print(f"{y}    YOUR KEY IS BEING APPROVED: {c}{stored_key}{r}")  # Key approved message in yellow and key in cyan
    else:
        print("YOUR KEY ISN'T APPROVED, EXITING...")
        exit()  # Exit if not approved

    # Check subscription status
    if not check_subscription(github_subs_url, stored_key):
        print("Your subscription is not active. Please subscribe to continue using the tool.")
        exit()  # Exit if the user is not subscribed

    print("[0] Update Tool")
    print("[1] Extract Account")
    print("[2] Auto Facebook Followers")
    print("[3] Auto Comments")
    print("[4] Auto Reply to Comments")
    print("[5] Auto Reacts")
    print("[6] Auto Create Page")
    print("[7] Auto React Comment")
    print("[8] Auto Reacts for Videos(NEW METHOD)")
    print('[9] Auto Reacts for Reels ')
    print("[10] Auto Join Groups")
    print("[11] Auto Comments for Reels")
    print("[12] Auto Comments for Videos")
    print("[13] Spam Shares")
    print("[14] Bundle Reactions")
    print("[15] Auto Comment For Post(EASY WAY FOR DIFFERENT COMMENTS)")
    print("[C] AUTO REMOVE DEAD ACCOUNTS")
    print("[RDP] REMOVE DUPLICATE ACCOUNTS")
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
        acc_checker()
    elif choice == 'RDP':
        dupli_remover()
    elif choice == 'R':
        reset()
    elif choice == 'E':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice, please try again.")
        main_menu()

def update():
    # Paths to the local repositories
    main_repo_path = '.'  # Assuming the
def update():
    # Paths to the local repositories
    main_repo_path = '.'  # Assuming the script is in the main repo directory
    boosting_repo_path = './BOOSTING'  # Path to the local BOOSTING repository

    # Update the main repository
    try:
        print(f"{c}Updating the main repository...{r}")
        subprocess.run(['git', 'pull'], cwd=main_repo_path, check=True)
        print(f"{wh}Main repository updated successfully.{r}")
    except subprocess.CalledProcessError as e:
        print(f"{red}Error occurred while updating the main repository: {e}{r}")

    # Check if the BOOSTING repo exists locally
    if not os.path.exists(boosting_repo_path):
        print(f"{red}BOOSTING repository not found locally. Please clone it first.{r}")
        return  # Exit if the repository is not found

    # Update the BOOSTING repository
    try:
        print(f"{c}Pulling the latest changes from the BOOSTING repository...{r}")
        subprocess.run(['git', 'pull'], cwd=boosting_repo_path, check=True)
        print(f"{wh}BOOSTING repository updated successfully.{r}")
    except subprocess.CalledProcessError as e:
        print(f"{red}Error occurred while updating the BOOSTING repository: {e}{r}")
              
# Add functions for other features like extract_account(), auto_facebook_followers(), etc.
# Below are examples of how they might look:

def extract_account():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'extract-acc.py'
    clone_and_run(repo_url, script_name)

def auto_facebook_followers():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'auto-follow.py'
    clone_and_run(repo_url, script_name)

def auto_comments():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'auto_comment.py'
    clone_and_run(repo_url, script_name)

def auto_reply_to_comments():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'atrc.py'
    clone_and_run(repo_url, script_name)

def auto_reacts():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'auto-reacts.py'
    clone_and_run(repo_url, script_name)

def auto_create_page():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'atc_page.py'
    clone_and_run(repo_url, script_name)

def auto_react_comment():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'auto-react-comment.py'
    clone_and_run(repo_url, script_name)

def auto_working_vid():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'working-vid.py'
    clone_and_run(repo_url, script_name)

def auto_reacts_reels():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'reels_reacts.py'
    clone_and_run(repo_url, script_name)

def auto_join_groups():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'join_group.py'
    clone_and_run(repo_url, script_name)

def auto_comments_reels():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'reels_comments.py'
    clone_and_run(repo_url, script_name)

def auto_comments_vids():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'video_comments.py'
    clone_and_run(repo_url, script_name)

def spam_share():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'spam_share.py'
    clone_and_run(repo_url, script_name)
    
def bundle_reacts():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'bundle_reacts.py'
    clone_and_run(repo_url, script_name)

def easy_comments():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'easy_comments.py'
    clone_and_run(repo_url, script_name)

def acc_checker():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'acc_checker.py'
    clone_and_run(repo_url, script_name)
    
def dupli_remover():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'dupli_remover.py'
    clone_and_run(repo_url, script_name)

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
    main_menu()