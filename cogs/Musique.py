from discord.ext import commands, tasks
from discord import Member
import discord

bot = commands.Bot(command_prefix = "!")

class Musique(commands.Cog):

   @commands.command()
   async def pingm(self, ctx):
      await ctx.send("Test")

def setup(bot):
   bot.add_cog(Musique(bot))