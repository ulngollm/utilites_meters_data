from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram import filters
from commands import Handlers
import os



load_dotenv()
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')

app = Client('bot', API_ID, API_HASH, bot_token=BOT_API_TOKEN)


def hello(client, message):
    message.reply(
        'Привет!'
    )

app.add_handler(MessageHandler(hello, filters.command(['start'])))
app.add_handler(MessageHandler(Handlers.add_request, filters.command(['add'])))
app.add_handler(MessageHandler(Handlers.last, filters.command(['last'])))
app.add_handler(MessageHandler(Handlers.calc, filters.command(['calc'])))

app.add_handler(CallbackQueryHandler(Handlers.add))
app.add_handler(MessageHandler(Handlers.read_input, filters.text))

app.run()