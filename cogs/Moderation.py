from discord.ext import commands, tasks
from discord import Member
import discord
import datetime

bot = commands.Bot(command_prefix = "!")
log = bot.get_channel(int(966799968889340014))

class Moderation(commands.Cog):

   def __init__(self, bot):
      self.bot = bot   

   @commands.command()
   @commands.has_permissions(manage_messages = True)
   async def clear(self, ctx, number : int):
      messages = await ctx.channel.history(limit = number+1).flatten()
      for message in messages:
         await message.delete()
      embed = discord.Embed(
         title= "**🗑️ Messages supprimé**",
         description = f"```{str(ctx.author)} a supprimé {str(number)} message dans {message.channel.name}```",
         color=0xf7ce36,
         )
      await ctx.send("``"+str(number)+""+" messages ont été supprimés``")

   @commands.command()
   @commands.has_permissions(kick_members = True)
   async def kick(self, ctx, user : discord.User, *reason):
      log = bot.get_channel(int(966799968889340014))
      reason  = " ".join(reason)
      embed = discord.Embed(
         title= "**👢 Kick**",
         description = f"```{str(ctx.author)} a kick {str(user)} du serveur```",
         color=0xedb321,
         )
      embed.add_field(name = "Raison:", value = "```"+reason+"```")
      embed.set_footer(text = str(user.id), icon_url = user.avatar_url)
      embed.set_thumbnail(url = ctx.author.avatar_url)
      await ctx.guild.kick(user, reason = reason)
      await ctx.send(embed = embed)
      await log.send(embed = embed)
      await print("Name:",str(user.name), "ID:",str(user.id), "Reason:", str(reason), "Type: Kick")

   @commands.command()
   @commands.has_permissions(ban_members = True)
   async def ban(self, ctx, user : discord.User, *reason):
      if reason == None:
         reason = "Non spécifié"
      log = bot.get_channel(int(966799968889340014))
      reason  = " ".join(reason)
      await ctx.guild.ban(user, reason = reason)
      embed = discord.Embed(
         title= "**🔨 Ban**",
         description = f"```{str(ctx.author)} a ban {str(user)} du serveur```",
         color=0xab0c0c,
         )
      embed.add_field(name = "Raison:", value = "```"+reason+"```")
      embed.set_footer(text = str(user.id), icon_url = user.avatar_url)
      embed.set_thumbnail(url = ctx.author.avatar_url)
      await ctx.send(embed = embed)
      await log.send(embed = embed)
      print("Name:",str(user.name), "- ID:",str(user.id), "- Reason:", str(reason), "- Type: Ban")

   @commands.command()
   @commands.has_permissions(ban_members = True)
   async def unban(self, ctx, user : discord.User):
      log = bot.get_channel(int(966799968889340014))
      await ctx.guild.unban(user)
      embed = discord.Embed(
         title= "**🔄 Unban**",
         description = f"```{str(ctx.author)} a unban {str(user)} du serveur```",
         color=0xab0c0c,
         )
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_thumbnail(url = ctx.author.avatar_url)
      await ctx.send(embed = embed)
      await log.send(embed = embed)
      print("Name:",str(user.name), "- ID:",str(user.id), "- Type: Unban")

def setup(bot):
   bot.add_cog(Moderation(bot))