import discord
import os
import requests
import json
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


web_server()
bot.run(os.getenv('TOKEN'))