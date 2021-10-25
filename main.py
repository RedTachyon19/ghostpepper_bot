
import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix= "/")

# must add discord bot token
# make the bot token hidden, it is a password for the bot.
ghostpepper_TOKEN = 'token' 

# Roast command type '/roast to get roasted'
# Don't use an array to store the roasts.

roast_list = ['you suck', 'shut up dumbass', 'you like someone photoshopped a monkey face onto a horse', 'I care more about dead snails than I do about you', 'you are so ugly you turned medusa into stone.']

@bot.command()
async def roast(ctx):
  await ctx.send(random.choice(roast_list))

# execute bot
bot.run(ghostpepper_TOKEN)



