import discord
import my_secret_token
import facts


TOKEN = my_secret_token.get_token()


intents = discord.Intents.default()
intents.message_content = True

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

client.run(TOKEN)