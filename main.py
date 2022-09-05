import discord
import my_secret_token
import facts
import pics

TOKEN = my_secret_token.get_token()


intents = discord.Intents.default()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Logged in as {}'.format(client.user))


cat_words = ['cat', 'kitty', 'puss', 'kitties']

@client.event 
async def on_message(message):
    msg = str(message.content).lower()
    for w in cat_words:
        if w in  msg:
            await message.add_reaction('🐈')
            break
    if "fact" in msg:
        await message.channel.send(facts.get_fact())
    if "pic" in msg:
        await message.channel.send(pics.get_pic())

client.run(TOKEN)