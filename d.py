import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("bot is ready")
    print("We have logged in as {0.user}".format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def clear_all(ctx, amount=1000):
    await ctx.channel.purge(limit=amount)
    
@client.command()
async def clearall(ctx, amount=1000):
    await ctx.channel.purge(limit=amount)

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def emoji(message):
    if message.author == client.user:
        return 

    if message.content.startswith('test'):
        emoji = client.get_emoji(310177266011340803)
        await message.add_reaction(emoji)



client.run("NjgzMzUyODIzNTUwNzA1NjY1.XlqUlg.DBI47wv6w2m2PqU-QyRKwUwINDk")