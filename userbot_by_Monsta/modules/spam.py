# modulesspam.py

import asyncio
from telethon import events

def register(client)
    @client.on(events.NewMessage(pattern=r'.spam (d+) (d+) (.+)'))
    async def spam(event)
        try
            args = event.pattern_match.groups()
            count = int(args[0])          # сколько сообщений отправить
            delay = int(args[1])           # пауза между отправкой (секунды)
            message = args[2]              # текст сообщения

            await event.reply(f🚀 Начинаю спам {count} сообщений, интервал {delay} сек.)

            for _ in range(count)
                await event.respond(message)
                await asyncio.sleep(delay)

            await event.respond(✅ Спам завершён!)

        except Exception as e
            await event.reply(f❌ Ошибка {str(e)})
