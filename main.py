import discord
import my_secret_token
import facts
from cat_pic_gatherer import CatPicGatherer
from general_gatherer import GeneralGatherer
from xkcd_gatherer import XkcdGatherer
from inspirobot_gatherer import InspirobotGatherer
import re

TOKEN = my_secret_token.get_token()


intents = discord.Intents.default()

client = discord.Client(intents=intents)

gatherers = [
    # CatPicGatherer(), # Cat
    # GeneralGatherer('https://randomfox.ca/floof/', ['image'], '🦊', ['fox']),
    GeneralGatherer('https://some-random-api.ml/img/bird', ['link'], '🐦', 'bird|birb'),
    GeneralGatherer('https://some-random-api.ml/img/dog', ['link'], '🐶', 'dog|pupp'),
    GeneralGatherer('https://some-random-api.ml/img/cat', ['link'], '🐈', 'cat|kitt|puss'),
    GeneralGatherer('https://some-random-api.ml/img/fox', ['link'], '🦊', 'fox'),
    GeneralGatherer('https://some-random-api.ml/img/raccoon', ['link'], '🦝','rac+o+n|trash panda'),
    GeneralGatherer('https://some-random-api.ml/img/panda', ['link'], '🐼', '(?<!(red|trash) )panda'),
    GeneralGatherer('https://some-random-api.ml/img/kangaroo', ['link'], '🦘', 'kangaroo'),
    GeneralGatherer('https://some-random-api.ml/img/koala', ['link'], '🐨', 'koala'),
    GeneralGatherer('https://some-random-api.ml/img/red_panda', ['link'], '🔴', 'red panda'),
    GeneralGatherer('https://some-random-api.ml/img/whale', ['link'], '🐋', 'whale'),
    GeneralGatherer('https://some-random-api.ml/img/pikachu', ['link'], '😲', 'pikachu'),
    GeneralGatherer('https://random-d.uk/api/v1/random?type=png', ['url'], '🦆', 'duck|quack'),
    GeneralGatherer('https://shibe.online/api/shibes?count=1', [0], '🦮', 'cheems|shiba'),
    GeneralGatherer('https://zoo-animal-api.herokuapp.com/animals/rand', ['image_link'], '🐵', 'animal|zoo'),
    GeneralGatherer('https://coffee.alexflipnote.dev/random.json', ['file'], '☕', 'coffee|kafi'),
    GeneralGatherer('https://api.yomomma.info/', ['joke'], '👩', 'yo ?mama|yo ?mamma|your ?mom'),
    GeneralGatherer('https://api.kanye.rest/', ['quote'], '🎤', 'kanye'),
    XkcdGatherer(),
    InspirobotGatherer()
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
    used = False
    if "fact" in msg:
        await message.channel.send(facts.get_fact())
        await message.add_reaction('📝')
        used = True
    for gatherer in gatherers:
        found = re.findall(gatherer.trigger_regex, msg, flags=re.IGNORECASE)
        for _ in range(min(len(found), 5)):
            await message.channel.send(gatherer.get())
            await message.add_reaction(gatherer.emote)
            used = True
    if "git" in msg:
        await message.channel.send("You can look me up at https://github.com/pokorj54/puss-in-boots. Contribution is welcomed.")
        used = True
    if 'list' in msg or not used:
        await message.channel.send("I can do: \n" + "".join([str(g.trigger_regex) + " -> " + g.emote + "\n" for g in gatherers]))

client.run(TOKEN)