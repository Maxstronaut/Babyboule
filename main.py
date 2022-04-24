import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = "!")

intents = discord.Intents.default()
intents.members = True

initial_extensions = []

for filename in os.listdir('./cogs'):
   if filename.endswith('.py'):
      initial_extensions.append("cogs." + filename[:-3])

print(initial_extensions)

if __name__ == '__main__':
   for extension in initial_extensions:
      bot.load_extension(extension)

@bot.event
async def on_ready():
   await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="Garfiled Kart Deluxe"))
   print(bot.user.name + " est en ligne")

# @bot.command()
# async def ping(ctx):
#    await ctx.send("Pong")

bot.run("aaa")  
