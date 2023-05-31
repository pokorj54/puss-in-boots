import discord
import my_secret_token
import facts
from cat_pic_gatherer import CatPicGatherer
from general_gatherer import GeneralGatherer
from xkcd_gatherer import XkcdGatherer
from inspirobot_gatherer import InspirobotGatherer
from reddit_gatherer import RedditGatherer
import re

TOKEN = my_secret_token.get_token()


intents = discord.Intents.default()

client = discord.Client(intents=intents)

gatherers = [
    # CatPicGatherer(), # Cat
    # GeneralGatherer('https://randomfox.ca/floof/', ['image'], '🦊', ['fox']),
    GeneralGatherer('https://some-random-api.com/img/bird', ['link'], '🐦', 'bird|birb'),
    GeneralGatherer('https://some-random-api.com/img/dog', ['link'], '🐶', 'dog|pupp'),
    GeneralGatherer('https://some-random-api.com/img/cat', ['link'], '🐈', 'cat|kitt|puss|kat|gat|kot'),
    GeneralGatherer('https://some-random-api.com/img/fox', ['link'], '🦊', 'fox'),
    GeneralGatherer('https://some-random-api.com/img/raccoon', ['link'], '🦝','rac+o+n|trash panda'),
    GeneralGatherer('https://some-random-api.com/img/panda', ['link'], '🐼', '(?<!(..red|trash) )panda'),
    GeneralGatherer('https://some-random-api.com/img/kangaroo', ['link'], '🦘', 'kangaroo'),
    GeneralGatherer('https://some-random-api.com/img/koala', ['link'], '🐨', 'koala'),
    GeneralGatherer('https://some-random-api.com/img/red_panda', ['link'], '🔴', 'red panda'),
    GeneralGatherer('https://some-random-api.com/img/whale', ['link'], '🐋', 'whale'),
    GeneralGatherer('https://some-random-api.com/img/pikachu', ['link'], '😲', 'pikachu'),
    GeneralGatherer('https://random-d.uk/api/v1/random?type=png', ['url'], '🦆', 'duck|quack'),
    GeneralGatherer('https://shibe.online/api/shibes?count=1', [0], '🦮', 'cheems|shiba'),
    GeneralGatherer('https://api.bunnies.io/v2/loop/random/?media=mp4,av1', ['media', 'mp4'], '🐇', 'bunn|rabbit'),
    GeneralGatherer('https://zoo-animal-api.herokuapp.com/animals/rand', ['image_link'], '🐵', 'animal|zoo'),
    GeneralGatherer('https://coffee.alexflipnote.dev/random.json', ['file'], '☕', 'coffee|kafi'),
    GeneralGatherer('https://api.yomomma.info/', ['joke'], '👩', 'yo ?mama|yo ?mamma|your ?mom'),
    GeneralGatherer('https://api.kanye.rest/', ['quote'], '🎤', 'kanye'),
    XkcdGatherer(),
    InspirobotGatherer(),
    RedditGatherer('RATS','🐀','rat'),
    RedditGatherer('Otters','🦦','otter|ottie'),
    RedditGatherer('Rabbits','🐇','rabbit')
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