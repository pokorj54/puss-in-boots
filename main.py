from asyncio import events
import discord
import my_secret_token

TOKEN = my_secret_token.get_token()


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Logged in as {}'.format(client.user))


cat_words = ['cat', 'kitty', 'puss']

@client.event 
async def on_message(message):
    msg = str(message.content)
    for w in cat_words:
        if w in  msg:
            await message.add_reaction('🐈')

client.run(TOKEN)