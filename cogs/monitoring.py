import discord, psutil, datetime, platform, os
from discord.ext import commands

class Monitoring(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases = ["мониторинг", "мтр"])
    async def monitoring(self, ctx):
        await ctx.send("Собираю данные!!!", delete_after = 2)
        cpu_percent = int(100.0 - psutil.cpu_times_percent(interval=2)[2])
        cpu_count = psutil.cpu_count(logical=True)
        cpu_name = platform.processor()
        memory_percent = psutil.virtual_memory()[2]
        memory_full = f"{(str(psutil.virtual_memory()[0])[:2])[0]}.{(str(psutil.virtual_memory()[0])[:2])[1]} Гб"
        memory_available = f"{(str(psutil.virtual_memory()[1])[:2])[0]}.{(str(psutil.virtual_memory()[1])[:2])[1]} Гб"
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d.%B.%Y %H:%M:%S")
        ping = int(self.bot.latency * 1000)
        memory_prog = str(int(psutil.Process(os.getpid()).memory_info().rss) / 1024)[:2]
        monitor = discord.Embed(title='Мониторинг.', description=f'**Процессор:**\nЗагруженность:`{cpu_percent}%`\nКоличество ядер:`{cpu_count}`\nНазвание:`{cpu_name}`\n**Оперативная память:**\nЗагруженность:`{memory_percent}%`\nОбщий объем:`{memory_full}`\nСвободный объем:`{memory_available}`\nСкрипт потребялет:`{memory_prog}Мб`\n**Система:**\nUptime:`{boot_time}`', colour= 0xFF0000)
        monitor.set_author(name = f'{ctx.message.author}', icon_url = ctx.message.author.avatar_url)
        monitor.set_footer(text = f"Пинг:{ping}")
        await ctx.send(embed = monitor, delete_after = 30)

def setup(bot):
    bot.add_cog(Monitoring(bot))