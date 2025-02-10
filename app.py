from telethon import TelegramClient, events
import asyncio
import random
import re
from telethon.tl.functions.channels import InviteToChannelRequest

class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

accounts = [
    {"session": "account1", "api_id": api_id, "api_hash": "api_hash",
     "phone_number": "phone_number"}
]

excluded_user_ids = {x, x, x}
default_delay = (5, 10)  

def select_account():
    print("Accounts:")
    for i, account in enumerate(accounts):
        print(f"{i} - {account['phone_number']}")
    account_index = int(input("Which account do you want to select? (Number): "))
    return accounts[account_index]

async def add_members_to_channel(client, source_group, target_channel):
    """Adds group members to a channel as users (does not make them admins)."""
    try:
        members = await client.get_participants(source_group)
        print(f"{len(members)} members found. Adding to the channel...")

        for member in members:
            if not member.bot and member.id not in excluded_user_ids:
                try:
                    await client(InviteToChannelRequest(target_channel, [member.id]))
                    print(f"{Colors.GREEN}{member.id} successfully added to the channel.{Colors.RESET}")
                    await asyncio.sleep(random.randint(*default_delay))  # Anti-spam wait time
                except Exception as e:
                    error_message = str(e)
                    print(f"{Colors.RED}Error adding {member.id}: {error_message}{Colors.RESET}")

                    # Extract the X value from "A wait of X seconds is required" message
                    wait_time_match = re.search(r"A wait of (\d+) seconds is required", error_message)
                    if wait_time_match:
                        wait_time = int(wait_time_match.group(1))
                        print(f"{Colors.RED}Telegram spam protection! Waiting for {wait_time} seconds...{Colors.RESET}")
                        await asyncio.sleep(wait_time)
                    else:
                        await asyncio.sleep(random.randint(*default_delay))  # Normal wait time
    except Exception as e:
        print(f"{Colors.RED}An error occurred: {e}{Colors.RESET}")

async def main():
    selected_account = select_account()
    client = TelegramClient(selected_account["session"],
                            selected_account["api_id"],
                            selected_account["api_hash"])
    async with client:
        await client.start(phone=selected_account["phone_number"])
        print(f"Logged in with {selected_account['phone_number']}!")

        groups = []
        channels = []
        async for dialog in client.iter_dialogs():
            if dialog.is_group:
                groups.append(dialog)
            elif dialog.is_channel:
                channels.append(dialog)

        print("Groups:")
        for i, group in enumerate(groups):
            print(f"{i} - {group.title}")
        group_index = int(input("Select the group whose members you want to add: "))
        source_group = groups[group_index]

        print("Channels:")
        for i, channel in enumerate(channels):
            print(f"{i} - {channel.title}")
        channel_index = int(input("Select the target channel: "))
        target_channel = channels[channel_index]

        await add_members_to_channel(client, source_group, target_channel)

if __name__ == "__main__":
    asyncio.run(main())
