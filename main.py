import discord,os,json
from json import load
from discord.ext import commands


with open('setting.json') as f:
    config = json.load(f)

token = config.get('token')
name = config.get('name')
url = config.get('twitch')


bot = commands.Bot(command_prefix="!",Self_bot=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

@bot.event
async def on_ready():
    print(f" STATUS LOGIN DISCORD USERNAME >  {bot.user}")
    clear()
    print(f" STATUS STREAMING RUNNING ! {bot.user}")
    await bot.change_presence(activity=discord.Streaming(name=name, url=url,emoji='🖥️'))


bot.run(token,bot=False)