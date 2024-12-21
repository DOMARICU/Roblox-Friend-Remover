import requests
import time

# ===========================
# Roblox Friend Remover Script
# ===========================
# This script automatically removes all friends from a Roblox account.
# It uses Roblox's API endpoints for friend management and includes CSRF token handling.
#
# **Instructions:**
# 1. Replace "HERE YOUR COOKIES" with your .ROBLOSECURITY cookie.
#    - **How to find your cookie:**
#      a. Open your browser (e.g., Chrome, Firefox).
#      b. Navigate to the Roblox website and log in.
#      c. Open Developer Tools by pressing F12 or Ctrl+Shift+I (Cmd+Option+I on Mac).
#      d. Go to the "Application" tab (in some browsers, it may be under "Storage").
#      e. Look under "Cookies" for `https://www.roblox.com`.
#      f. Find the cookie named `.ROBLOSECURITY` and copy its value.
# 2. Replace "12345678" with your Roblox user ID.
#    - **How to find your user ID:**
#      a. Go to your Roblox profile page.
#      b. The URL will look like this: `https://www.roblox.com/users/12345678/profile`.
#      c. Copy the numerical part of the URL (e.g., `12345678`) and paste it below.
#
# **Disclaimer:**
# - This script is for educational purposes only.
# - Using automated scripts may violate Roblox's Terms of Service.
# - Use this script at your own risk. Your account could be banned.

# Roblox authentication cookie
ROBLOX_COOKIE = "HERE YOUR COOKIES"  # Replace with your .ROBLOSECURITY cookie
HEADERS = {
    'Cookie': f'.ROBLOSECURITY={ROBLOX_COOKIE}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

USER_ID = "12345678"  # Replace with your Roblox user ID

def update_csrf_token():
    """
    Retrieves a new CSRF token by intentionally causing a 403 error.
    The token is included in the response headers and is required for authenticated requests.
    """
    url = f"https://friends.roblox.com/v1/users/7672872696/unfriend"
    try:
        response = requests.post(url, headers=HEADERS)
        if response.status_code == 403 and 'X-CSRF-TOKEN' in response.headers:
            HEADERS['X-CSRF-TOKEN'] = response.headers['X-CSRF-TOKEN']
            print("CSRF token successfully updated.")
        else:
            print(f"Failed to retrieve CSRF token: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Unexpected error while retrieving CSRF token: {str(e)}")

def get_friends():
    """
    Fetches the user's friend list from the Roblox API.
    Returns a list of friends with their IDs and names.
    """
    url = f"https://friends.roblox.com/v1/users/{USER_ID}/friends"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print(f"Error retrieving friend list: {response.status_code}, {response.text}")
        return []

def remove_friend(friend_id):
    """
    Sends a request to the Roblox API to unfriend a specific user.
    Automatically retries with a refreshed CSRF token if the request fails due to token expiration.
    """
    url = f"https://friends.roblox.com/v1/users/{friend_id}/unfriend"
    response = requests.post(url, headers=HEADERS)
    if response.status_code == 200:
        print(f"Successfully removed friend {friend_id}.")
    elif response.status_code == 403:
        print("CSRF token expired, updating token...")
        update_csrf_token()
        response = requests.post(url, headers=HEADERS)
        if response.status_code == 200:
            print(f"Successfully removed friend {friend_id} (after token update).")
        else:
            print(f"Error removing friend {friend_id} after token update: {response.status_code}, {response.text}")
    else:
        print(f"Error removing friend {friend_id}: {response.status_code}, {response.text}")

def unfriend_all():
    """
    Fetches the friend list and iteratively removes each friend.
    Includes a delay between requests to avoid overwhelming the Roblox servers.
    """
    update_csrf_token()
    if 'X-CSRF-TOKEN' not in HEADERS:
        print("Script cannot start because the CSRF token could not be retrieved.")
        return

    friends = get_friends()
    print(f"You have {len(friends)} friends.")
    for friend in friends:
        print(f"Removing friend {friend['id']} - {friend['name']}...")
        remove_friend(friend['id'])
        time.sleep(1)

if __name__ == "__main__":
    unfriend_all()
