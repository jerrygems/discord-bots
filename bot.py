import io
import discord
from numpy import *
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from discord.ext import commands
import pyfiglet as fig
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import random
import asyncio
import hashid
from Levenshtein import distance
import os
from fuzzywuzzy import fuzz
import pandas as pd
import matplotlib.pyplot as plt
import uuid
from PIL import Image, ImageDraw, ImageFont
import base64
import re
from dotenv import load_dotenv

load_dotenv()

def scrapereports():
    url = 'https://danielmiessler.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # find all elements with the class 'home-posts'
    elements = soup.find_all(class_='home-posts')

    # return the text of a random element from the list
    return random.choice(elements).text


# time

TOKEN = os.getenv('BOT_TOKEN')

client = commands.Bot(intents=discord.Intents.all(), command_prefix="!")


@client.event
async def on_ready():
    print("red")


@client.event
async def on_member_join(member):
    await member.guild.system_channel.send(
        "```fix\n" + fig.figlet_format(member.username, font="standard") + "hola mi amigo ¿cómo estás?```")
    print(f" " + member.username + " just joined ")


# @client.event
# async def on_member_join(ctx):
#     await ctx.send("{ctx.member} hola mi amigo ¿cómo estás?")


@client.command()
async def GreyMatter(ctx):
    await ctx.send("`it's GreyMatter how can i help you`")


@client.command()
async def sayTime(ctx):
    await ctx.send(
        "```fix\r#the time right now is ;-) \n" + fig.figlet_format(datetime.now().strftime("%H h : %M m : %S s"),
                                                                    font="standard") + "```")


@client.command()
async def sayDate(ctx):
    await ctx.send("```fix\r#the date today is ;-) \n" + fig.figlet_format(datetime.now().strftime("%d:%m:%Y"),
                                                                           font="standard") + "```")


@client.command()
async def solveIt(ctx, equation: str):
    try:
        result = str(eval(equation))
        await ctx.send("```fix\r" + fig.figlet_format(result, font="standard") + "```")
    except Exception as e:
        await ctx.send("```fix\r" + fig.figlet_format("Sorry equation can't be evaluated", font="standard") + "```")
        print(e)


@client.command()
async def writeIt(ctx, words: str):
    result = str(words)
    await ctx.send("```fix\r" + fig.figlet_format(result, font="standard") + "```")


@client.command()
@commands.has_permissions(administrator=True)
async def clearIt(ctx):
    await ctx.channel.purge()


@client.command()
async def trend(ctx):
    await ctx.send("``` " + str(scrapereports()) + "```")


@client.command()
async def Commands(ctx):
    await ctx.send(
        "```fix\n well! as every bot has some commands i also have commands\n hit !Commands to list out commands\n1. !trend \n2. !sayTime \n3. !solveIt (expression) \n4. !sayDate \n5. !help \n"
        "6. !writeIt\n7. !clearIt(admins only Xd) \n8. !askPuzzle (maths/logical) \n"
        "9. !describeCsv column_x column_y C:/Users/path/to/file.csv \n10. !plotIt valid_expression\n"
        "11. !describeColumn col_name C:/Users/path/to/file.csv \n"
        "12. !predictIt <features the you wanna predict with> <target that you actually wanna predict> <file_path>\n"
        ";-) exp: !predictIt feature_1 feature_2 predictValue C:/Users/path/to/file.csv\n"
        "13. coming soon```")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("```arm\n" + fig.figlet_format("404 command not found", font="standard") + "```")


@client.command()
async def askPuzzle(ctx, ans: str):
    def is_nearly_correct(user_input, correct_answer):
        if distance(user_input, correct_answer) <= 2:  # or you can use any threshold you want
            return True
        return False

    mathsque = [["If the sum of two numbers is 15 and one number is 9, what is the other number?", "6"],
                [
                    "If a train travels 60 miles per hour and you want to determine how far it will travel in 4 hours, what calculation would you use?",
                    "240 miles"],
                ["The sum of two consecutive numbers is 73. What are the numbers?", "36,37"],
                [
                    "If the sum of two numbers is 50 and one number is 25, what is the other number?" "The sum of three consecutive numbers is 45. What are the numbers?",
                    "15,16,17"],
                [
                    "If the sum of the squares of two numbers is 200 and the sum of the numbers is 20, what are the two numbers?",
                    "0,20"],
                [
                    "If the sum of two numbers is 45 and the ratio of the larger number to the smaller number is 3:2, what are the two numbers?",
                    "18 and 27"],
                ["If the sum of two numbers is 60, what is the sum of the squares of the numbers?", "3600"],
                ["The sum of two numbers is 40, and one number is twice the other. What are the two numbers?",
                 "40/3 and 80/3"]]
    logicalque = [["What's nowhere but everywhere, except where something is?\n answer:{*******}", "nothing"],
                  ["What's green and then red?\nanswer:{****s in a *******}", "frogs in a blender"],
                  ["What's strong enough to smash ships but still fears the sun?\nanswer:{***}", "ice"],
                  ["A diamond plate, a glowing grate, a place you never leave. Where am I?\nanswer:{****}", "home"],
                  [" I'm strong as a rock, but a word can destroy me. What am I?\nanswer:{*******}", "silence"],
                  ["What do you call a tavern of blackbirds?\nanswer:{*******}", "crowbar"],
                  ["Without fingers I point, without arms I strike, without feet I run. What am I?\nanswer:{a *****}",
                   "a clock"],
                  ["What has to be broken before you can use it?\nanswer:{an ***}", "an egg"],
                  ["What starts with an E, ends with an E, but only contains one letter?\nanswer:{********}",
                   "envelope"],
                  ["What is full of holes but still holds water?\nanswer:{*****e}", "Sponge"],
                  ["What is always in front of you but can't be seen?\nanswer:{******}", "future"],
                  [
                      "I am the beginning of everything, the end of everywhere. I am the beginning of eternity, the end of time and space. What am I?\nanswer:{answer in sigle letter}",
                      "e"],
                  [
                      "I am seen in the water if seen in the sky I am in the rainbow a mist is my mate. What am I?\nanswer:{a *****}",
                      "a cloud"],
                  ["I am a word that begins with T, ends with T, and has T in it. What am I?\nanswer:{******}",
                   "teapot"],
                  [
                      "I am light as a feather, but not even the strongest man can hold me for much longer than a minute. What am I?\nanswer:{**e**h}",
                      "breath"],
                  ["Forwards I am heavy; backwards I am not.\nanswer:{***}", "ton"],
                  [
                      "I can be broken without being held. Some people use me to deceive, but when delivered, I am the greatest gift of all.\nanswer:{a *******}",
                      "a promise"],
                  ["What three words are said too much, meant by few, wanted by all?\nanswer:{* **** ***}",
                   "i love you"],
                  [
                      "What can be stolen, mistaken, or altered, yet never leaves you your entire life?\nanswer:{your ********}",
                      "your identity"],
                  [
                      "The tallest trees fall, at my glorious call, some may resist, but only for so long. What am I?\nanswer{*******}",
                      "gravity"],
                  ["I can be a member of a group but I can never blend in.\nanswer{an **********}", "an individual"],
                  [
                      "I feel your every move, I know your every thought. I'm with you from birth and I'll see you when you rot.\nanswer{your **********}",
                      "your reflection"],
                  [
                      "I can sneak up on you or be right in front of you without you knowing. But when I reveal myself you will never be the same.\nanswer{*********}",
                      "betrayal"],
                  [
                      "A nightmare for some. For others, a savior I come. My hand's cold and bleak. It's the warm hearts they seek.\nanswer:{*e**h}",
                      "death"]]
    if ans == "logical":
        question00, correct00 = random.choice(logicalque)
        await ctx.send("```fix\n " + question00 + " ```")

        try:
            vary = await client.wait_for("message", timeout=30.0)
            if is_nearly_correct(vary.content, correct00) and vary.channel == ctx.channel:
                await ctx.send("```fix\nCongrats you're correct```")
            else:
                await ctx.send("```fix\nHey pal! sorry to say but you know what, you didn't get it```")
        except asyncio.TimeoutError:
            await ctx.send("```fix\nHey! you're late now time's gone, save you're answer for later```")
    elif ans == "maths":
        question11, correct11 = random.choice(mathsque)
        await ctx.send("```fix\n " + question11 + " ```")

        try:
            vary = await client.wait_for("message", timeout=30.0)
            if is_nearly_correct(vary.content, correct11) and vary.channel == ctx.channel:
                await ctx.send("```fix\nCongrats you're correct```")
            else:
                await ctx.send("```fix\nHey pal! sorry to say but you know what, you didn't get it```")
        except asyncio.TimeoutError:
            await ctx.send("```fix\nHey! you're late now time's gone, save you're answer for later```")
    else:
        await ctx.send("```fix\nnow you're here```")


@client.command()
async def whichHash(ctx, hash_value: str):
    try:
        hash_type = hashid.identify(hash_value.encode())
        await ctx.send("type of hash is : " + hash_type[0].name + "")
    except:
        await ctx.send("Couldn't identify the type of hash")


@client.command()
async def describeCsv(ctx, x: str, y: str, file_path: str):
    try:
        file = file_path
        print(file)
        df = pd.read_csv(file_path, encoding="utf-8")
        description = df.describe().to_string()
        await ctx.send(f"Data description:\n```\n{description}```")

        if x not in df.columns or y not in df.columns:
            raise ValueError(f"Column(s) '{x}' or '{y}' not found in the dataframe")

        filename = "images/" + str(uuid.uuid4()).replace("-", "") + ".png"
        plt.clf()
        plt.scatter(df[x], df[y])
        plt.savefig(filename)

        with open(filename, 'rb') as f:
            await ctx.send(file=discord.File(f))
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@client.command()
async def plotIt(ctx, expression: str):
    try:
        # Validate the expression using regular expressions
        pattern = r"^[-+*/\d\sx\(\)]+$"
        if not re.match(pattern, expression):
            raise Exception("Invalid characters in expression")

        # Define x as a variable and assign a value
        x = np.linspace(-10, 10, num=1000)

        # Use eval to evaluate the expression
        y = eval(expression)

        # Create the plot
        plt.clf()
        plt.plot(x, y)
        filename = "images/" + str(uuid.uuid4()).replace("-", "") + ".png"
        plt.savefig(filename)

        # Send the plot as a file to the Discord chat
        with open(filename, 'rb') as f:
            await ctx.send(file=discord.File(f))
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@client.command()
async def describeColumn(ctx, column_name: str, file_path: str):
    home_data = pd.read_csv(file_path.replace("\\", "\\\\"))

    X = home_data[column_name]

    await ctx.send("```fix\n " + X.describe().to_string() + " ```")


@client.command()
async def predictIt(ctx, *args):
    try:
        cols = args[:-1]
        file_path = args[-1]
        data = pd.read_csv(file_path.replace("\\", "\\\\"))
        features = [col for col in cols[:-1]]
        x = data[features]
        y = data[cols[-1]]
        my_model = DecisionTreeRegressor(random_state=1)
        my_model.fit(x, y)
        predictions = my_model.predict(x)

        # Plot the graph
        plt.clf()
        plt.plot(x.index, y, label='Actual')
        plt.plot(x.index, predictions, label='Predicted')
        plt.legend()
        filename = "images/" + str(uuid.uuid4()).replace("-", "") + ".png"
        plt.savefig(filename)

        # Send the plot as a file to the Discord chat
        with open(filename, 'rb') as f:
            await ctx.send(file=discord.File(f))
    except Exception as e:
        await ctx.send("An error occurred: " + str(e))


client.run(TOKEN)
