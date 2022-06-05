import discord
def get_help(topic):
    if topic == 'main':
        embed = discord.Embed(
            color=discord.Color.random(),
            title='Commands',
            description='For more info about a command, use `/help [command]`'
        )
        usage = '`hello`, `help`, `roll`, `8ball`, `invite`, `ping`'
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
        usage = '/help [command]*'
    elif topic == 'invite':
        embed = discord.Embed(
            color=discord.Color.random(),
            title='Invite',
            description='Gives the invite link of the bot.'
        )
        usage = '/invite'
    elif topic == 'roll':
        embed = discord.Embed(
            color=discord.Color.random(),
            title='Roll',
            description='Rolls the dice based on the number you select.'
        )
        usage = '/roll [integer]'
    elif topic == 'ping':
        embed = discord.Embed(
            color=discord.Color.random(),
            title='Ping',
            description='Tests the latency of the bot.'
        )
        usage = '`/ping`'
    return embed, usage