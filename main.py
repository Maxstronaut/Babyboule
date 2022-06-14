from datetime import date
from msilib.schema import Error
import discord
from discord.ext import commands, tasks
import os
import datetime

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
   log = bot.get_channel(int(966799968889340014)) 
   await bot.change_presence(status=discord.Status.invisible, activity=discord.Activity(type=discord.ActivityType.watching, name="les nouvelles coques Babyboule"))
   await log.send("Babyboule est en ligne")
   print(bot.user.name + " est en ligne")

@bot.event
async def on_message_delete(message):
   if message.author == bot.user:
      return
   log = bot.get_channel(int(966799968889340014))
   if message.author == bot.user:
      return
   embed = discord.Embed(
      title= "**🗑️  Message supprimé**",
      description = f"Un message de {str(message.author)} a été supprimé dans #{message.channel.name}:\n\n```{message.content}```",
      color=0xda291c,
      set_thumbnail = message.author.avatar_url,
      )
   embed.timestamp = datetime.datetime.utcnow()
   await log.send(embed = embed)

@bot.event
async def on_message_edit(after, before):
   log = bot.get_channel(int(966799968889340014))
   if before.author == bot.user:
      return
   embed = discord.Embed(
      title= "**✍  Message modifié**",
      description = f"{str(before.author)} a modifié son message dans #{before.channel.name}:\n\n```Avant: {after.content}\n\nAprès: {before.content}\n\n""```",
      color=0xda291c,
      set_thumbnail = before.author.avatar_url,
      )
   embed.timestamp = datetime.datetime.utcnow()
   await log.send(embed = embed)

@bot.event
async def on_command_error(ctx, error):
   print(error)
   if isinstance(error, commands.MissingRequiredArgument):
      embed = discord.Embed(
         title= "**❌ Erreur**",
         description = f"{str(ctx.author.display_name)}, il me manque des arguments nécessaire pour effectuer cette commande!\n\n> Effectue !help [Nom de la commande] pour plus d'informations sur celle ci",
         color=0xda291c,
         )
      embed.set_footer(text = error)
      await ctx.send(embed = embed)
   elif isinstance(error, commands.MissingPermissions):
      embed = discord.Embed(
         title= "**❌ Erreur**",
         description = f"{str(ctx.author.display_name)}, il te manque des permissions requises pour pouvoir effectuer cette commande!",
         color=0xda291c,
         )
      embed.set_footer(text = error)
      await ctx.send(embed = embed)
   else:
      print(error)

bot.run("OTY2NzM5NDE0MjU0NDg1NTk0.YmGIPQ.AcVxD19UjM-LvHaWHIf5PUVbjjA")