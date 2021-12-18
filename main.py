import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
a = 'OTIxMDQ1MTgyNjcyMTY2OTQy.YbtMK'
b = 'w.01UB_c96jyh6A0ZGSgLz0fKLqS4'
token = a + b
client.run(token)
