import discord, pyowm, json, os
from discord.ext import commands

class Other(commands.Cog):
	def __init__(self,bot):
		self.bot = bot

	@commands.command(aliases= ["погода"])
	async def weather(self, ctx, city = None):
		if city == None:
			await ctx.send('Укажите город!', delete_after=10)
		else:
			owm = pyowm.OWM('c88a1aa1d7cb2565b7905b16ea12114e', language='ru')
			observation = owm.weather_at_place(city)
			w = observation.get_weather()
			temperature = w.get_temperature('celsius')['temp']
			humidity = w.get_humidity()
			Wind = w.get_wind()['speed']
			emb = discord.Embed(title = f'Погода в {city}',description = f'**Температура:** `{temperature}°`\n**Влажность:** `{humidity}%`\n**Скорость ветра:** `{Wind} м/c`',colour = 0x00FF00)
			emb.set_author(name = f'{ctx.message.author}',icon_url = ctx.message.author.avatar_url)
			await ctx.send(embed = emb, delete_after = 30)

	@commands.command(aliases= ["помощь"])
	async def help(self, ctx, command = None):
		if not command:
			helpown = discord.Embed(title = "Список команд", description='Используйте `!` перед началом команды\n**Общее**\n`help`,`weather`\n**Развлечение**\n`picture`,`F`,`coin`,`roll`\n**Модерация**\n`report`,`mute`,`unmute`,`ban`,`create_role`,`role`,`move`\n**Другое**\n`say`,`esay`,`clear`', colour=0x39d0d6)
			helpown.set_footer(text ='Вы можете ввести help для команды и получить доп. информацию')
			await ctx.send(embed = helpown, delete_after=30)
		else:
			a = os.path.join(os.path.dirname(__file__), "../Json/help.json")
			info = json.load(open(a, encoding="UTF-8"))
			commands = info.get(command)
			if commands is None:
				await ctx.send('Укажите правильно команду', delete_after=10)
			else:
				await ctx.send(embed = discord.Embed(title = commands["title"], description = commands["description"], colour = 0x39d0d6), delete_after = 60)

def setup(bot):
    bot.add_cog(Other(bot))
