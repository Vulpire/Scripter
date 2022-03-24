import discord
import os
# import requests
# import json
from replit import db
from keep_alive import keep_alive


client = discord.Client()
guild = client.get_guild(342146742399139853) #change to scripted

# def get_quote():
#   response = requests.get("http://zenquotes.io/api/random")
#   json_data = json.loads(response.text)
#   quote = json_data[0]['q'] + " -" + json_data[0]['a']
#   return quote

def update_score(id):
  if id in db.keys():
    score = db[id]
    score += 1
    db[id] = score
  else: 
    db[id] = 1

def update_total():
  total = db[str(342146742399139853)]
  total += 1
  db[str(342146742399139853)] = total

@client.event
async def on_member_join(member):
  B = discord.utils.get(client.get_guild(342146742399139853).channels, id=892260044308107325)
  string = "Total Members: " + str(client.get_guild(342146742399139853).member_count)
  await B.edit(name=string)

@client.event
async def on_ready():
  print("We have logged in as {0.user}"
  .format(client)) 

  B = discord.utils.get(client.get_guild(342146742399139853).channels, id=892260044308107325)
  string = "Total Members: " + str(client.get_guild(342146742399139853).member_count)
  await B.edit(name=string)

@client.event
async def on_message(message):
  if message.author == client.user: #spiderman meme
    return
  
  #updates users score on any message
  update_score(str(message.author.id))  

  #updates total number of msgs
  update_total()
  if db[str(342146742399139853)] % 50 == 0:
    B = discord.utils.get(client.get_guild(342146742399139853).channels, id=892256400481353738)
    string = "Total Messages: " + str(db[str(342146742399139853)])
    await B.edit(name=string)


  #secret pass into server
  if message.channel.id == 557373833473032203: #change to scripted channel
    if message.content == os.getenv('password'):
      var = discord.utils.get(message.guild.roles, name = "Member")
      await message.author.add_roles(var)
      await message.delete()
      await message.channel.send('Your role has been changed', delete_after=1)

  #weeb / nsfw
  if message.channel.id == 892202217954750505: #change to scripted channel
    if str.lower(message.content) == "weeb":
      var = discord.utils.get(message.guild.roles, name = "Weeb")
      await message.author.add_roles(var)
      await message.delete()
      await message.channel.send('Your role has been changed', delete_after=1)
    if str.lower(message.content) == "nsfw":
      var = discord.utils.get(message.guild.roles, name = "Nsfw")
      await message.author.add_roles(var)
      await message.delete()
      await message.channel.send('Your role has been changed', delete_after=1)


  # if message.content.startswith("!quote"):
  #   q = get_quote()
  #   await message.channel.send(q)

  if message.content.startswith("!score"):
    score = round(db[str(message.author.id)] / 5)
    await message.channel.send(score)

#await message.channel.send('pong!', delete_after=5)
  
keep_alive()
client.run(os.getenv('token'))