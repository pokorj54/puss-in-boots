import discord
import my_secret_token
import facts
import cat_pics
import fox_pics

TOKEN = my_secret_token.get_token()


intents = discord.Intents.default()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Logged in as {}'.format(client.user))


cat_words = ['cat', 'kitt', 'puss', 'kitties']
fox_words = ['fox']

@client.event 
async def on_message(message):
    msg = str(message.content).lower()
    if msg == '' or message.author == client.user:
        return
    await message.add_reaction('🐱')
    if "fact" in msg:
        await message.channel.send(facts.get_fact())
        await message.add_reaction('📝')
    for w in cat_words:
        if w in msg:
            await message.channel.send(cat_pics.get_pic())
            await message.add_reaction('🐈')
            break
    for w in fox_words:
        if w in msg:
            await message.channel.send(fox_pics.get_pic())
            await message.add_reaction('🦊')


client.run(TOKEN)