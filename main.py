
import discord
from discord.ext import commands
import random
import os

bot = commands.Bot(command_prefix= "/")

#must add discord bot token
ghostpepper_TOKEN = 'token'

# Roast command type '/roast to get roasted'

roast_list = ['you suck', 'shut up dumbass', 'you like someone photoshopped a monkey face onto a horse', 'I care more about dead snails than I do about you', 'you are so ugly you turned medusa into stone.']

@bot.command()
async def roast(ctx):
  await ctx.send(random.choice(roast_list))



# execute bot
bot.run(ghostpepper_TOKEN)


