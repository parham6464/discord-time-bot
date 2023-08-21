#-----------imports & froms-----------
import discord
from discord.ext import commands, tasks
from datetime import datetime
import asyncio
import pytz
from dotenv import load_dotenv
from os import getenv
#-----------imports & froms-----------

client = commands.Bot(command_prefix='!!',
                      intents=discord.Intents.all(),
                      case_insensitive=True,
                      self_bot=True)

load_dotenv()
TOKEN = getenv('TOKEN')

@tasks.loop()
async def status_task():
    await client.change_presence(status=discord.Status.online , activity=discord.Activity(type=discord.ActivityType.watching, name="Programming Services"))
    await asyncio.sleep(1)
    await client.change_presence(status=discord.Status.idle ,activity=discord.Activity(type=discord.ActivityType.watching, name="main language:Python"))
    await asyncio.sleep(1)
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="24/7"))
    await asyncio.sleep(1)


@client.event
async def on_ready():
  
  print(f'logged in as {client.user.name}')
  channel = client.get_channel(1118935624402096268)
  await channel.connect()
  status_task.start()

#----------time------------
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def total_all(ctx):
  time_clocker.start(ctx)


@tasks.loop(minutes=1)
async def time_clocker(ctx):
  my_date = datetime.now(pytz.timezone('Asia/Tehran'))
  my_date = my_date.replace(second=0, microsecond=0)
  d = my_date.now()
  real_ir_time = d.strftime('%H:%M')
  await ctx.guild.me.edit(nick=f'Time : {real_ir_time}')


#----------time------------
client.run(TOKEN)
