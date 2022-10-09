#import discord
import discord
from discord.ext import commands
from discord import guild

from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

import os
import random
import datetime
import keep_alive


bot = commands.Bot(command_prefix= "!g ")
slash = SlashCommand(bot, sync_commands = True)

bot.remove_command('help')

keywords = ['/message',]
pandey_keywords = ['frustrat', 'Frustrat', 'FRUSTRAT']
n_words = ['n-word']


#message should not be scanned if sent by a bot
@bot.event
async def on_message(message):
  
  for word in keywords:
    if word in message.content:
      await message.delete()
      break  

## fun little easter eggs below
  if message.author.id != 901310349687541820:
    #kill bill pandey
    for word in pandey_keywords:
      if word in message.content:     
        await message.channel.send('they call me Kill Bill Pandey!!')
        await message.channel.send('https://www.youtube.com/watch?v=e-RkZSlcRFg')
      
    if ('nvincible' in message.content):
      await message.reply(file = discord.File(r'invincible_titlecard_2.jpg'))
    
    
    ## Moderation N-word Detector
    for word in n_words:
      if word in message.content:  
        em = discord.Embed(title = "N-word Detected!", url = "https://discord.gg/VkF3z8WmEN", description = "@everyone a n-word was found!", color = 0x000000)

        em.add_field(name = "Message Author", value = message.author, inline = False)
        em.add_field(name = "Message Content", value = message.content, inline = False)
        em.add_field(name = "Time", value = datetime.date.today(), inline = False)
        em.set_thumbnail(url = 'https://tinyurl.com/shaqnigger')
        em.set_footer(icon_url = message.author.avatar_url, text = message)
        await message.reply(embed = em)

  await bot.process_commands(message)


#add slash command
@slash.slash(
  name = 'add',
  description = 'adds roasts or pickups to my datatbase',
  guild_ids = [],
  options = [
    create_option(
      name = 'option',
      description = 'chose your word',
      required = True,
      option_type = 3,
      choices = [
        create_choice(name='roast', value = 'roast'),
        create_choice(name='pick up line', value = 'pickup')
      ]
    ),
    create_option(
      name = 'text', 
      description = 'input the text', 
      required = True, option_type = 3
      )
  ]
)
async def add(ctx:SlashContext, option:str, text:str):
     if option == 'roast':
      f = open("roasts.txt", "a")
     elif option == 'pickup':
       f = open("pickup_lines.txt","a")
     f.write("\n")
     f.write(text)
     f.close()

     await ctx.send(ctx.author.mention + ' added a ' + option + ' to my data base')

#roast slash command
file = open("roasts.txt", "r")
roast_len = 0
for line in file:
    if line != "\n":
        roast_len += 1
file.close()

@slash.slash(
  name = 'roast',
  description = 'sends a roasts a user in the server',
  guild_ids = []
)
async def roast(ctx:SlashContext):
  with open("roasts.txt") as open_file:
      lines = open_file.readlines()
      await ctx.send(lines[random.randint(0,roast_len)])

# Pickup slash command type '/pickup to get a pick up line'
file = open("pickup_lines.txt", "r")
pickup_len = 0
for line in file:
    if line != "\n":
        pickup_len += 1
file.close()

@slash.slash(
  name = 'pickup',
  description = 'gives a pickup line',
  guild_ids = []
)
async def pickup(ctx:SlashContext):
  with open("pickup_lines.txt") as open_file:
      lines = open_file.readlines()
      await ctx.send(lines[random.randint(0,pickup_len)])

ball_choices = [
  "It is certain."
  "It is decidedly so.",
  "Without a doubt.",
  "Yes definitely.",
  "You may rely on it",
  "As I see it, yes.",
  "Most likely.",
  "Outlook is good.",
  "Yes.",
  "Signs point to yes",
  "Reply hazy, try again.",
  "Ask again later.",
  "Better not tell you now.",
  "Cannot predict now.",
  "Concentrate and ask again.",
  "Don't count on it.",
  "My reply is no.",
  "My sources say no.",
  "Outlook not so good.",
  "Very doubtful."
]

@slash.slash(
  name = '8ball',
  description = 'answers your question',
  guild_ids = []
)
async def eightball(ctx:SlashContext, question:str):
  await ctx.send(ball_choices[random.randint(0,len(ball_choices) - 1)])


#spam function to spam I guess, its against the rules though lol
@slash.slash(
  name = 'spam',
  description = 'spams a message',
  guild_ids = []
)
async def spam(ctx:SlashContext, amount:int, text:str):
  for i in range (amount):
    await ctx.send(text)

@slash.slash(
  name = 'say',
  description = 'says a message',
  guild_ids = []
)
async def say(ctx:SlashContext, text:str):
  await ctx.send(text)

#stolen from dank memer
@slash.slash(
  name = 'rate',
  description = 'rates how much you are of something',
  guild_ids = [],
  options = [
    create_option(
      name = 'option',
      description = 'chose the type',
      required = True,
      option_type = 3,
      choices = [
        create_choice(name = 'woke', value = 'a wokist'),
        create_choice(name = 'simp', value = 'a simp'),
        create_choice(name = 'horny', value = 'horny'),
        create_choice(name = 'spicy', value = 'spicy'),
        create_choice(name = 'tryhard', value = 'tryharding'),
        create_choice(name='loser', value = 'a loser')
      ]
    )
  ]
)

async def rate(ctx:SlashContext, option:str):
  await ctx.send(ctx.author.mention + ' is ' + str(random.randint(0,100)) + '% ' + option)

#coin flip slash command
@slash.slash(
  name = 'coinflip',
  description = 'flips a coin for you',
  guild_ids = []
)
async def coinflip(ctx:SlashContext):
  if random.randint(0,1) == 0:
    await ctx.send('🪙 Heads!')
  else:
    await ctx.send('🪙 Tails!')
    
# execute bot
keep_alive.keep_alive()
ghostpepper_TOKEN = os.environ['ghostpepper_TOKEN']
bot.run(ghostpepper_TOKEN)
