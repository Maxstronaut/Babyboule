from queue import Empty
from discord.ext import commands, tasks
from discord import Member
import discord
from bs4 import BeautifulSoup
import urllib.parse
from urllib.request import urlopen,Request
import random

bot = commands.Bot(command_prefix = "!")

class Fun(commands.Cog):

   @commands.command()
   async def send(self, ctx, user : discord.User, *message):
      print(ctx.author, user, message)
      message  = " ".join(message)
      await user.send("Messagerie Anonyme: "+str(message))
      messages = await ctx.channel.history(limit = 1).flatten()
      for message in messages:
         await message.delete()
   
   @commands.command()
   @commands.has_permissions(kick_members = True)
   async def say(self, ctx, *say):
      messages = await ctx.channel.history(limit = 1).flatten()
      for message in messages:
         await message.delete()
      say  = " ".join(say)
      await ctx.send(say)

   @commands.command()
   async def jetesuce(self, ctx):
      await ctx.send("https://media.discordapp.net/attachments/931616283215142912/975867078596759552/Polish_20220516_230643678.jpg")

def setup(bot):
   bot.add_cog(Fun(bot)) 