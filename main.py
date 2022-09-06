import discord
import my_secret_token
import facts
from cat_pic_gatherer import CatPicGatherer
from general_pic_gatherer import GeneralPicGatherer

TOKEN = my_secret_token.get_token()


intents = discord.Intents.default()

client = discord.Client(intents=intents)

pic_gatherers = [
    CatPicGatherer(), # Cat
    GeneralPicGatherer('https://randomfox.ca/floof/', ['image'], '🦊', ['fox']), # Fox
    GeneralPicGatherer('https://some-random-api.ml/img/birb', ['link'], '🐦', ['bird', 'birb']) ,# Bird
    GeneralPicGatherer('https://some-random-api.ml/img/raccoon', ['link'], '🦝', ['raccoon', 'racoon']) # Raccoon
]


@client.event
async def on_ready():
    print('Logged in as {}'.format(client.user))


@client.event 
async def on_message(message):
    msg = str(message.content).lower()
    if msg == '' or message.author == client.user:
        return
    await message.add_reaction('🐱')
    if "fact" in msg:
        await message.channel.send(facts.get_fact())
        await message.add_reaction('📝')
    for gatherer in pic_gatherers:
        for w in gatherer.trigger_words:
            if w in msg:
                await message.channel.send(gatherer.get_pic())
                await message.add_reaction(gatherer.emote)
                break

client.run(TOKEN)