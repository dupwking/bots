import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("으흠,나 뭐하지")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("ex/test"):
        await message.channel.send("test 확인!")

client.run("봇토큰")