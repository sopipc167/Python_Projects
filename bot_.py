import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("ready")
    game = discord.Game(name='', type=1)
    await client.change_presence(status=discord.Status.offline, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        if message.author.name != "아로니아_회의봇":
            await client.send_message(massage.chanel,"안녕하세요")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
