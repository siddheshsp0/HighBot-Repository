#FOR TESTING

import config
TOKEN = config.TOKEN

# #FOR PUSHING TO GITHUB
# import os
# TOKEN = os.environ['DISCORD_API']



#-----------------------------------------#

import discord
from discord.ext import commands
import utils
import func

#globals
guilds = [886108558792470528, 767999484181217321, 885102811598176296, 888635182352064513]
pref = 'h?'
bot = commands.Bot(command_prefix = pref)



#main discord client stuff 

@bot.event
async def on_ready():
  print('Bot Started')


#if someone pings the bot
@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send(f'> Yo {message.author.mention}, use /help for help!')



# help command
@bot.slash_command(guild_ids=guilds)
async def help(ctx, *, command=None):
  member_avatar = ctx.author.avatar
  if member_avatar == None:
    member_avatar = utils.no_avatar
  if command == None:
    emb = discord.Embed(title='List of commands', description='List of our available commands!')

    for i in func.bot_function.list_of_commands.keys():
      if i != None:
        emb.add_field(name=f'`/{i}`', value=func.bot_function.list_of_commands[i].get_desc_ov()+'\n')
    emb.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=member_avatar)
    await ctx.respond(embed=emb)
    return

  if command in func.bot_function.list_of_commands.keys():
    if command == None:
      await ctx.respond(embed=discord.Embed(title='Command not found, use /help :frowning:'))
      return
    cmd_obj = func.bot_function.list_of_commands[command]
    emb = discord.Embed(title=f'`{cmd_obj.get_name()}`', description=cmd_obj.get_desc_main())
    perm = ''
    if cmd_obj.get_permissions() == None:
      perm=None
    else:
      for i in cmd_obj.get_permissions():
        perm = perm+i+', '

    emb.add_field(name='`Required Permissions: `', value=perm)
    emb.add_field(name='Usage: ', value=cmd_obj.get_use())
    emb.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=member_avatar)
    await ctx.respond(embed=emb)
  else:
    await ctx.respond(embed=discord.Embed(title='Command not found, use /help :frowning:'))
    return




# clear command
@bot.slash_command(guild_ids=guilds, aliases=['c'], description='Clear messages!')
@commands.has_permissions(manage_messages = True, administrator = True)

async def clear(ctx, amount='1', ):
  if amount.lower() == 'all':
    await ctx.respond('Clearing all messages!')
    count_msg = 0
    async for _ in ctx.channel.history(limit=None):
      count_msg += 1
    await ctx.channel.purge(limit = count_msg)
    # emb = discord.Embed(title = f'Succesfully deleted {amount} {count_msg}', description = ctx.author.mention)
    # # await ctx.respond(embed = emb)

    return


  try:
    int(amount)
  except:
    await ctx.respond('Give a valid number noob!')
    return

  await ctx.respond(f'Clearing {amount} messages!')

  real_amount = int(amount)+1
  await ctx.channel.purge(limit = real_amount)
  noofmsg = 'message' if amount == 1 else 'messages'
  emb = discord.Embed(title = f'Succesfully deleted {amount} {noofmsg}', description = ctx.author.mention, color=discord.Colour.red())
  await ctx.channel.send(embed = emb)




# Id command
@bot.slash_command(aliases=['info','id','whois'], guild_ids=guilds, name='info', description = 'Get info about anyone')
async def info_command(ctx, member:discord.Member):
  member_avatar = member.avatar
  if member_avatar == None:
    member_avatar = utils.no_avatar

  emb = discord.Embed(color=discord.Colour.red(), description = f'About {member.name}')
  emb.add_field(name='Name', value=member.name)
  emb.add_field(name='NickName', value=member.display_name, inline=False)
  emb.add_field(name='Full Name', value = str(member), inline=False)
  emb.add_field(name='ID', value=member.id, inline=False)

  emb.set_author(name=member.name, icon_url=member_avatar)
  emb.set_thumbnail(url = member_avatar)

  emb.set_footer(icon_url = ctx.author.avatar, text = f'Requested by {ctx.author.display_name}')

  await ctx.respond(embed=emb)



# food command
@bot.slash_command(guild_ids=guilds, name='eat', description='What do you want to eat?' )
async def eat(ctx,*,food:str):
  member_avatar = ctx.author.avatar
  if member_avatar == None:
    member_avatar = utils.no_avatar
  food = food.lower()
  menu_list = utils.menu_list
  statment = str
  try:
    statment = menu_list[food]
  except:
    emb = discord.Embed(title = 'That\'s not on menu :frowning:', description = 'use /menu for menu!', color=discord.Colour.green())
    await ctx.respond(embed=emb)
    return
  statment = menu_list[food]
  emb = discord.Embed(title=f'{ctx.author.display_name}{statment}', color=discord.Colour.green())
  await ctx.respond(embed=emb)

#menu command
@bot.slash_command(guild_ids=guilds, name='menu', description='Our Menu!')
async def menu(ctx,):
  menu_list = utils.menu_list
  emb = discord.Embed(title='Our Menu', description='use /eat to enjoy one of the meals!', color=discord.Colour.green())

  for item in menu_list:
    emb.add_field(name=item.capitalize(), value='\u200b')
  emb.set_footer(icon_url = ctx.author.avatar, text = f'Requested by {ctx.author.display_name}')

  await ctx.respond(embed=emb)







# For testing
bot.run (TOKEN)

