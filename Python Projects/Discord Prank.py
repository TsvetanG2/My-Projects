import discord

client = discord.Client()

@client.event
async def on_connect():
    for user in client.user.friends:
        try:
            await.user.send('')
            print("Working with: {user.name}")
        except:
            print("No working on: {user.name}")
client.run("token", bot=False)
