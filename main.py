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
    GeneralPicGatherer('https://randomfox.ca/floof/', ['image'], '🦊', ['fox']),
    GeneralPicGatherer('https://some-random-api.ml/img/birb', ['link'], '🐦', ['bird', 'birb']),
    GeneralPicGatherer('https://random-d.uk/api/v1/random?type=png', ['url'], '🦆', ['duck', 'quack']),
    GeneralPicGatherer('https://some-random-api.ml/img/raccoon', ['link'], '🦝', ['raccoon', 'racoon']),
    GeneralPicGatherer('https://some-random-api.ml/img/panda', ['link'], '🐼', ['panda']),
    GeneralPicGatherer('https://shibe.online/api/shibes?count=1"', [0], '🐶', ['cheems', 'doge', 'shiba'])
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