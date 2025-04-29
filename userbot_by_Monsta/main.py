# main.py

from telethon import TelegramClient
import config
import os
import importlib


client = TelegramClient(config.session_name, config.api_id, config.api_hash)


def load_modules():
    for filename in os.listdir('modules'):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            module = importlib.import_module(f'modules.{module_name}')
            if hasattr(module, 'register'):
                module.register(client)


async def main():
    load_modules()
    print("Userbot запущен! ✅")
    await client.run_until_disconnected()

client.start()
client.loop.run_until_complete(main())
