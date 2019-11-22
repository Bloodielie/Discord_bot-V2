from discord.ext import commands
import discord, config, asyncio, datetime, os
from cogs.Utils import utils

class Jojobot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.load()

    def load(self):
        self.remove_command('help')

        modules = (
          'cogs.entertainment',
          'cogs.moderation',
          'cogs.events',
          'cogs.other',
          'cogs.monitoring'
        )
        print(f'|Cogs/INFO|     |Cogs/NAME|     |Cogs/ERROR|')
        for i in modules:
            a = i.replace('cogs.', '').capitalize()
            try:
                length = len(i)
                probel = utils.check_space(length)

                self.load_extension(i)
                print(f'LOADED!         {a}{probel}Not Error\n')
            except Exception as error:
                print(f'NOT LOADED!     {a}{probel}{error}\n')

    async def on_disconnect(self):
        print('[Socket/WARN]          <Socket Disconnected>\n')

    async def on_connect(self):
        print('[Socket/CONNECT]       <Socket Connected>\n')

    async def on_ready(self):
        print('[Discord/INFO]         <Jojobot ready!>\n')

        type = discord.ActivityType
        activ = discord.Activity(name= f"!help", type= type.watching)
        await self.change_presence(status=discord.Status.online, activity=activ)

    async def on_command(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass

    async def on_command_error(self, ctx, error):
        try:
            channel = self.get_channel(config.error_chanel)
            emb = discord.Embed(title = "Ошибка в on_command_error!", description = f"Произошла ошибка:\n```{error}```", colour = 0xff0000)
            await channel.send(embed = emb)
        except:
            pass


if __name__ == "__main__":
    tokenrs = os.environ.get('BOT_TOKEN')
    bot = Jojobot(command_prefix=config.prefix,case_insensitive=True).run(str(tokenrs))
