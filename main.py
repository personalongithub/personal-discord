"""Main script for the bot."""
import os
import random

import discord
from geopy.geocoders import Nominatim
from resources import eight_ball, help_docs, variables

bot = discord.Bot()


@bot.event
async def on_ready():
    """An action after the bot is ready to use."""
    print(f'The bot has successfully logged in as {bot.user}')


@bot.slash_command(description='Says hello!')
async def hello(ctx: discord.ApplicationContext):
    """Says hello!"""
    await ctx.respond(f'Hello, {ctx.author.name}!')


@bot.slash_command(name='help', description='Shows help options for commands')
@discord.option('topic',
                description='Get help for a specific command',
                default='main',
                choices=['8ball', 'coordinate', 'hello', 'help', 'invite', 'ping', 'roll',
                'stringify'])
async def slash_help(ctx: discord.ApplicationContext, topic: str):
    """Shows help options for commands"""
    embed, usage = help_docs.get_help(topic)
    embed.add_field(name='List of Commands' if topic == 'main' else 'Usage', value=usage)
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
    await ctx.respond(embed=embed)


@bot.slash_command(description='Roll a die!')
@discord.option('number', description='Choose a number!', min_value=2, default=6)
async def roll(ctx: discord.ApplicationContext, number: int):
    """Roll a die!"""
    await ctx.respond(
        f'**{ctx.author.name}** rolled a **{random.randint(1, number)}**! (1-{number}) :game_die:')


@bot.slash_command(name='8ball', description="What's your fortune?")
@discord.option('question', description='Ask your question!')
async def c_eight_ball(ctx: discord.ApplicationContext, question: str):
    """What's your fortune?"""
    embed = discord.Embed(
        color=discord.Color.random(),
        title='Magic 8-Ball :8ball:',
    )
    embed.add_field(name=question, value=eight_ball.eight_ball(question))
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
    await ctx.respond(embed=embed)


@bot.slash_command(name='invite', description='Invite the bot to a server!')
async def invite(ctx: discord.ApplicationContext):
    """Invite the bot to a server!"""
    embed = discord.Embed(color=discord.Color.random(), title='Invite the bot!')
    embed.add_field(name='Invite Personal to a server',
                    value='**[Personal Invite Link](https://discord.com/api/oauth2/authorize'\
                        '?client_id=954564559467868171&permissions=274877908992&scope=bot'\
                        '%20applications.commands)**')
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
    await ctx.respond(embed=embed)


@bot.slash_command(description='Test the latency of the bot!')
async def ping(ctx: discord.ApplicationContext):
    """Test the latency of the bot!"""
    await ctx.respond(f'Pong! :ping_pong:  Latency is {round(bot.latency * 1000)}ms')


@bot.slash_command(description='Grab the coordinates of a location.')
@discord.option('location', description='This location is used for grabbing coordinates.')
@discord.option('privacy',
                description="Sends the location privately so that others don't see it.",
                default=False)
async def coordinate(ctx: discord.ApplicationContext, location: str, privacy: bool):
    """Grab the coordinates of a location."""
    try:
        location_info = Nominatim(user_agent='Personal Discord Bot').geocode(location)
        await ctx.respond(
            'The coordinates for this location are '\
            f'**({location_info.latitude}, {location_info.longitude})** :map:',
            ephemeral=bool(privacy))
    except AttributeError:
        await ctx.respond(
            'We have failed to get coordinates for this location!',
            ephemeral=bool(privacy))

@bot.slash_command(description='Make a random string of characters of any length')
@discord.option('length', description='How long will your string be?', min_value=1, max_value=2048)
async def stringify(ctx: discord.ApplicationContext, length: int):
    """Makes a random string that is a select amount of characters."""
    string = ''
    for i in range(length):
        string += random.choice(variables.STRING_SET)
        del i
    await ctx.respond(string)


bot.run(os.environ['DISCORD_TOKEN'])
