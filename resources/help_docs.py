'Module for grabbing help topics.'
import discord


def get_help(topic):
    'Grabs a help topic'
    if topic == 'main':
        embed = discord.Embed(
            color=discord.Color.random(),
            title='Commands',
            description='For more info about a command, use `/help [command]`'
        )
        usage = '`hello`, `help`, `roll`, `8ball`, `invite`, `ping`, `coordinate`'
    elif topic == '8ball':
        embed = discord.Embed(
            color=discord.Color.random(),
            title='8-Ball',
            description='Grab your fortune with this Magic 8-Ball.'
        )
        usage = '`/8ball [question]`'
    elif topic == 'coordinate':
        embed = discord.Embed(
            color=discord.Color.random(),
            title='Coordinate',
            description='Grabs the coordinates of any location.'
        )
        usage = '`/coordinate [location] [privacy]*`'
    elif topic == 'hello':
        embed = discord.Embed(
            color=discord.Color.random(),
            title='Hello',
            description='Says hello!'
        )
        usage = '`/hello`'
    elif topic == 'help':
        embed = discord.Embed(
            color=discord.Color.random(),
            title='Help',
            description='Shows help information lmao'
        )
        usage = '`/help [command]*`'
    elif topic == 'invite':
        embed = discord.Embed(
            color=discord.Color.random(),
            title='Invite',
            description='Gives the invite link of the bot.'
        )
        usage = '`/invite`'
    elif topic == 'roll':
        embed = discord.Embed(
            color=discord.Color.random(),
            title='Roll',
            description='Rolls the dice based on the number you select.'
        )
        usage = '`/roll [integer]`'
    elif topic == 'ping':
        embed = discord.Embed(
            color=discord.Color.random(),
            title='Ping',
            description='Tests the latency of the bot.'
        )
        usage = '`/ping`'
    return embed, usage
