import discord, psutil, datetime
from discord.ext import commands

class Monitoring(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases = ["мониторинг", "мтр"])
    async def monitoring(self, ctx):
        await ctx.send("Собираю данные!!!", delete_after = 2)
        cpu_percent = int(100.0 - psutil.cpu_times_percent(interval=2)[2])
        cpu_count = psutil.cpu_count(logical=True)
        memory_percent = psutil.virtual_memory()[2]
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d.%B.%Y %H:%M:%S")
        ping = int(self.bot.latency * 1000)
        monitor = discord.Embed(title='Мониторинг.', description=f'**Процессор:**\nЗагруженность:`{cpu_percent}%`\nКоличество ядер:`{cpu_count}`\n**Оперативная память:**\nЗагруженность:`{memory_percent}%`\n**Система:**\nUptime:`{boot_time}`', colour= 0xFF0000)
        monitor.set_author(name = f'{ctx.message.author}', icon_url = ctx.message.author.avatar_url)
        monitor.set_footer(text = f"Пинг:{ping}")
        await ctx.send(embed = monitor, delete_after = 30)

def setup(bot):
    bot.add_cog(Monitoring(bot))