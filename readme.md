# README

## Roblox Friend Remover by Vortex
https://discord.gg/DNgMdVfxJu

This script automates the process of removing all friends from a Roblox account. It interacts with Roblox's API endpoints to retrieve your friend list and remove them individually.

### Features
- Automatically retrieves your entire friend list.
- Removes friends iteratively to avoid overwhelming Roblox's servers.
- Handles CSRF token updates for secure API interactions.

### Usage Instructions

1. **Download the Script**
   - Clone or download this repository to your local machine.

2. **Configure the Script**
   - Open the script in any text editor.
   - Replace the placeholder `HERE YOUR COOKIES` with your `.ROBLOSECURITY` cookie:
     - Open your browser (e.g., Chrome or Firefox).
     - Go to the Roblox website and log in.
     - Open Developer Tools (`F12` or `Ctrl+Shift+I`).
     - Navigate to the "Application" tab and select "Cookies" for `https://www.roblox.com`.
     - Find the `.ROBLOSECURITY` cookie and copy its value.
   - Replace `12345678` with your Roblox user ID:
     - Your user ID is visible in your profile URL (e.g., `https://www.roblox.com/users/12345678/profile`).

3. **Run the Script**
   - Ensure Python or Python 3 is installed on your system.
   - Execute the script in a terminal using:
     ```bash
     python script_name.py
     ```

4. **Review the Output**
   - The script will list all friends and remove them one by one.

### Disclaimer
- This script is for educational purposes only.
- Using automated tools may violate Roblox's Terms of Service.
- Use at your own risk. The author is not responsible for any actions taken against your account.

---

