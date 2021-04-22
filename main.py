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
  await message.send('Work in progress\nBot by AlphaPuffer')

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

@bot.command()
async def play(message, url : str):
  pass
web_server()
bot.run(os.getenv('TOKEN'))