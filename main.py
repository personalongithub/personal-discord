import os, discord, random, eight_ball
from discord.ext import commands
command = commands.Bot(command_prefix='$', help_command = None)
bot = discord.Bot()

@bot.event
async def on_ready(): 
    print(f'We have logged in as {bot.user}')
    
@command.command()
async def hello(ctx): 
    await ctx.send(f'Hello, {ctx.author.name}!')

@bot.slash_command(name='hello', description='Says hello!')
async def slash_hello(ctx): 
    await ctx.send(f'Hello, {ctx.author.name}!')

@command.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Help',
        description = 'For more info about a command, use `$help [command]`',
        color = discord.Color.random(),
    )
    embed.set_footer(text = f'Requested by {ctx.author}', icon_url = ctx.author.avatar_url)
    embed.add_field(name='Commands', value='`hello`, `help`, `roll`, `8ball`, `invite`')
    await ctx.send(embed=embed)

@command.command()
async def roll(ctx, number=6): 
    await ctx.send(f'**{ctx.author.name}** rolled a **{random.randint(1, number)}**! (1-{number})')

@bot.slash_command(name = 'roll', description = 'Roll a die!')
@discord.option('number', description='Choose a number!', min_value=1, default=6)
async def slash_roll(ctx:discord.ApplicationContext, number:int): 
    await ctx.send(f'**{ctx.author.name}** rolled a **{random.randint(1, number)}**! (1-{number})')

@command.command(name='8ball')
async def eight_ball_command(ctx, *, question):
    if len(question) > 0:
        embed = discord.Embed(
            title = 'Magic 8-Ball :8ball:',
            color = discord.Color.random()
        )
        embed.set_footer(text = f'Requested by {ctx.author}', icon_url = ctx.author.avatar_url)
        embed.add_field(name=question, value=eight_ball.eight_ball(question))
        await ctx.send(embed=embed)
    else:
        await ctx.send('You need a question in order to use this command!')

@bot.slash_command(name = '8ball', description = "What's your fortune?")
@discord.option('question', description='Ask your question!')
async def slash_eight_ball(ctx:discord.ApplicationContext, question:str):
    embed = discord.Embed(
        title = 'Magic 8-Ball :8ball:',
        color = discord.Color.random()
    )
    embed.set_footer(text = f'Requested by {ctx.author}', icon_url = ctx.author.avatar_url)
    embed.add_field(name=question, value=eight_ball.eight_ball(question))
    await ctx.send(embed=embed)

@command.command()
async def invite(ctx):
    embed = discord.Embed(
      title = 'Invite the bot!',
      color = discord.Color.random()
    )
    embed.set_footer(text = f'Requested by {ctx.author}', icon_url = ctx.author.avatar_url)
    embed.add_field(name='Invite Personal to a server', value='**[Personal Invite Link](https://discord.com/api/oauth2/authorize?client_id=954564559467868171&permissions=274877908992&scope=bot%20applications.commands)**')
    await ctx.send(embed=embed)

bot.run(os.environ['DISCORD_TOKEN'])