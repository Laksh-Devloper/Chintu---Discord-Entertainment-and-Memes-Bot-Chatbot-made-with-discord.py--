'''
Made By LAKSH

A Simple Personal Fun Bot for Fun Commands

Jump to testing Section - 684 / 700 apx

'''

# Importing Required Packages - START

import os

# os.system("pip install -U discord.py[voice]")
# os.system("pip install -U discord-py-interactions")

import discord
from discord import app_commands
from discord.ext import commands
from discord import interactions
import asyncio
import random
import datetime
import requests
import json
import requests
import pyjokes
import wikipedia
from PIL import Image, ImageDraw
from io import BytesIO

from keep_alive import keep_alive
import aiohttp


# Defining Important Parametres -- START

intents = discord.Intents.default()
intents.message_content = True

# Main Code --- START MAIN CODE

bot = commands.Bot(command_prefix='>', intents=intents)


# On Ready
@bot.event
async def on_ready():
   
    print("Ready!")


# Slash Commands


@bot.command()
async def sync(ctx):
    print("sync command")
    if ctx.author.id == 777799198057431062:
        await ctx.bot.tree.sync()
        await ctx.send('Command tree synced. [ Syncing May Take Time Upto 1 Hour Due to Discord Ratelimits]')
    else:
        await ctx.send('You must be the owner to use this command!')


@bot.tree.command(
    name="help",
    description="Presents all the commands available for the bot",
     )
async def help(interaction):

    em = discord.Embed(title='Developer : ',
                       description="Laksh_pro#7211",
                       color=discord.Color.purple())

    em.add_field(
        name="About : ",
        value=
        "The Legend Chintu is  here to satisfy all your needs, ahh not that need... Entertainment , Fun , Memes and Many More. Enjoy "
    )

    em.add_field(
        name="Support : ",
        value=
        f"[Invite](https://discord.com/api/oauth2/authorize?bot__id=843024379806089247&permissions=8&scope=bot)"
    )

    em.add_field(name="Help : ",
                 value=" use help <title> to know its commands. ")

    em.add_field(
        name="Title : ",
        value="🔴 Fun \n🟠 Meme \n🟢 Giveaway \n🔵 Other \n🟣 Game \n🟤 Chatbot\n")

    em.add_field(
        name="\n📰 Latest News : ",
        value=
        "🆕 Chatbot is now ```AVAILABLE``` with a new feature . Check ```>help chatbot``` for details and start chatting with chintu-chatbot now :)\n"
    )

    em.add_field(
        name="Commands : ",
        value=
        "joke , wanted , worthless , rolldice , flipcoin , stare , anger , choice , noob,insult , f  , pp , howhot , howgay , howhorny , howcool , gender ,dark , invite , gsearch , avatar , fuxk_u ,  getlink, roast , hack , iqcalc , say , rate"
    )

    await interaction.response.send_message(embed=em)


@bot.tree.command(name="f",
                  description="Pay respect command",
                   )
@commands.cooldown(3, 10, commands.BucketType.user)
async def f(interaction):
    await interaction.response.send_message(
        f"{user.mention} You paid respect, Keep it up")


@bot.tree.command(name="gender",
                  description="Generate random gender",
                   )
@commands.cooldown(3, 10, commands.BucketType.user)
async def gender(interaction, name: discord.Member = None):
    gen = ["Male", "Female"]
    rgender = random.choice(gen)
    if name == None:
        name = interaction.author
        em = discord.Embed(title="Gender Guesser",
                           description=f"{name.mention}'s Gender is  " +
                           rgender,
                           color=discord.Color.purple())
        await interaction.response.send_message(embed=em)
    else:
        em = discord.Embed(title="Gender Guesser",
                           description=f"{name.mention}'s Gender is  " +
                           rgender,
                           color=discord.Color.purple())
        await interaction.response.send_message(embed=em)


# TEST COMMAND -- START

# @bot.tree.command(name = "test", description = "Trying Buttons",  )
# async def test(interaction):
#     b1 = Button(label="Click" , style= discord.ButtonStyle.primary)
#     v = View()
#     v.add_item(b1)
#     await interaction.response.send_message("Hello!" , v)

# END


@bot.tree.command(name="invite",
                  description="Sends the invite link for the bot",
                   )
async def invite_command(interaction):

    em = discord.Embed(
        title="Invite The Bot : ",
        description=
        f"Thanks For inviting this bot \nInvite Link : https://discord.com/api/oauth2/authorize?bot_id=843024379806089247&permissions=8&scope=bot",
        color=discord.Color.yellow())
    await interaction.response.send_message(embed=em)


@bot.tree.command(name="flip_coin",
                  description="Flips A coin",
                   )
async def flip_coin(interaction):
    rint = random.randint(0, 1)
    if rint == 0:
        coin = "Head"
    elif rint == 1:
        coin = "Tail"
    em = discord.Embed(title="Coin Flipped : ",
                       description=f"It's a {coin}",
                       color=discord.Color.green())
    await interaction.response.send_message(embed=em)


import random
import re
import greetings


class ChatbotAI:
    def __init__(self):
        self.training_data = []

    def train(self, training_data):
        self.training_data = training_data

    def generate_response(self, user_input):
        response = "Sorry, I'm not sure how to respond to that."

        # Find the best matching pattern in the training data
        best_match = None
        max_match_score = 0
        for pattern, answer in self.training_data:
            match_score = self.calculate_match_score(user_input, pattern)
            if match_score > max_match_score:
                max_match_score = match_score
                best_match = answer

        # Generate a response based on the best matching pattern
        if best_match:
            response = best_match

        return response

    def calculate_match_score(self, user_input, pattern):
        # Calculate a match score based on keyword matching
        user_words = re.findall(r'\w+', user_input.lower())
        pattern_words = re.findall(r'\w+', pattern.lower())
        common_words = set(user_words) & set(pattern_words)
        match_score = len(common_words)
        return match_score

chatbot = ChatbotAI()
chatbot.train(greetings.training_data)

@bot.tree.command(name="chat",
                  description="Chat With AI",
                   )
async def chat(interaction, message: str):
    response = chatbot.generate_response(message)
    await interaction.response.send_message(response)





# SLASH COMMAND WITH APIs -- START

@bot.tree.command(name="joke",
                  description="Gives a random Joke",
                   )
@commands.cooldown(3, 10, commands.BucketType.user)
async def joke(interaction):

    try:
        url = "https://dad-jokes.p.rapidapi.com/random/joke"
        headers = {
            "X-RapidAPI-Key":
            "", # Get API KEY from Rapid-APi
            "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers)
        response_json = json.loads(response.text)
        body = response_json['body'][0]
        setup = body['setup']
        punchline = body['punchline']

        await interaction.response.send_message(setup + " , " + punchline)
    except Exception as e:
        await interaction.response.send_message(
            "Error Generating a Joke , try it later")


# PREFIX Commands ----- START




# * HELP COMMAND *

bot.remove_command("help")


@bot.group(invoke_without_command=True)
async def help(ctx, context=""):
    user = ctx.author
    em = discord.Embed(title='Developer : ',
                       description="Laksh_pro#7211",
                       color=discord.Color.purple())
    em.add_field(
        name="About : ",
        value=
        "The Legend Chintu is  here to satisfy all your needs, ahh not that need... Entertainment , Fun , Memes and Many More. Enjoy "
    )
    em.add_field(
        name="Support : ",
        value=
        f"[Invite](https://discord.com/api/oauth2/authorize?bot__id=843024379806089247&permissions=8&scope=bot)"
    )
    em.add_field(name="Help : ",
                 value=" use help <title> to know its commands. ")
    em.add_field(
        name="Title : ",
        value="🔴 Fun \n🟠 Meme \n🟢 Giveaway \n🔵 Other \n🟣 Game \n🟤 Chatbot\n")
    em.add_field(
        name="\n📰 Latest News : ",
        value=
        "🆕 Chatbot is now ```AVAILABLE``` with a new feature . Check ```>help chatbot``` for details and start chatting with chintu-chatbot now :)\n"
    )
    em2 = discord.Embed(title='Fun Commands 😆', color=discord.Color.purple())
    em2.add_field(
        name="Commands : ",
        value=
        "joke , insult , f  , pp , howhot , howgay , howhorny , howcool , gender , roast , hack , iqcalc , say , rate"
    )
    em3 = discord.Embed(title='Giveaway Commands 🥰',
                        color=discord.Color.green())
    em3.add_field(name="gstart : ", value="gstart [time] [prize]")
    em4 = discord.Embed(title='Other Commands 😊', color=discord.Color.blue())
    em4.add_field(name="Commands : ",
                  value="dark , invite , gsearch , avatar , getlink")
    em5 = discord.Embed(title='Meme Commands 😂', color=discord.Color.purple())
    em5.add_field(
        name="Commands : ",
        value=
        "wanted , worthless , stare , anger , choice , noob , fuxk_u , chuna_laga_diya , meri_taraf_mat_dekhiye , daring , scare_me , fire "
    )
    em6 = discord.Embed(title='Game Commands 🕹️', color=discord.Color.red())
    em6.add_field(name="Commands : ", value="rolldice , flipcoin")
    em7 = discord.Embed(title='Chatbot ', color=discord.Color.blue())
    em7.add_field(
        name="Setup : ",
        value=
        "New Feature Alert : To do this you have to add another bot ```chintu-chatbot```: https://discord.com/api/oauth2/authorize?bot _id=843492358997278760&permissions=522304&scope=bot \nThis is a extended feature of chintu bot. The prefix of ```chintu-chatbot``` will be ```c!``` Enjoy :)"
    )
    context = context.lower()

    # LOGIC -

    if context == "moderation":
        await ctx.send(embed=em1)
    elif context == "fun":
        await ctx.send(embed=em2)
    elif context == "giveaway":
        await ctx.send(embed=em3)
    elif context == "other":
        await ctx.send(embed=em4)
    elif context == "meme":
        await ctx.send(embed=em5)
    elif context == "game":
        await ctx.send(embed=em6)
    elif context == "chatbot":
        await ctx.send(embed=em7)

    else:
        await ctx.send(embed=em)


# HELP COMMAND -- END

# OTHER Commands

# NO API USAGE COMMANDS -- START


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
@commands.cooldown(3, 10, commands.BucketType.user)
async def hack(ctx, user: discord.Member = None):
    if user == None:
        await ctx.send("Who do you wanna hack fool.")
    else:
        email = [
            "chintuisbest@gmail.com", "strangerpgl@gmail.com",
            "angelpriya@gmail.com", "iamgirl@gmail.com",
            "secretlygay@gmail.com", "nogf@gmail.com",
            "oliverrisworstfruit@gmail.com", "whoisnoone@gmail.com"
        ]
        password = [
            "CHINTU_BOT_IS_BEST", "No One is dead", "i am chintu",
            "hentai_lover", "opgirl32"
        ]
        passr = random.choice(password)
        emair = random.choice(email)
        message = await ctx.send(f"Hacking {user.mention}")
        await asyncio.sleep(2)
        await message.edit(content="Accessing Discord Files")
        await asyncio.sleep(2)
        await message.edit(content="Blocking All GF's")
        await asyncio.sleep(2)
        await message.edit(content="No GF Found")
        await asyncio.sleep(2)
        await message.edit(content="Bypassing Discord Server")
        await asyncio.sleep(2)
        await message.edit(content=f"Successfully Hacked {user.mention}")
        await asyncio.sleep(2)
        await message.edit(
            content=
            f"{user.mention} Account is Now Hacked. \nEmail : {emair}\nPassword : {passr}"
        )


@bot.command()
async def mimic(ctx, target: discord.Member, *, message: str):
    # Create a webhook with the target's username and avatar
    avatar_url = target.avatar.url
    response = requests.get(avatar_url)
    await ctx.channel.purge(limit=1)
    webhook = await ctx.channel.create_webhook(name=target.name,
                                               avatar=response.content)

    # Send a message through the webhook
    async with aiohttp.ClientSession() as session:
        webhook_url = webhook.url
        payload = {"content": message}
        async with session.post(webhook_url, json=payload) as response:
            if response.status == 204:
                await ctx.message.add_reaction(
                    "\u2705")  # Successful response, add a green checkmark
            else:
                await ctx.message.add_reaction("\u274C"
                                               )  # Error response, add a red X

    # Delete the webhook
    await webhook.delete()


@bot.command()
@commands.cooldown(3, 10, commands.BucketType.user)
async def pp(ctx, name: discord.Member = None):
    if name == None:
        name = ctx.author
        pp = [
            "8===============D", "8=============D", "8============D",
            "8===========D", "8==========D", "8=========D", "8=========D",
            "8========D", "8=======D", "8======D", "8=====D", "8====D",
            "8===D", "8==D", "8=D", "8D"
        ]
        realpp = random.choice(pp)
        user = ctx.author
        em = discord.Embed(title="PP Size Guesser",
                           description=f"{name.mention}PP's size : " + realpp,
                           color=ctx.author.color)
        await ctx.send(embed=em)
    else:
        pp = [
            "8===============D", "8=============D", "8============D",
            "8===========D", "8==========D", "8=========D", "8=========D",
            "8========D", "8=======D", "8======D", "8=====D", "8====D",
            "8===D", "8==D", "8=D", "8D"
        ]
        realpp = random.choice(pp)
        user = ctx.author
        em = discord.Embed(title="PP Size Guesser",
                           description=f"{name.mention}PP's size : " + realpp,
                           color=ctx.author.color)
        await ctx.send(embed=em)


@bot.command()
@commands.cooldown(3, 10, commands.BucketType.user)
async def rolldice(ctx: interactions):
    roll = [1, 2, 3, 4, 5, 6]
    res = random.choice(roll)
    user = ctx.author
    message = await ctx.send(f"{user.mention} Rolled the Dice [:]")
    await asyncio.sleep(2)
    await message.edit(content="Dice is Rolling [::]")
    await asyncio.sleep(1)
    await message.edit(content="Dice is Rolling [::::]")
    await asyncio.sleep(1)
    await message.edit(content="Dice is Rolling [::::::]")
    await asyncio.sleep(2)
    await message.edit(content=f"The Number is {res}")


@bot.command()
@commands.cooldown(3, 10, commands.BucketType.user)
async def say(ctx, *, text=None):
    if text == None:
        await ctx.send("How can i say nothing , Fool * 100")
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send(text)


@bot.command(aliases=['flip'])
@commands.cooldown(3, 10, commands.BucketType.user)
async def flipcoin(ctx):
    flip = ["Head", "Tails"]
    flipr = random.choice(flip)
    message = await ctx.send(f"{ctx.author.mention} flipped coin")
    await asyncio.sleep(2)
    await message.edit(content=f"It's {flipr}")


@bot.command()
@commands.cooldown(3, 10, commands.BucketType.user)
async def rate(ctx, text=None):
    if text == None:
        await ctx.send("How can i rate nothing , Fool * 100")
    else:
        rate = random.randint(0, 10)
        await ctx.send(f"I will rate {text} as {rate}/10")


@bot.command()
@commands.cooldown(3, 10, commands.BucketType.user)
async def howhot(ctx, name: discord.Member = None):
    if name == None:
        name = ctx.author
        rhot = random.randint(0, 100)
        rhot = str(rhot)
        user = ctx.author
        em = discord.Embed(title="Hotness Calculator",
                           description=f"{name.mention} Hotness : " + rhot +
                           "% Hot",
                           color=ctx.author.color)
        await ctx.send(embed=em)
    else:
        rhot = random.radint(0, 100)
        rhot = str(rhot)
        user = ctx.author
        em = discord.Embed(title="Hotness Calculator",
                           description=f"{name.mention}Hotness : " + rhot +
                           "% Hot",
                           color=ctx.author.color)
        await ctx.send(embed=em)


@bot.command(aliases=['iqcalculator'])
@commands.cooldown(3, 10, commands.BucketType.user)
async def iqcalc(ctx, name: discord.Member = None):
    if name == None:
        name = ctx.author
        rhot = random.randint(0, 1000)
        rhot = str(rhot)
        user = ctx.author
        em = discord.Embed(title="IQ Calculator",
                           description=f"{name.mention} Smartness : " + rhot +
                           "% IQ",
                           color=ctx.author.color)
        await ctx.send(embed=em)
    else:
        rhot = random.radint(0, 1000)
        rhot = str(rhot)
        user = ctx.author
        em = discord.Embed(title="IQ Calculator",
                           description=f"{name.mention} Smartness : " + rhot +
                           "% IQ",
                           color=ctx.author.color)
        await ctx.send(embed=em)


@bot.command()
@commands.cooldown(3, 10, commands.BucketType.user)
async def howgay(ctx, name: discord.Member = None):
    if name == None:
        name = ctx.author
        rgay = random.randint(0, 100)
        rgay = str(rgay)
        user = ctx.author
        em = discord.Embed(title="Are you Gay ?",
                           description=f"{name.mention} Gayness : " + rgay +
                           "%  Gay",
                           color=ctx.author.color)
        await ctx.send(embed=em)
    else:
        rgay = random.randint(0, 100)
        rgay = str(rgay)
        user = ctx.author
        em = discord.Embed(title="Are you Gay ?",
                           description=f"{name.mention}gayness : " + rgay +
                           "%  Gay",
                           color=ctx.author.color)
        await ctx.send(embed=em)


@bot.command()
@commands.cooldown(3, 10, commands.BucketType.user)
async def howhorny(ctx, name: discord.Member = None):
    if name == None:
        name = ctx.author
        user = ctx.author
        rhorny = random.randint(0, 100)
        rhorny = str(rhorny)
        em = discord.Embed(title="You horny Bitch",
                           description=f"{name.mention} horniness : " +
                           rhorny + "% Horny",
                           color=ctx.author.color)
        await ctx.send(embed=em)
    else:
        user = ctx.author
        rhorny = random.randint(0, 100)
        rhorny = str(rhorny)
        em = discord.Embed(title="You horny B!tch",
                           description=f"{name.mention} horniness : " +
                           rhorny + "% Horny",
                           color=ctx.author.color)
        await ctx.send(embed=em)


@bot.command()
@commands.cooldown(3, 10, commands.BucketType.user)
async def howcool(ctx, name: discord.Member = None):
    if name == None:
        name = ctx.author
        rcool = random.randint(0, 100)
        rcool = str(rcool)
        user = ctx.author
        em = discord.Embed(title="Coolness Calculator",
                           description=f"{name.mention} Coolness : " + rcool +
                           "% Cool",
                           color=ctx.author.color)
        await ctx.send(embed=em)
    else:
        rcool = random.randint(0, 100)
        user = ctx.author
        rcool = str(rcool)
        em = discord.Embed(title="Coolness Calculator",
                           description=f"{name.mention} Coolness : " + rcool +
                           "% Cool",
                           color=ctx.author.color)
        await ctx.send(embed=em)


@bot.command()
@commands.cooldown(3, 10, commands.BucketType.user)
async def f(ctx):
    user = ctx.author
    await ctx.send(f"{user.mention} You paid respect , Keep it up")


# NO API USAGE COMMANDS -- END

# API USAGE COMMANDS -- START


@bot.command()
@commands.cooldown(3, 10, commands.BucketType.user)
async def joke(ctx):
    My_joke = pyjokes.get_joke(language="en", category="all")

    em = discord.Embed(title='Here is  your joke , Enjoy',
                       description=My_joke,
                       color=ctx.author.color)
    await ctx.send(embed=em)


@bot.command()
@commands.cooldown(3, 10, commands.BucketType.user)
async def insult(ctx, name: discord.Member = None):
    if name == None:
        name = ctx.author
        insult = requests.get(
            'https://evilinsult.com/generate_insult.php?lang=en&type=json')
        if insult.status_code == 200:
            insult = insult.json()['insult']
            user = ctx.author
            em = discord.Embed(title="Evil Insult Generator",
                               description=f"{name.mention} {insult}",
                               color=ctx.author.color)
            await ctx.send(embed=em)
    else:
        insult = requests.get(
            'https://evilinsult.com/generate_insult.php?lang=en&type=json')
        if insult.status_code == 200:
            insult = insult.json()['insult']
            user = ctx.author
            em = discord.Embed(title="Evil Insult Generator",
                               description=f"{name.mention} {insult}",
                               color=ctx.author.color)
            await ctx.send(embed=em)


@bot.command()
@commands.cooldown(3, 10, commands.BucketType.user)
async def roast(ctx, name: discord.Member = None):
    if name == None:
        name = ctx.author
        insult = requests.get(
            'https://evilinsult.com/generate_insult.php?lang=en&type=json')
        if insult.status_code == 200:
            insult = insult.json()['insult']
            user = ctx.author
            em = discord.Embed(title="Evil Insult Generator",
                               description=f"{name.mention} {insult}",
                               color=ctx.author.color)
            await ctx.send(embed=em)
    else:
        insult = requests.get(
            'https://evilinsult.com/generate_insult.php?lang=en&type=json')
        if insult.status_code == 200:
            insult = insult.json()['insult']
            user = ctx.author
            em = discord.Embed(title="Evil Insult Generator",
                               description=f"{name.mention} {insult}",
                               color=ctx.author.color)
            await ctx.send(embed=em)


# API USAGE COMMANDS -- END

# IMAGE MANIUPULATION -- START
@bot.tree.command(name="wanted" , description="wanted" ,  )
@commands.cooldown(3, 10, commands.BucketType.user)

async def wanted(interaction, user: discord.Member = None):
    if user is None:
        await interaction.response.send_message("Who do you want to mark as wanted? Please mention the user.")
    else:
        want = Image.open("wanted.jpg")
        avatar_url = user.avatar.url
        response =  requests.get(avatar_url)
        data = BytesIO(response.content)
        pfp = Image.open(data)
        pfp = pfp.resize((303, 302))
        want.paste(pfp, (72, 145))
        want.save("wantedp.jpg")
        await interaction.response.send_message(file=discord.File("wantedp.jpg"))

@bot.tree.command(name="fire" , description="burn into Fire" ,  )
@commands.cooldown(3, 10, commands.BucketType.user)

async def fire(interaction, user: discord.Member = None):
    if user is None:
        await interaction.response.send_message("Who do you want to create a fiery meme for? Please mention the user.")
    else:
        fire = Image.open("fire.png")
        avatar_url = user.avatar.url
        response =  requests.get(avatar_url)
        data = BytesIO(response.content)
        pfp = Image.open(data)
        pfp = pfp.resize((250, 260))
        fire.paste(pfp, (72, 145))
        fire.save("firep.png")
        await interaction.response.send_message(file=discord.File("firep.png"))

@bot.tree.command(name="meri_taraf_mat_dekhiye",    description="Create a 'meri taraf mat dekhiye' meme")

async def meri_taraf_mat_dekhiye(interaction, user: discord.Member):
    if user is None:
        await interaction.response.send_message("Who do you want to create a 'meri taraf mat dekhiye' meme for? Please mention the user.")
    else:
        meri_taraf = Image.open("meri_taraf_mat_dekhiye.jpg")
        avatar_url = user.avatar.url
        response =  requests.get(avatar_url)
        data = BytesIO(response.content)
        pfp = Image.open(data)
        pfp = pfp.resize((130, 130))
        meri_taraf.paste(pfp, (250, 135))
        meri_taraf.save("meri_taraf_p.jpg")
        await interaction.response.send_message(file=discord.File("meri_taraf_p.jpg"))

@bot.tree.command(description="Create a 'chuna laga diya' meme" ,  name="chuna_laga_diya" ,   )
async def chuna_laga_diya(interaction, user: discord.Member):
    if user is None:
        await interaction.response.send_message("Who do you want to create a 'chuna laga diya' meme for? Please mention the user.")
    else:
        chuna_laga = Image.open("chuna_laga_diya.webp")
        avatar_url = user.avatar.url
        response =  requests.get(avatar_url)
        data = BytesIO(response.content)
        pfp = Image.open(data)
        pfp = pfp.resize((130, 130))
        chuna_laga.paste(pfp, (275, 100))
        chuna_laga.save("chuna_laga_p.webp")
        await interaction.response.send_message(file=discord.File("chuna_laga_p.webp"))


@bot.tree.command(description="Create a 'fuxk u' meme" , name="fuxk_u",  )

async def fuxk_u(interaction, user1: discord.Member, user2: discord.Member):
    if user1 is None or user2 is None:
        await interaction.response.send_message("Who do you want to create a 'fuxk u' meme for? Please mention two users.")
    else:
        fuxk_u_img = Image.open("fuxk_u.jpg")
        avatar_url1 = user1.avatar.url
        avatar_url2 = user2.avatar.url
        response1 = await requests.get(avatar_url1)
        response2 = await requests.get(avatar_url2)
        data1 = BytesIO(response1.content)
        data2 = BytesIO(response2.content)
        pfp1 = Image.open(data1)
        pfp2 = Image.open(data2)
        pfp1 = pfp1.resize((100, 112))
        pfp2 = pfp2.resize((100, 112))
        fuxk_u_img.paste(pfp1, (220, 42))
        fuxk_u_img.paste(pfp2, (220, 500))
        fuxk_u_img.save("fuxk_u_p.jpg")
        await interaction.response.send_message(file=discord.File("fuxk_u_p.jpg"))

@bot.tree.command(description="Create a 'worthless' meme" , name="worthless"  ,  )

async def worthless(interaction, user: discord.Member):
    if user is None:
        await interaction.response.send_message("Who do you want to create a 'worthless' meme for? Please mention the user.")
    else:
        worthless_img = Image.open("worthless.jpg")
        avatar_url = user.avatar.url
        response =  requests.get(avatar_url)
        data = BytesIO(response.content)
        pfp = Image.open(data)
        pfp = pfp.resize((100, 100))
        worthless_img.paste(pfp, (170, 99))
        worthless_img.save("worthless_p.jpg")
        await interaction.response.send_message(file=discord.File("worthless_p.jpg"))

# ... (Previous code)

@bot.tree.command(description="Stare at two users" , name="stare",  )

async def stare(interaction, user1: discord.Member, user2: discord.Member):
    if user1 is None or user2 is None:
        await interaction.response.send_message("Who do you want to create a 'stare' meme for? Please mention two users.")
    else:
        stare_img = Image.open("stare.jpg")
        avatar_url1 = user1.avatar.url
        avatar_url2 = user2.avatar.url
        response1 = await requests.get(avatar_url1)
        response2 = await requests.get(avatar_url2)
        data1 = BytesIO(response1.content)
        data2 = BytesIO(response2.content)
        pfp1 = Image.open(data1)
        pfp2 = Image.open(data2)
        pfp1 = pfp1.resize((43, 42))
        pfp2 = pfp2.resize((43, 42))
        stare_img.paste(pfp1, (45, 42))
        stare_img.paste(pfp2, (110, 20))
        stare_img.save("stare_p.jpg")
        await interaction.response.send_message(file=discord.File("stare_p.jpg"))

@bot.tree.command(description="Add anger text to an image" , name="anger" ,  )

async def anger(interaction, text: str):
    anger_img = Image.open("anger.jpg")
    draw = ImageDraw.Draw(anger_img)
    font = ImageFont.truetype("ARIAL.TTF", 30)
    draw.text((405, 500), text, (0, 0, 0), font=font)
    anger_img.save("anger_p.jpg")
    await interaction.response.send_message(file=discord.File("anger_p.jpg"))

# ... (Continue defining other subcommands)


# ... (Previous code)

@bot.tree.command(description="Present two choices" , name="choice",   )

async def choice(interaction, choice1: str, choice2: str):
    choice_img = Image.open("choice.jpg")
    draw = ImageDraw.Draw(choice_img)
    font = ImageFont.truetype("ARIAL.TTF", 10)
    draw.text((14, 25), choice1, (10, 10, 10), font=font)
    draw.text((74, 15), choice2, (0, 0, 0), font=font)
    choice_img.save("choice_p.jpg")
    await interaction.response.send_message(file=discord.File("choice_p.jpg"))

@bot.tree.command(description="Create a 'noob' meme" , name="noob",    )

async def noob(interaction, user: discord.Member):
    if user is None:
        await interaction.response.send_message("Who do you want to create a 'noob' meme for? Please mention the user.")
    else:
        noob_img = Image.open("noob.jpg")
        avatar_url = user.avatar.url
        response =  requests.get(avatar_url)
        data = BytesIO(response.content)
        pfp = Image.open(data)
        pfp = pfp.resize((103, 102))
        noob_img.paste(pfp, (72, 145))
        noob_img.save("noob_p.jpg")
        await interaction.response.send_message(file=discord.File("noob_p.jpg"))

# ... (Continue defining other subcommands)


@bot.tree.command(description="Create a scary meme" , name="scare_me",   )
async def scare_me(interaction, user: discord.Member):
    if user is None:
        await interaction.response.send_message("Who do you want to create a scary meme for? Please mention the user.")
    else:
        scare = Image.open("scare_me.jpeg")
        avatar_url = user.avatar.url
        response =  requests.get(avatar_url)
        data = BytesIO(response.content)
        pfp = Image.open(data)
        pfp = pfp.resize((70, 80))
        scare.paste(pfp, (20, 105))
        scare.save("scarep.jpeg")
        await interaction.response.send_message(file=discord.File("scarep.jpeg"))

@bot.tree.command(description="Create a daring meme" , name="daring",   )
async def daring(interaction, user: discord.Member):
    if user is None:
        await interaction.response.send_message("Who do you want to create a daring meme for? Please mention the user.")
    else:
        daring = Image.open("dariing.jpg")
        avatar_url = user.avatar.url
        response =  requests.get(avatar_url)
        data = BytesIO(response.content)
        pfp = Image.open(data)
        pfp = pfp.resize((130, 130))
        daring.paste(pfp, (750, 105))
        daring.save("daringp.jpg")
        await interaction.response.send_message(file=discord.File("daringp.jpg"))



# IMAGE MANIPULATION -- END


# TESTING SECTION -- START


@bot.command()
@commands.cooldown(3, 10, commands.BucketType.user)
async def test(ctx, user: discord.Member = None):
    yas = '✔️'
    nay = '❌'
    game_embed = discord.Embed(title=f"Bola na TEST he ",
                               description='TEST',
                               color=discord.Color.purple())
    q = await ctx.send(embed=game_embed)
    await q.add_reaction(yas)
    await q.add_reaction(nay)

    valid_reactions = ['✔️', '❌']

    # def check(reaction, user):
    #     return user == ctx.author and str(reaction.emoji) in valid_reactions
    #     await bot.wait_for(reaction_add , timeout=60.0, check=check)

    #     if str(reaction.emoji) == yas:
    #         return await ctx.send('nice')
    #     else:
    #         await ctx.send("Cancelled")


# TESTING SECTION - END

# Error Handling :=


@bot.event
async def on_command_error(ctx, error):
    user = ctx.author
    mperms = discord.Embed(
        title="ERROR 404",
        description=
        f"{user.mention}, You don't have Permissions to do that. Go get some you idiot 😊",
        color=discord.Color.red())
    margu = discord.Embed(
        title="ERROR 404",
        description=
        f"{user.mention}, Wrong or Missing Argument Detected. go to play school again 😊",
        color=discord.Color.red())
    mrole = discord.Embed(
        title="ERROR 404",
        description=
        f"{user.mention}, You need a particular role for executing this command kid",
        color=discord.Color.red())
    mcool = discord.Embed(
        title="ERROR 404",
        description=
        f"{user.mention}, The Command Is in cooldown , pls try again in few seconds",
        color=discord.Color.red())

    if isinstance(error, commands.MissingPermissions):
        my_msg1 = await ctx.send(embed=mperms)
        await my_msg1.add_reaction("✔️")
    elif isinstance(error, commands.MissingRequiredArgument):
        my_msg2 = await ctx.send(embed=margu)
        await my_msg2.add_reaction("✔️")
    elif isinstance(error, commands.MissingRole):
        my_msg3 = await ctx.send(embed=mrole)
        await my_msg3.add_reaction("✔️")
    elif isinstance(error, commands.CommandOnCooldown):
        my_msg5 = await ctx.send(embed=mcool)
        await my_msg5.add_reaction("✔️")
    else:
        raise error


# Secret ---
keep_alive()  # KEEPING BOT ALIVE EVERYTIME
bot.run(os.environ.get('KEY'))  # KEY TOKEN 
