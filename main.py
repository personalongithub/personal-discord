import os, discord, random
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from eight_ball import eight_ball
client = commands.Bot(command_prefix = '$', help_command = None)
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready(): 
  print(f'We have logged in as {client.user}')
    
@client.command()
async def hello(ctx): 
  await ctx.send(f'Hello, {ctx.author.name}!')

@slash.slash(name='hello', description='Says hello!')
async def slash_hello(ctx): 
  await ctx.send(f'Hello, {ctx.author.name}!')

@client.command()
async def help(ctx):
  embed = discord.Embed(
    title = 'Help',
    description = 'For more info about a command, use `$help [command]`',
    color = discord.Color.random(),
  )
  embed.set_footer(text = f'Requested by {ctx.author}', icon_url = ctx.author.avatar_url)
  embed.add_field(name='Commands', value='`hello`, `help`, `roll`, `8ball`, `invite`')
  await ctx.send(embed=embed)

@client.command()
async def roll(ctx, number=6): 
  await ctx.send(f'**{ctx.author.name}** rolled a **{random.randint(1, number)}**! (1-{number})')

@slash.slash(
  name = 'roll',
  description = 'Roll a die!',
  options = [
    create_option(
      name = 'number',
      description = 'Choose a number!',
      required = False,
      option_type = 4
    )
  ]
)
async def slash_roll(ctx:SlashContext, number:int=6): 
  await ctx.send(f'**{ctx.author.name}** rolled a **{random.randint(1, number)}**! (1-{number})')

@client.command(name='8ball')
async def eight_ball_command(ctx, *, question):
  try:
    embed = discord.Embed(
      title = 'Magic 8-Ball :8ball:',
      color = discord.Color.random()
    )
    embed.set_footer(text = f'Requested by {ctx.author}', icon_url = ctx.author.avatar_url)
    embed.add_field(name=question, value=eight_ball(question))
    await ctx.send(embed=embed)
  except: pass

@slash.slash(
  name = '8ball',
  description = "What's your fortune?",
  options = [
    create_option(
      name = 'question',
      description = 'Ask your question!',
      required = True,
      option_type = 3
    )
  ]
)
async def slash_eight_ball(ctx:SlashContext, question:str):
  embed = discord.Embed(
      title = 'Magic 8-Ball :8ball:',
      color = discord.Color.random()
    )
  embed.set_footer(text = f'Requested by {ctx.author}', icon_url = ctx.author.avatar_url)
  embed.add_field(name=question, value=eight_ball(question))
  await ctx.send(embed=embed)

@client.command()
async def invite(ctx):
  embed = discord.Embed(
    title = 'Invite the bot!',
    color = discord.Color.random()
  )
  embed.set_footer(text = f'Requested by {ctx.author}', icon_url = ctx.author.avatar_url)
  embed.add_field(name='Invite Personal to a server', value='**[Personal Invite Link](https://discord.com/api/oauth2/authorize?client_id=954564559467868171&permissions=274877908992&scope=bot%20applications.commands)**')
  await ctx.send(embed=embed)

client.run(os.environ['DISCORD_TOKEN'])