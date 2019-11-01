import discord, config, asyncio, datetime, vk_api
from discord.ext import commands

class On_ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
          
    @commands.Cog.listener()
    async def on_ready(self):
        print('[Discord/INFO]         <Jojobot ready!>\n')

        type = discord.ActivityType
        activ = discord.Activity(name= f"!help", type= type.watching)
        await self.bot.change_presence(status=discord.Status.online, activity=activ)

def setup(bot):
    bot.add_cog(On_ready(bot))
