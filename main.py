import discord
import my_secret_token
import facts
from cat_pic_gatherer import CatPicGatherer
from general_pic_gatherer import GeneralPicGatherer

TOKEN = my_secret_token.get_token()


intents = discord.Intents.default()

client = discord.Client(intents=intents)

pic_gatherers = [
    # CatPicGatherer(), # Cat
    # GeneralPicGatherer('https://randomfox.ca/floof/', ['image'], '🦊', ['fox']),
    GeneralPicGatherer('https://some-random-api.ml/img/birb', ['link'], '🐦', ['bird', 'birb']),
    GeneralPicGatherer('https://some-random-api.ml/img/dog', ['link'], '🐶', ['dog', 'pupp']),
    GeneralPicGatherer('https://some-random-api.ml/img/cat', ['link'], '🐈', ['cat', 'kitt', 'puss']),
    GeneralPicGatherer('https://some-random-api.ml/img/fox', ['link'], '🦊', ['fox']),
    GeneralPicGatherer('https://some-random-api.ml/img/raccoon', ['link'], '🦝', ['raccoon', 'racoon']),
    GeneralPicGatherer('https://some-random-api.ml/img/panda', ['link'], '🐼', ['panda']),
    GeneralPicGatherer('https://some-random-api.ml/img/kangaroo', ['link'], '🦘', ['kangaroo']),
    GeneralPicGatherer('https://some-random-api.ml/img/koala', ['link'], '🐨', ['koala']),
    GeneralPicGatherer('https://some-random-api.ml/img/red_panda', ['link'], '🔴', ['red panda']),
    GeneralPicGatherer('https://random-d.uk/api/v1/random?type=png', ['url'], '🦆', ['duck', 'quack']),
    GeneralPicGatherer('https://shibe.online/api/shibes?count=1', [0], '🦮', ['cheems', 'shiba']),
    GeneralPicGatherer('https://zoo-animal-api.herokuapp.com/animals/rand', ['image_link'], '🐵', ['animal', 'zoo'])
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
    for gatherer in pic_gatherers:
        for w in gatherer.trigger_words:
            if w in msg:
                await message.channel.send(gatherer.get_pic())
                await message.add_reaction(gatherer.emote)
                used = True
                break
    if "git" in msg:
        await message.channel.send("You can look me up at https://github.com/pokorj54/puss-in-boots. Contribution is welcomed.")
        used = True
    if 'list' in msg or not used:
        await message.channel.send("I can do: \n" + "".join([str(g.trigger_words) + " -> " + g.emote + "\n" for g in pic_gatherers]))

client.run(TOKEN)