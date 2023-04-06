import os
import openai
import time
import json
import random
import twitchio
from twitchio.client import Client
from twitchio.ext import commands
import configparser
#import logging
#logging.basicConfig(level=logging.DEBUG)

config = configparser.ConfigParser()
config.read('config.ini')

# Your Twitch bot's username and OAuth token https://id.twitch.tv/oauth2/authorize?response_type=token&client_id={clientId}&redirect_uri=http://localhost&scope=chat%3Aedit+chat%3Aread&state=c3ab8aa609ea11e793ae92361f002671
BOT_USERNAME = config.get('API_KEYS', 'twitch-username')
TOKEN = config.get('API_KEYS', 'twitch-token')
OPENAI_API_KEY = config.get('API_KEYS', 'openapi-key')
TWITCH_CLIENT_ID = config.get('API_KEYS', 'twitch-client-id')
# The Twitch channel you want your bot to join
CHANNEL_NAME = config.get('API_KEYS', 'twitch-channel')

# The message you want your bot to respond to
TARGET_MESSAGE = 'Salut'
TARGET_MESSAGE2 = 'Hello'
TARGET_MESSAGE3 = 'bonsoir'
TARGET_MESSAGE4 = 'lu!'
TARGET_MESSAGE5 = 'yo!'
TARGET_MESSAGE6 = 'yoyo'
TARGET_MESSAGE7 = 'yo'
openai.api_key = OPENAI_API_KEY

# Define a new bot
bot = commands.Bot(
    token=TOKEN,
    client_id=os.environ.get('CLIENT_ID', TWITCH_CLIENT_ID),
    nick=BOT_USERNAME,
    prefix='!',
    initial_channels=[CHANNEL_NAME]
)
class Bot(commands.Bot):

    start_time = 0

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=TOKEN,client_id=os.environ.get('CLIENT_ID', TWITCH_CLIENT_ID),nick=BOT_USERNAME,prefix='!',initial_channels=[CHANNEL_NAME])

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

    # Listen for the target message and respond to it
    async def event_message(self, message):
        if message.echo:
            return
        if (message.content.lower().__contains__(TARGET_MESSAGE.lower()) or \
            message.content.lower() == TARGET_MESSAGE7.lower() or \
            message.content.lower().__contains__(TARGET_MESSAGE2.lower()) or \
            message.content.lower().__contains__(TARGET_MESSAGE3.lower()) or \
            message.content.lower().__contains__(TARGET_MESSAGE4.lower()) or \
            message.content.lower().__contains__(TARGET_MESSAGE6.lower()) or \
            message.content.lower().__contains__(TARGET_MESSAGE5.lower())) and not message.content.lower().__contains__(BOT_USERNAME):
            time.sleep(4.4)
            await self.handle_hello_message(message)
            print('\n Greetings')
        if (message.content.lower().__contains__(BOT_USERNAME.lower()) and len(message.content) > 30 and (time.perf_counter() - self.start_time) > 20):
            time.sleep(2.4)
            self.start_time = time.perf_counter()
            m = message.content.lower().replace('@' + BOT_USERNAME, BOT_USERNAME)
            inputStr = 'Repond à la question en maximum 200 caractères : ' + m
            systemData = {}
            systemData['role'] = "system"
            systemData['content'] = "Tu es " + BOT_USERNAME  + ", donnant des réponses concises et précises à des questions qui te sont posées."
            data = {}
            data['role'] = "user"
            data['content'] = inputStr
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                temperature=1.2,
                messages = [systemData,data])
            await self.handle_gpt_message(message, response['choices'][0]['message']['content'])

    
    # Define a function to handle the bot's response
    async def handle_hello_message(self, message):
        await message.channel.send(f"Hello {message.author.name}! HeyGuys ")
        
    # Define a function to handle the bot's response
    async def handle_gpt_message(self, message, response):
        print(response)
        await message.channel.send('@' + message.author.name + ' ' + response)

bot = Bot()
bot.run()
