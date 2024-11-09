import os
import time
import random
import shutil
import subprocess  # To run git pull command
import requests

# Constants and configuration
KEY_FILE = 'approval_key.txt'  # Store the approval key
SUBSCRIPTION_FILE = 'subscriptions.txt'  # Store subscription data
valid_gcash_numbers = ['09123456789', '09234567890']  # Example valid GCash numbers for simplicity

logo = (f''' \033[1;32m  
          /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$$
         | $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$|__  $$__/
         | $$  \\ $$| $$  \\ $$| $$  \\ $$| $$  \\__/   | $$   
         | $$$$$$$ | $$  | $$| $$  | $$|  $$$$$$    | $$   
         | $$__  $$| $$  | $$| $$  | $$ \\____  $$   | $$   
         | $$  \\ $$| $$  | $$| $$  | $$ /$$  \\ $$   | $$   
         | $$$$$$$/|  $$$$$$/|  $$$$$$/| $$$$$$/   | $$   
         |_______/  \\______/  \\______/  \\______/    |__/   
                                                  
''')

def clear_screen():
    os.system('clear')

def count_lines(file_path):
    try:
        with open(file_path, 'r') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        return 0  # Return 0 if the file does not exist

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

def check_approval(approval_key):
    # Replace with actual key validation logic
    if approval_key == "valid-key":
        return True
    return False

def handle_subscription(gcash_number, amount_paid):
    """
    Handles subscription based on GCash number and payment.
    """
    expiration_time = None
    if gcash_number in valid_gcash_numbers:
        if amount_paid == 5:  # 5 pesos gives 1 day
            expiration_time = time.time() + 86400  # 1 day in seconds
        elif amount_paid == 20:  # 20 pesos gives 6 weeks
            expiration_time = time.time() + 6 * 7 * 86400  # 6 weeks in seconds
        else:
            print("Invalid amount for subscription.")
    else:
        print("Invalid GCash number.")
    
    return expiration_time

def check_subscription(gcash_number):
    """
    Check if the GCash number has a valid subscription.
    """
    try:
        with open(SUBSCRIPTION_FILE, 'r') as file:
            subscriptions = file.readlines()
        for line in subscriptions:
            number, expiration = line.strip().split(',')
            if number == gcash_number:
                expiration_time = float(expiration)
                if expiration_time > time.time():
                    return True
                else:
                    print(f"Subscription for {gcash_number} has expired.")
                    return False
    except FileNotFoundError:
        return False
    return False

def main_menu():
    clear_screen()
    print(logo)
    
    print("Checking approval...")
    stored_key = get_stored_key()
    if stored_key:
        approval_key = stored_key
    else:
        approval_key = generate_random_key()
        save_key(approval_key)
        print(f"Generated Approval Key: {approval_key}")

    if check_approval(approval_key):
        print(f"Your key is approved: {approval_key}")
    else:
        print("Your key is not approved. Exiting...")
        exit()

    print("[Enter] GCash Payment")
    gcash_number = input("Enter GCash number: ").strip()
    amount_paid = int(input("Enter the amount paid (5, 20): ").strip())

    # Handle subscription logic
    expiration_time = handle_subscription(gcash_number, amount_paid)
    if expiration_time:
        with open(SUBSCRIPTION_FILE, 'a') as file:
            file.write(f"{gcash_number},{expiration_time}\n")
        print(f"Payment successful! Subscription valid until {time.ctime(expiration_time)}")

    # Now check if the user has a valid subscription
    if not check_subscription(gcash_number):
        print("No valid subscription found. Exiting...")
        return  # Exit if the user doesn't have a valid subscription

    print("[0] Update Tool")
    print("[1] Extract Account")
    print("[2] Auto Facebook Followers")
    print("[3] Auto Comments")
    print("[4] Auto Reply to Comments")
    print("[5] Auto Reacts")
    print("[6] Auto Create Page")
    print("[7] Auto React Comment")
    print("[8] Auto Working Video")
    print("[9] Auto Reacts Reels")
    print("[10] Auto Join Groups")
    print("[11] Auto Comments Reels")
    print("[12] Auto Comments Vids")
    print("[13] Spam Share")
    print("[14] Bundle Reacts")
    print("[15] Easy Comments")
    print("[16] Acc Checker")
    print("[17] Duplicates Remover")
    print("[18] Reset")
    print("[E] Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '0':
        update()  # Update the tool
    elif choice == '1':
        extract_account()  # Extract account
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
    elif choice == '16':
        acc_checker()
    elif choice == '17':
        dupli_remover()
    elif choice == '18':
        reset()  # Reset the folder
    elif choice.upper() == 'E':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice, please try again.")
        main_menu()

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

# Function to clone the repository and run the script
def clone_and_run(repo_url, script_name):
    # Clone the repository
    if not os.path.exists('BOOSTING'):
        print("Cloning BOOSTING repository...")
        subprocess.run(['git', 'clone', repo_url])

    # Run the specific script from the repository
    script_path = os.path.join('BOOSTING', script_name)
    if os.path.exists(script_path):
        print(f"Running {script_name}...")
        subprocess.run(['python', script_path])
    else:
        print(f"Script {script_name} not found!")

# Update function to handle repository pulls
def update():
    # Paths to the local repositories
    main_repo_path = '.'  # Assuming the script is in the main repo directory
    boosting_repo_path = './BOOSTING'  # Path to the local BOOSTING repository

    # Update the main repository
    try:
        print("Updating the main repository...")
        subprocess.run(['git', 'pull'], cwd=main_repo_path, check=True)
        print("Main repository updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while updating the main repository: {e}")

    # Check if the BOOSTING repo exists locally
    if not os.path.exists(boosting_repo_path):
        print("BOOSTING repository not found locally. Please clone it first.")
        return  # Exit if the repository is not found

    # Update the BOOSTING repository
    try:
        print("Pulling the latest changes from the BOOSTING repository...")
        subprocess.run(['git', 'pull'], cwd=boosting_repo_path, check=True)
        print("BOOSTING repository updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while updating the BOOSTING repository: {e}")

# Function to check key validity from file
def check_key_validity():
    stored_key = get_stored_key()
    if stored_key and check_approval(stored_key):
        print(f"Your key is approved: {stored_key}")
    else:
        print("Your key is not approved. Exiting...")
        exit()

# Main function to control the flow
if __name__ == "__main__":
    main_menu()
