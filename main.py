import discord
import os
import requests
import json
import random
from web_sever import web_server
from discord.ext import commands

bot = commands.Bot(command_prefix="p!")

@bot.event
async def on_ready():
  print(f"{bot.user} is alive!")

  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to p!info"))

@bot.command()
async def tenie(message):
    await message.send('Era odata un om si avea o tenie de care nu putea sa scape.Disperat, merge la cel mai bun doctor din lume, doctorul de tenii.Il intreaba pe doctor daca il poate ajuta, iar doctorul ii raspunde "Bine, vino maine cu o banana si un biscuite".Curios, omul nostru vine urmatoarea zi, doctorul il apleaca pe masa si ii baga in fund banana si dupa aceea biscuitele. "Foarte bine, repetam tratamentul 2 saptamani!". Disperat, omul face tratamentul si la sfarsit doctorul ii spune "Maine e ultima zi, sa vii cu o banana si un ciocan." Speriat, vine omul urmatoarea zi, il apleaca doctorul pe masa, ii baga banana in fund si asteapta... si asteapta... la care iese tenia "Si biscuitele meu unde e?" si doctorul ii da un ciocan in cap si moare.')

@bot.command()
async def info(message):
  await message.send('Work in progress\nBot by AlphaPuffer')

@bot.command()
async def rps(message, arg):
  choices = ['rock', 'paper', 'scissors']
  choice = random.choice(choices)
  if arg == choice:
    result = discord.Embed(title="Rock paper scissors", description="It's a draw!", color=0x00ff00)
    result.add_field(name="You picked", value=arg, inline=False)
    result.add_field(name="I picked", value=choice, inline=False)
    await message.send(embed=result)  
  elif arg == "rock":
    if choice == "paper":
      result = discord.Embed(title="Rock paper scissors", description="I win!", color=0x00ff00)
      result.add_field(name="You picked", value=arg, inline=False)
      result.add_field(name="I picked", value=choice, inline=False)
      await message.send(embed=result)  
    else:
      result = discord.Embed(title="Rock paper scissors", description="You win!", color=0x00ff00)
      result.add_field(name="You picked", value=arg, inline=False)
      result.add_field(name="I picked", value=choice, inline=False)
      await message.send(embed=result)  
  elif arg == "paper":
    if choice == "scissors":
      result = discord.Embed(title="Rock paper scissors", description="I win!", color=0x00ff00)
      result.add_field(name="You picked", value=arg, inline=False)
      result.add_field(name="I picked", value=choice, inline=False)
      await message.send(embed=result)  
    else:
      result = discord.Embed(title="Rock paper scissors", description="You win!", color=0x00ff00)
      result.add_field(name="You picked", value=arg, inline=False)
      result.add_field(name="I picked", value=choice, inline=False)
      await message.send(embed=result)  
  elif arg == "scissors":
    if choice == "rock":
      result = discord.Embed(title="Rock paper scissors", description="I win!", color=0x00ff00)
      result.add_field(name="You picked", value=arg, inline=False)
      result.add_field(name="I picked", value=choice, inline=False)
      await message.send(embed=result)  
    else:
      result = discord.Embed(title="Rock paper scissors", description="You win!", color=0x00ff00)
      result.add_field(name="You picked", value=arg, inline=False)
      result.add_field(name="I picked", value=choice, inline=False)
      await message.send(embed=result)  
  else:
    await message.send("Input not valid, please try again!")

web_server()
bot.run(os.getenv('TOKEN'))