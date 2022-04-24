import discord
from discord.ext import commands

class Misc(commands.Cog):

   def __init__(self, bot):
      self.bot = bot

   @commands.command()
   async def ping(self, ctx):
      await ctx.send("Pong")

   @commands.command()
   async def say(self, ctx, *text):
      await ctx.send(text)

def setup(bot):
   bot.add_cog(Misc(bot))

# Pour event:
# commands.Cog.listener()