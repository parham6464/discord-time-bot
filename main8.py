#-----------imports & froms-----------
import discord
from discord.ext import commands, tasks
from datetime import datetime
import asyncio
import pytz
from dotenv import load_dotenv
from os import getenv
import jdatetime
from deep_translator import GoogleTranslator
#-----------imports & froms-----------

client = commands.Bot(command_prefix='!!!',
                      intents=discord.Intents.all(),
                      case_insensitive=True,
                      self_bot=True)

load_dotenv()
TOKEN = getenv('TOKEN')

@tasks.loop()
async def status_task():
    await client.change_presence(status=discord.Status.online , activity=discord.Activity(type=discord.ActivityType.watching, name="parham-programming.ir"))
    await asyncio.sleep(1)
    await client.change_presence(status=discord.Status.idle ,activity=discord.Activity(type=discord.ActivityType.watching, name="APA Company"))
    await asyncio.sleep(1)
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="24/7"))
    await asyncio.sleep(1)


@client.event
async def on_ready():

    print(f'logged in as {client.user.name}')
    channel = client.get_channel(1136110442041839726)
    await channel.connect()
    status_task.start()

#----------time------------
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def calender(ctx):
    time_clocker.start(ctx)


@client.command()
@commands.has_permissions(administrator=True)
async def seprate(ctx):
    await ctx.message.delete()
    await ctx.send('https://media.discordapp.net/attachments/1109869978347380829/1125340569149919242/hive-didver1.gif')

@tasks.loop(hours=1)
async def time_clocker(ctx):
    sss=jdatetime
    fa_date =sss.datetime.now().strftime("%B %d")
    xc=GoogleTranslator(source='en', target='fa').translate(fa_date)
    await ctx.guild.me.edit(nick=f'تاریخ: {xc}')


#----------time------------
client.run(TOKEN)
