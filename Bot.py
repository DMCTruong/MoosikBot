##########################################################################################
# Program Name :     Discord Bot
# Author       :     DMCTruong
# Last Updated :     August 31, 2017
# License      :     MIT
# Description  :     A general purpose bot written for Discord               
##########################################################################################


# To do List:
#	- Add a calculator
#	- Add a translator: https://pypi.python.org/pypi/googletrans
#	- Add a better tutorial on how to install and get the keys for the configurations
#	- Add better documentation of the code
#	- Add better documentation of installations
#   - Redo the restart command
#	- Return the user's avatar?
#	- Update pyrebase commands

import discord
from discord.ext import commands
import logging
import asyncio
import configurations

from modules import database
from modules import help
from modules import miscellaneous
from modules import music
from modules import owner_only
from modules import timer

# ------------- Logging --------------

if configurations.DISCORD_LOG in ["y", "Y", "yes", "Yes", "YES"]:
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

# if configurations.COMMAND_LOG in ["y", "Y", "yes", "Yes", "YES"]:
# if configurations.ERROR_LOG in ["y", "Y", "yes", "Yes", "YES"]:



# -------- Initialize the Bot --------

bot = commands.Bot(configurations.PREFIX) 

bot.add_cog(database.Database(bot))
bot.add_cog(help.Help(bot))
bot.add_cog(miscellaneous.Miscellaneous(bot))
bot.add_cog(music.Music(bot))
bot.add_cog(owner_only.Owner_Only(bot))
bot.add_cog(timer.Time(bot))

print("\nPlease wait while the Bot logs in ...")

@bot.event
async def on_ready():
    print("\nLogged in as:\n")
    print("Username : " + bot.user.name)
    print("ID Number: " + bot.user.id)
    print('\nType ">>help" in the Discord chat for the list of commands.')
    print("=============================================")
	
    await bot.change_presence(game=discord.Game(name='>>help for commands!'))
	
bot.run(configurations.BOT_TOKEN)