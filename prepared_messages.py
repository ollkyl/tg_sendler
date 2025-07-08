from telethon import TelegramClient
from dotenv import dotenv_values
import asyncio
from telethon.errors import ChatWriteForbiddenError

env_values = dotenv_values(".env")

api_id = int(env_values.get("API_ID"))
api_hash = env_values.get("API_HASH")
print(api_id)


channels_banned = ["channel1", "channel2", "channel3"]

channels_without_links = ["channel4", "channel5", "channel6"]

channels_with_links = ["channel7", "channel8", "channel9"]


sent_messages = set()


async def send_latest_posts():
    async with TelegramClient(
        "session_name", api_id, api_hash, system_version="4.16.30-vxCUSTOM"
    ) as client:
        while True:
            # Пересылаем обычные сообщения
            individual_messages = [
                "Привет! Это тестовое сообщение 1.",
                "Как дела? Это тестовое сообщение 2.",
                "Это третье тестовое сообщение.",
            ]

            async def msg_task():
                for msg in individual_messages:
                    await forward_to_channels(client, channels_with_links, msg)
                    await asyncio.sleep(3650)

            async def msg2_task():
                for msg in individual_messages:
                    msg = msg.replace("@", "")
                    await forward_to_channels(client, channels_without_links, msg)
                    await asyncio.sleep(3650)

            await asyncio.gather(msg_task(), msg2_task())

            print("⚠ Ожидание 30 секунд перед новой проверкой...")
            await asyncio.sleep(30)


async def forward_to_channels(client, channels, message):
    """Пересылает одиночное сообщение"""
    for channel in channels:
        try:
            await client.send_message(channel, message)
            # await client.forward_messages(channel, message)

            print(f"✅ Сообщение переслано в {channel}")

        except ChatWriteForbiddenError:
            print(f"❌ Нет прав на отправку в {channel}")
        except Exception as e:
            print(f"❌ Ошибка пересылки в {channel}: {e}")

    print(" forward_to_channelstttttttttttttttttt")
    await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.run(send_latest_posts())
