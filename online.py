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
import requests
import json
import aiohttp		


Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="MultiVerse Official Bot", command_prefix=commands.when_mentioned_or("!!"), pm_help = True)
client.remove_command('help')



async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='!!help'))
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
	
@client.event
async def on_reaction_add(reaction, user):
  if reaction.message.server is None:
      if reaction.emoji == '😁':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='FUN COMMANDS')
        embed.add_field(name = 'SEE',value ='Sends donation link')
        my_msg = await client.send_message(user,embed=embed)
        await asyncio.sleep(30)
        await client.delete_message(my_msg)
        
      if reaction.emoji == '⚙':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='MODERATION COMMANDS')
        embed.add_field(name = 'SEE',value ='``m!dm @user <text>``, ``m!muteinchannel @user <time in minutes>``, ``m!setupwelcomer``, ``m!embed <text>``, ``m!role @user <rolename>``, ``m!setnick @user <New nickname>``, ``m!serverinfo``, ``m!userinfo @user``, ``m!lock #channel or mv!lock``, ``m!unlock #channel or mv!unlock``, ``m!membercount``, ``m!say <text>``, ``m!kick @user``, ``m!mute @user <time in minutes>``, ``m!unmute @user``, ',inline = False)
        react_message = await client.send_message(user,embed=embed)
        await client.add_reaction(react_message, reaction)
        await asyncio.sleep(30)
        await client.delete_message(react_message)
    
        
        
        
      if reaction.emoji == '👥':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='GENERAL COMMANDS')
        embed.add_field(name = 'SEE',value ='``m!help``, ``m!google <anything>``, ``mv!youtube <anything>``, ``m!botinvite``, ``m!ping``, ``m!serverinvite``, ``mv!avatar or mv!avatar @user``, ``m!meme``, ',inline = False)
        react_message = await client.send_message(user,embed=embed)
        await asyncio.sleep(30)
        await client.delete_message(react_message)
        
        
        
      if reaction.emoji == '⏱':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Emoji Help')
        embed.add_field(name = 'm!wow',value ='WOW emoji <a:WOW:515854429485006848>',inline = False)
        react_message = await client.send_message(user,embed=embed)
        await asyncio.sleep(30)
        await client.delete_message(react_message)
  else:
      if reaction.emoji == '🇻':
            role = discord.utils.get(user.server.roles, name='Verified')
            await client.add_roles(user, role)



@client.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.set_author(name='Help')
      embed.add_field(name = 'Having doubts? Join our server and clear your doubts. Server link:',value ='https://discord.gg/zxBfDY7',inline = False)
      embed.add_field(name = 'React with ⚙ ',value ='MODERATION COMMANDS.',inline = False)
      embed.add_field(name = 'React with 😁 ',value ='FUN COMMANDS.',inline = False)
      embed.add_field(name = 'React with 👥 ',value ='GENERAL COMMANDS',inline = False)
      embed.add_field(name = 'React with ⏱ ',value ='ANEMI COMMANDS',inline = False)
      dmmessage = await client.send_message(author,embed=embed)
      reaction1 = '⚙'
      reaction2 = '😁'
      reaction3 = '👥'
      reaction4 = '⏱'
      await client.add_reaction(dmmessage, reaction1)
      await client.add_reaction(dmmessage, reaction2)
      await client.add_reaction(dmmessage, reaction3)
      await client.add_reaction(dmmessage, reaction4)
      await client.say('I sent you the list of commands in a private message. Check your direct messages')
   
    
client.run(os.getenv('Token')) 
