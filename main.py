import discord
import os
import requests
import json
import random
from web_sever import web_server
from discord.ext import commands

bot = commands.Bot(command_prefix="p!")

# stuff happening on launch
@bot.event
async def on_ready():
  print(f"{bot.user} is alive!")

  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="p!info"))

# the oldest joke in the book
@bot.command()
async def tenie(message):
    await message.send('Era odata un om si avea o tenie de care nu putea sa scape.Disperat, merge la cel mai bun doctor din lume, doctorul de tenii.Il intreaba pe doctor daca il poate ajuta, iar doctorul ii raspunde "Bine, vino maine cu o banana si un biscuite".Curios, omul nostru vine urmatoarea zi, doctorul il apleaca pe masa si ii baga in fund banana si dupa aceea biscuitele. "Foarte bine, repetam tratamentul 2 saptamani!". Disperat, omul face tratamentul si la sfarsit doctorul ii spune "Maine e ultima zi, sa vii cu o banana si un ciocan." Speriat, vine omul urmatoarea zi, il apleaca doctorul pe masa, ii baga banana in fund si asteapta... si asteapta... la care iese tenia "Si biscuitele meu unde e?" si doctorul ii da un ciocan in cap si moare.')

# info command
@bot.command()
async def info(message):
  t = "Bot by AlphaPuffer"
  emb = discord.Embed(title = t, description = "Here's a list of all of the commands:", color=discord.Colour.from_rgb(242, 235, 34))
  emb.add_field(name = "p!rps [choice]",value = "Play a game of rock, paper, scissors!", inline = False)
  emb.add_field(name = "p!joke number",value = "Tells you the number of jokes Puffer Bot currently knows!", inline = False)
  emb.add_field(name = "p!joke [number]",value = "Tells you the joke with the selected number! If no number was chosen he'll tell you a random one.", inline = False)
  await message.send(embed = emb)

# rock paper scissors command
@bot.command()
async def rps(message, arg):
  choices = ['rock', 'paper', 'scissors']
  choice = random.choice(choices)
  outcome = ""
  if arg not in choices:
    await message.send("Input not valid, please try again!")
  else:
    if arg == choice:
      outcome = "It's a draw!" 
    elif arg == "rock" and choice == "paper" or arg == "paper" and choice == "scissors" or arg == "scissors" and choice == "rock":
        outcome = "You lost!"
    else:
        outcome = "You won!"
    result = discord.Embed(title="Rock paper scissors", description=outcome, color=discord.Colour.from_rgb(242, 235, 34))
    result.add_field(name="You picked", value=arg, inline=False)
    result.add_field(name="I picked", value=choice, inline=False)
    result.set_thumbnail(url="https://i.imgur.com/duOJoq2.png")
    await message.send(embed=result) 

# random/chosen jokes command
@bot.command()
async def joke(message, arg = None):
  jokes = [
"""
A man is told the local bank offers mortgages with no interest.
The man enters the bank.

Man: I’m here to find out about the mortgage.
Employee: I don’t really care.
""",
"""
What do sprinters eat before a race?

Nothing. They fast.
""",
"""
How many Buzzfeed employees does it take to operate an electric chair?

10, but 4 will shock you.
""",
"""
What does Jeff Bezos do right before bed time?

He puts his pjamazon.
""",
"""
You're riding a horse full speed, there's a giraffe beside you and you're being chased by a lion. What do you do?

Get your drunk ass off the carousel.
"""
  ]
  if arg:
    if arg == "number":
      t = "Currently Puffer Bot knows " + str(len(jokes)) + " jokes!"
      emb = discord.Embed(title = t, color=discord.Colour.from_rgb(242, 235, 34))
      await message.send(embed = emb)
    elif not arg.isdigit() or int(arg) > len(jokes) or int(arg)<= 0:
      t = "Joke number not valid, please try again!"
      emb = discord.Embed(title = t, color=discord.Colour.from_rgb(242, 235, 34))
      await message.send(embed = emb)
    else:
      t = "Joke No." + arg
      emb = discord.Embed(title = t, color=discord.Colour.from_rgb(242, 235, 34))
      emb.add_field(name = '\u200b' , value = jokes[int(arg)-1], inline=False)
      await message.send(embed = emb)
  else:
      nr = random.randint(1,len(jokes))
      t = "Joke No." + str(nr)
      emb = discord.Embed(title = t, color=discord.Colour.from_rgb(242, 235, 34))
      emb.add_field(name = '\u200b' , value = jokes[nr-1], inline=False)
      await message.send(embed = emb)
web_server()
bot.run(os.getenv('TOKEN'))