import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("아로니아 회의 보조")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        if message.author.name != "아로니아_회의봇":
            await message.channel.send("안녕하세요")


client.run("NjkzNDM0MDY3Mzg3MDIzNDIx.Xn9BEw._vJhcQNeE4R1UFFC4_F358AQ_oY")