
import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime

Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="Here is some command for you", command_prefix=commands.when_mentioned_or("!!"), pm_help = False)


async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='marcos || !!help'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='with '+str(len(set(client.get_all_members())))+' users'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='in '+str(len(client.servers))+' servers'))
        await asyncio.sleep(5)
	
	
	
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started New here ')
    print('Created by MARCOS')
    client.loop.create_task(status_task())
	
def is_owner(ctx):
    return ctx.message.author.id == "498378677512437762" #replace_it_with_your_discord_id

def is_soyal(ctx):
    return ctx.message.author.id == "498378677512437762" 		

@client.event
async def on_message(message):
    channel = client.get_channel('519791076803084288')
    if message.server is None and message.author != client.user:
        await client.send_message(channel, '{} : <@{}> : '.format(message.author.name, message.author.id) + message.content)
    await client.process_commands(message)

@client.command(pass_context = True) #command_to_stop_your_bot_using-<prefix>shutdown
@commands.check(is_owner)
async def shutdown():
    await client.logout()
  
@client.command(pass_context=True, aliases=['em', 'e'])
async def modmail(ctx, *, msg=None):
    channel = discord.utils.get(client.get_all_channels(), name='📬mod-mails📬')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    color = discord.Color((r << 16) + (g << 8) + b)
    if not msg:
        await client.say("Please specify a message to send")
    else:
        await client.send_message(channel, embed=discord.Embed(color=color, description=msg + '\n Message From-' + ctx.message.author.id))
        await client.delete_message(ctx.message)
    return
	
@client.command()
async def servers():
  servers = list(client.servers)
  await client.say(f"Connected on {str(len(servers))} servers:")
  await client.say('\n'.join(server.name for server in servers))
 
	
@client.command(pass_context=True)
@commands.check(is_soyal)
async def botdm(ctx, user: discord.Member, *, msg: str):
    await client.send_typing(user)
    await client.send_message(user, msg)
	
@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def announce(ctx, channel: discord.Channel=None, *, msg: str):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(title="Announcement", description="{}".format(msg), color = discord.Color((r << 16) + (g << 8) + b))
    await client.send_message(channel, embed=embed)
    await client.delete_message(ctx.message)
	
client.run(os.getenv('Token'))
