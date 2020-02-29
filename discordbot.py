import discord
from discord.ext import commands


client = discord.Client()
    




@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

    

@client.event
async def on_message(message):
    if message.author == client.user:
            return

    if message.content.startswith('point'):
        await message.channel.send('https://imgur.com/tGinjqI')
    
    if message.content.startswith('virgins'):
        await message.channel.send('https://imgur.com/6aK947c')

    if message.content.startswith('just'):
        await message.channel.send('https://imgur.com/tGinjqI https://imgur.com/6aK947c')
    
    if message.content.startswith('based'):
        await message.add_reaction('<:ok_hand:683371855020556329>')   
  
    
client.run("NjcyNTQwODIzNzExMTIxNDUw.XjYp0Q.ENI4EnqNZOWE3hazoGmSoYWBgik")