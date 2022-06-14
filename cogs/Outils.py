from discord.ext import commands, tasks
from discord import Member
import discord
import random
import string
from time import sleep
import urllib.request

class Outils(commands.Cog):

   def __init__(self, bot):
      self.bot = bot

   @commands.command()
   async def ping(self, ctx):
      await ctx.send("Pong")

   @commands.command(aliases=['pdp'], description=f"- Récupere la photo de profil d'un utilisateur:")
   async def pfp(self, ctx, user : discord.User):
      embed = discord.Embed(
         title= f"**Photo de profil de {str(user)}**",
         )
      embed.set_image(url = user.avatar_url)
      await ctx.send(embed = embed)

   @commands.command(description=f"- Récupere des informations sur un utilisateur:")
   async def info(self, ctx, user : discord.User):
      mention = []
      for role in user.roles:
         mention.append(role.mention)
         b = ", ".join(mention)
      embed = discord.Embed(
         title= f"**Informations sur {str(user)}**",
         )
      embed.add_field(name = "Role: ", value = b)
      embed.add_field(name = "Permissions sur le serveur: ", value = user.guild_permissions)
      embed.add_field(name = "Création du compte: ", value = user.created_at)
      embed.add_field(name = "Nick sur le serveur: ", value = user.nick)
      embed.add_field(name = "ID: ", value = user.id)
      embed.add_field(name = "A rejoin le serveur: ", value = user.joined_at)
      embed.add_field(name = "Avatar: ", value = user.default_avatar_url)
      await ctx.send(embed = embed)

   @commands.command()
   async def test(self, ctx, user : discord.User):
      embed = discord.Embed(
         title= f"**Photo de profil de {str(user.member.profile)}**",
         )
      await ctx.send(embed = embed)


def setup(bot):
   bot.add_cog(Outils(bot))
   
