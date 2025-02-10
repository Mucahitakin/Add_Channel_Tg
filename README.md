# Telegram Group to Channel Member Adder

This script allows you to transfer members from a Telegram group to a Telegram channel using the Telethon library. The script avoids adding bots, excludes specific user IDs, and handles Telegram’s spam protection by waiting for the required time when necessary.

📌 Features
	•	✅ Select a Telegram account to use.
	•	✅ Fetch members from a selected Telegram group.
	•	✅ Add members to a selected Telegram channel.
	•	✅ Automatically waits if Telegram requests a cooldown period.
	•	✅ Ignores bots and excluded user IDs.
	•	✅ Uses random delays between member additions to prevent spam detection.

🔧 Installation

1️⃣ Install Required Dependencies

Make sure you have Python 3.7+ installed. Then, install the required dependencies:

pip install telethon

2️⃣ Set Up Your Telegram API Credentials

You need API ID and API Hash from My Telegram.
	•	Open my.telegram.org and log in with your Telegram account.
	•	Click on API Development Tools.
	•	Create a new application and get your API ID and API Hash.

3️⃣ Configure the Script

Edit the accounts list in the script and replace the placeholders:
```
accounts = [
    {"session": "account1", "api_id": YOUR_API_ID, "api_hash": "YOUR_API_HASH",
     "phone_number": "YOUR_PHONE_NUMBER"}
]
```
Replace YOUR_API_ID, YOUR_API_HASH, and YOUR_PHONE_NUMBER with your real credentials.

4️⃣ Run the Script

Run the script using:
```
python script.py
```
Follow the on-screen instructions:
	1.	Select the Telegram account.
	2.	Choose the group from which you want to transfer members.
	3.	Select the target channel where members should be added.

The script will begin adding members and handle any Telegram restrictions automatically.

⚠️ Important Notes
	•	You must be an admin in the target channel to add members.
	•	Telegram imposes limits on how many users you can add per day. If the script gets blocked, wait and try again later.
	•	Do not abuse this tool, as excessive use may lead to a temporary or permanent ban of your account.
