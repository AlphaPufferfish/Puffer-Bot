import discord
import os
import requests
import json
import random
from web_sever import web_server
from discord.ext import commands
from replit import db

bot = commands.Bot(command_prefix="p!")

# helper functions for the user joke db

def add_user_joke(joke):
  if "u_jokes" in db.keys():
    u_jokes = db["u_jokes"]
    u_jokes.append(joke)
    db["u_jokes"] = u_jokes
  else:
    db["u_jokes"] = [joke]

def add_vote(id):
  if "likes" in db.keys():
    likes = db["likes"]
    likes.append([id])
    db["likes"] = likes
  else:
    db["likes"] = [id]

def dislike(id):
  if "dislikes" in db.keys():
    dislikes = db["dislikes"]
    dislikes.append([id])
    db["dislikes"] = dislikes
  else:
    db["dislikes"] = [id]

def delete_joke(index):
  u_jokes = db["u_jokes"]
  if len(u_jokes) >= index:
    del u_jokes[index-1]
    db["u_jokes"] = u_jokes
  else:
    t = "Index does not exist!"
    emb = discord.Embed(title = t, color=discord.Colour.from_rgb(242, 235, 34))
    return emb;

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
@bot.command(aliases = ["Joke", "JOKE"])
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

# user submitted jokes
@bot.command()
async def ujoke(message,* , arg = None):
  u_jokes = db["u_jokes"]
  if arg:
    if arg == "number":
      t = "Currently Puffer Bot knows " +str(len(u_jokes)) + " user submitted joke(s)!"
      emb = discord.Embed(title = t, color=discord.Colour.from_rgb(242, 235, 34))
      await message.send(embed = emb)
    elif not arg.isdigit() or int(arg) > len(u_jokes) or int(arg)<= 0:
      t = "Joke number not valid, please try again!"
      emb = discord.Embed(title = t, color=discord.Colour.from_rgb(242, 235, 34))
      await message.send(embed = emb)
    else:
      t = "Joke No." + arg
      emb = discord.Embed(title = t, color=discord.Colour.from_rgb(242, 235, 34))
      emb.add_field(name = '\u200b' , value = u_jokes[int(arg)-1], inline=False)
      await message.send(embed = emb)
  else:
      nr = random.randint(1,len(u_jokes))
      t = "Joke No." + str(nr)
      emb = discord.Embed(title = t, color=discord.Colour.from_rgb(242, 235, 34))
      emb.add_field(name = '\u200b' , value = u_jokes[nr-1], inline=False)
      await message.send(embed = emb)

# submit a joke
@bot.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def jsubmit(message,* , arg = None):
  if arg:
    if len(arg)<=1024:
     add_user_joke(arg)
     add_vote(message.author.id)
     t = "Joke has been added successfully!"
    else:
      t = "Joke too long!Please enter a joke no longer than 1024 characters!"
  else:
    t = "No joke has been entered, please try again!"
  emb = discord.Embed(title = t, color=discord.Colour.from_rgb(242, 235, 34))
  await message.send(embed = emb)

# submit cooldown handler
@jsubmit.error
async def jsubmit_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Submit not available yet!",description=f"Try again in {error.retry_after//60:.0f} minutes.", color=discord.Colour.from_rgb(242, 235, 34))
        await ctx.send(embed=em)

# vote system
@bot.command()
async def like(message, nr = None):
  likes = db["likes"]
  uid = message.author.id
  if nr and nr.isdigit() and int(nr) <= len(likes) and int(nr)>0:
    if uid in likes[int(nr)-1]:
      t = "You already liked this joke!"
      emb = discord.Embed(title = t, color=discord.Colour.from_rgb(242, 235, 34))
      await message.send(embed = emb)
    else:
      likes[int(nr)-1].append(uid)
      t = "You liked joke No." + nr + "!"
      emb = discord.Embed(title = t, color=discord.Colour.from_rgb(242, 235, 34))
      await message.send(embed = emb)
  else:
    t = "Joke number not valid, please try again!"
    emb = discord.Embed(title = t, color=discord.Colour.from_rgb(242, 235, 34))
    await message.send(embed = emb)
  db["likes"] = likes

@bot.command()
async def pr(message):
  likes = db["likes"]
  dislikes = db["dislikes"]
  print(likes)
  print(dislikes)
  print("-----")
  print(likes[0])
  print("----")
  print(likes[1])
  print("-----")
  print(likes[2])

web_server()
bot.run(os.getenv('TOKEN'))