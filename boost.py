import os
import subprocess
import shutil
import random
import time

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
wh = "\033[1;37m"     # Bold white
r = "\033[0m"         # Reset color

KEY_FILE = 'approval_key.txt'

# Simulate GCash Payment Details (for demo purposes)
GCASH_TRANSACTION_NUMBER = "GCASH123456789"  # A dummy transaction number (you would use real payment verification)

# Function to simulate a GCash Payment
def process_payment():
    print(f"{y}Please make a payment via GCash. Pay the amount using the GCash transaction number below.{r}")
    print(f"{c}{GCASH_TRANSACTION_NUMBER}{r}")  # Display the GCash reference number for the user to make payment
    
    print("\nAfter payment, please enter the GCash transaction number you received via SMS or Email.")
    
    user_code = input("Enter your GCash transaction number: ").strip()
    
    # Simulate automatic payment confirmation
    if user_code == GCASH_TRANSACTION_NUMBER:
        print(f"{g}Payment confirmed! You have been automatically approved for 1 day of access.{r}")
        return True
    else:
        print(f"{red}Invalid transaction number. Please check your GCash payment or try again later.{r}")
        return False

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
    # This function checks if the approval key is approved by checking a file in GitHub.
    # For now, just returns True as placeholder for GitHub approval logic.
    return True

def clear_screen():
    os.system('clear')

def overview():
    print(logo)  # Print the logo
    print(f"\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━[{g}OVERVIEW{g}]━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"  {g}                   TOTAL ACCOUNTS: {g}50{g}")
    print(f'{g} ════════════════════════════════════════════════════════════════{r}')

def main_menu():
    clear_screen()
    overview()  # Call the overview function here

    # Check if the user has a valid subscription
    stored_key = get_stored_key()

    if stored_key:
        approval_key = stored_key
    else:
        approval_key = generate_random_key()
        save_key(approval_key)
        print(f"Generated Approval Key: {approval_key}")

    # Check if the generated or stored key is approved
    github_raw_url = 'https://github.com/0xppxuejoyd/keyy/blob/main/key.txt'  # Replace with your raw GitHub URL
    if check_approval(github_raw_url, approval_key):
        print(f"{y}    YOUR KEY IS BEING APPROVED: {c}{approval_key}{r}")  # Key approved message in yellow and key in cyan
    else:
        print(f"{red}YOUR KEY ISN'T APPROVED. Exiting...{r}")
        exit()  # Exit if not approved

    # Menu options
    print("[0] Update Tool")
    print("[1] Extract Account")
    print("[2] Auto Facebook Followers")
    print("[3] Auto Comments")
    print("[4] Auto Reply to Comments")
    print("[5] Auto Reacts")
    print("[6] Auto Create Page")
    print("[7] Auto React Comment")
    print("[8] Auto Reacts for Videos(NEW METHOD)")
    print("[9] Auto Reacts for Reels")
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
        print(f"{red}Invalid choice, please try again.{r}")
        main_menu()

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

def clone_and_run(repo_url, script_name):
    # Function to clone and run a script from GitHub
    subprocess.run(['git', 'clone', repo_url])
    subprocess.run(['python3', script_name])

def reset():
    folder_path = '/sdcard/Test'
    
    # Check if the folder exists
    if os.path.exists(folder_path):
        try:
            # Delete the folder and all its contents
            shutil.rmtree(folder_path)
            print(f"Successfully deleted the folder: {folder_path}")  # Inside the try block
        except Exception as e:
            print(f"Error while deleting the folder: {e}")  # If there's an error, it will print this
    else:
        print(f"The folder {folder_path} does not exist.")  # If the folder doesn't exist

if __name__ == "__main__":
    main_menu()
