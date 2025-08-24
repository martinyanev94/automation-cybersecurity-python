pip install pyautogui
import pyautogui
import time

def lock_user_account(username):
    print(f"Locking account for {username}...")
    
    # Example: This could be an API call or a database transaction instead 
    pyautogui.alert(text=f'Account for {username} has been locked!', title='Security Alert', button='OK')

# Simulating an unauthorized access event
unauthorized_username = "malicious_user"
lock_user_account(unauthorized_username)
