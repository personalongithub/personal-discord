import os, discord, random, eight_ball
bot = discord.Bot()

@bot.event
async def on_ready(): 
    print(f'We have logged in as {bot.user}')
    
@bot.slash_command(name='hello', description='Says hello!')
async def hello(ctx):
    await ctx.respond(f'Hello, {ctx.author.name}!')

@bot.slash_command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Help',
        description = 'For more info about a command, use `$help [command]`',
        color = discord.Color.random(),
    )
    embed.set_footer(text = f'Requested by {ctx.author}', icon_url = ctx.author.avatar_url)
    embed.add_field(name='Commands', value='`hello`, `help`, `roll`, `8ball`, `invite`')
    await ctx.respond(embed=embed)

@bot.slash_command(name = 'roll', description = 'Roll a die!')
@discord.option('number', description='Choose a number!', min_value=2, default=6)
async def slash_roll(ctx:discord.ApplicationContext, number:int):
    await ctx.respond(f'**{ctx.author.name}** rolled a **{random.randint(1, number)}**! (1-{number})')

@bot.slash_command(name = '8ball', description = "What's your fortune?")
@discord.option('question', description='Ask your question!')
async def slash_eight_ball(ctx:discord.ApplicationContext, question:str):
    embed = discord.Embed(
        title = 'Magic 8-Ball :8ball:',
        color = discord.Color.random(),
    )
    embed.set_footer(text = f'Requested by {ctx.author}', icon_url = ctx.author.avatar_url)
    embed.add_field(name=question, value=eight_ball.eight_ball(question))
    await ctx.respond(embed=embed)

@bot.slash_command(name='invite', description='Invite the bot to a server!')
async def invite(ctx):
    embed = discord.Embed(
        title = 'Invite the bot!',
        color = discord.Color.random(),
    )
    embed.set_footer(text = f'Requested by {ctx.author}', icon_url = ctx.author.avatar_url)
    embed.add_field(name='Invite Personal to a server', value='**[Personal Invite Link](https://discord.com/api/oauth2/authorize?client_id=954564559467868171&permissions=274877908992&scope=bot%20applications.commands)**')
    await ctx.respond(embed=embed)

bot.run(os.environ['DISCORD_TOKEN'])