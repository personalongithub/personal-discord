import discord
def get_help(topic):
    if topic == 'main':
        embed = discord.Embed(
            color=discord.Color.random(),
            title='Commands',
            description='For more info about a command, use `/help [command]`',
        )
        usage = '`hello`, `help`, `roll`, `8ball`, `invite`'
    elif topic == 'hello':
        embed = discord.Embed(
            color=discord.Color.random(),
            title='Hello',
            description='Says hello!',
        )
        usage = '`/hello`'
    else:
        pass
    return embed, usage
    