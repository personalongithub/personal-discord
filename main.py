import os, discord, random
from resources import help_docs, eight_ball
bot = discord.Bot()

@bot.event
async def on_ready(): 
    print(f'The bot has successfully logged in as {bot.user}')
    
@bot.slash_command(description='Says hello!')
async def hello(ctx):
    await ctx.respond(f'Hello, {ctx.author.name}!')

@bot.slash_command(description='Shows help options for commands')
@discord.option('topic', description='Get help for a specific command', default='main', choices=['8ball', 'hello', 'help', 'invite', 'main', 'ping', 'roll'])
async def help(ctx: discord.ApplicationContext, topic: str):
    embed, usage = help_docs.get_help(topic)
    embed.add_field(name='List of Commands' if topic == 'main' else 'Usage', value=usage)
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
    await ctx.respond(embed=embed)

@bot.slash_command(description='Roll a die!')
@discord.option('number', description='Choose a number!', min_value=2, default=6)
async def roll(ctx: discord.ApplicationContext, number: int):
    await ctx.respond(f'**{ctx.author.name}** rolled a **{random.randint(1, number)}**! (1-{number}) :game_die:')

@bot.slash_command(name='8ball', description="What's your fortune?")
@discord.option('question', description='Ask your question!')
async def c_eight_ball(ctx: discord.ApplicationContext, question: str):
    embed = discord.Embed(
        color=discord.Color.random(),
        title='Magic 8-Ball :8ball:',
    )
    embed.add_field(name=question, value=eight_ball.eight_ball(question))
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
    await ctx.respond(embed=embed)

@bot.slash_command(name='invite', description='Invite the bot to a server!')
async def invite(ctx: discord.ApplicationContext):
    embed = discord.Embed(
        color=discord.Color.random(),
        title='Invite the bot!',
    )
    embed.add_field(name='Invite Personal to a server', value='**[Personal Invite Link](https://discord.com/api/oauth2/authorize?client_id=954564559467868171&permissions=274877908992&scope=bot%20applications.commands)**')
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
    await ctx.respond(embed=embed)

@bot.slash_command(description='Test the latency of the bot!')
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond(f'Pong! :ping_pong:  Latency is {round(bot.latency * 1000)}ms')

bot.run(os.environ['DISCORD_TOKEN'])