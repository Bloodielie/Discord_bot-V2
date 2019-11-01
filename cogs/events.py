from discord.ext import commands
import discord, config, random, asyncio, datetime

class Event(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel = self.bot.get_channel(config.error_chanel)
		try:
		    role = discord.utils.get(member.guild.roles, name=config.role_on_member_join)
		    author = member.mention
		    await member.add_roles(role)
		    await member.send(content=f"Привет {author}, добро пожаловать на сервер Фронсуа")
		except Exception as error:
			await channel.send(embed = discord.Embed(title = "Произошла ошибка(EVENT)!",description=f'```{error}```', colour= 0xFF0000))

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		channel = self.bot.get_channel(config.error_chanel)
		try:
		    author = member.mention
		    await  member.send(content=f"Жаль, что ты уходишь от нас {author}")
		except Exception as error:
			await channel.send(embed = discord.Embed(title = "Произошла ошибка(EVENT)!",description=f'```{error}```', colour= 0xFF0000))

	@commands.Cog.listener()
	async def on_voice_state_update(self, member, voice_before, voice_after):
		members = 0
		error_channel = self.bot.get_channel(config.error_chanel)
		channel = self.bot.get_channel(config.voice_log_channel)
		channel_1 = self.bot.get_channel(config.voice_check)
		guild = member.guild
		dota_create = self.bot.get_channel(config.id_dota)
		game_create = self.bot.get_channel(config.id_game)
		try:
			if voice_after.channel == dota_create:
				random1 = random.randint(5,10)
				namechannel = 'dota[' + member.display_name + ']'
				channel_dota = await guild.create_voice_channel(name=namechannel, category=dota_create.category, user_limit=random1)
				await asyncio.sleep(0.5)
				await member.edit(voice_channel=channel_dota)
				status = True

				while status:
					await asyncio.sleep(10)
					if len(channel_dota.members) == 0:
						await channel_dota.delete()
						status = False
		except Exception as error:
			await error_channel.send(embed = discord.Embed(title = "Произошла ошибка(EVENT)!",description=f'```{error}```', colour= 0xFF0000))

		try:
			if voice_after.channel == game_create:
				random1 = random.randint(5,10)
				namechannel = 'game[' + member.display_name + ']'
				channel_game = await guild.create_voice_channel(name=namechannel, category=game_create.category, user_limit=random1)
				await asyncio.sleep(0.5)
				await member.edit(voice_channel=channel_game)
				status = True

				while status:
					await asyncio.sleep(10)
					if len(channel_game.members) == 0:
						await channel_game.delete()
						status = False
		except Exception as error:
			await error_channel.send(embed = discord.Embed(title = "Произошла ошибка(EVENT)!",description=f'```{error}```', colour= 0xFF0000))

		if voice_before.channel is None:
			emb=discord.Embed(description= f'{member.mention} вошёл в `{voice_after.channel.name}`',
				colour= 0x32CD32)
			emb.set_footer(text=str(datetime.datetime.utcnow()+datetime.timedelta(hours=3))[:19])
			await channel.send(embed = emb)

		elif voice_after.channel is None:
			emb=discord.Embed(description= f'{member.mention} вышел из `{voice_before.channel.name}`',
				colour= 0xB22222)
			emb.set_footer(text=str(datetime.datetime.utcnow()+datetime.timedelta(hours=3))[:19])
			await channel.send(embed = emb)

		elif voice_before.channel in member.guild.voice_channels:
			if voice_before.channel == voice_after.channel:
				pass
			elif voice_after.channel in member.guild.voice_channels:
				emb=discord.Embed(description= f'{member.mention} переместился `{voice_before.channel.name}` => `{voice_after.channel.name}`',
					colour= 0x1E90FF)
				emb.set_footer(text=str(datetime.datetime.utcnow()+datetime.timedelta(hours=3))[:19])
				await channel.send(embed= emb)

		for member1 in member.guild.voice_channels:
			member_1 = len(member1.members)
			members += member_1
			await channel_1.edit(name=f'● В войсах » {members}')

	@commands.Cog.listener()
	async def on_raw_reaction_add(self, rawreactionactionevent):
		if rawreactionactionevent.message_id == 630815980590989340:
			guild = self.bot.get_guild(rawreactionactionevent.guild_id)
			member = guild.get_member(rawreactionactionevent.user_id)
			role_ban = discord.utils.get(member.guild.roles, name="Опасный тип")
			role_OSU = discord.utils.get(member.guild.roles, name="OSUждаю")
			role_tiwinner = discord.utils.get(member.guild.roles, name="TIwinner")
			role_1 = discord.utils.get(member.guild.roles, name="carry")
			role_2 = discord.utils.get(member.guild.roles, name="mider")
			role_3 = discord.utils.get(member.guild.roles, name="offlaner")
			role_4 = discord.utils.get(member.guild.roles, name="sup 4")
			role_5 = discord.utils.get(member.guild.roles, name="sup 5")
			if rawreactionactionevent.emoji.name == "BanHammer":
				await member.add_roles(role_ban)
			elif rawreactionactionevent.emoji.name == "OSU":
				await member.add_roles(role_OSU)
			elif rawreactionactionevent.emoji.name == "Tiwinner":
				await member.add_roles(role_tiwinner)
			elif rawreactionactionevent.emoji.name == "carry":
				await member.add_roles(role_1)
			elif rawreactionactionevent.emoji.name == "mider":
				await member.add_roles(role_2)
			elif rawreactionactionevent.emoji.name == "offlaner":
				await member.add_roles(role_3)
			elif rawreactionactionevent.emoji.name == "sup4":
				await member.add_roles(role_4)
			elif rawreactionactionevent.emoji.name == "sup5":
				await member.add_roles(role_5)

	@commands.Cog.listener()
	async def on_raw_reaction_remove(self, rawreactionactionevent):
		if rawreactionactionevent.message_id == 630815980590989340:
			guild = self.bot.get_guild(rawreactionactionevent.guild_id)
			member = guild.get_member(rawreactionactionevent.user_id)
			role_ban = discord.utils.get(member.guild.roles, name="Опасный тип")
			role_OSU = discord.utils.get(member.guild.roles, name="OSUждаю")
			role_tiwinner = discord.utils.get(member.guild.roles, name="TIwinner")
			role_1 = discord.utils.get(member.guild.roles, name="carry")
			role_2 = discord.utils.get(member.guild.roles, name="mider")
			role_3 = discord.utils.get(member.guild.roles, name="offlaner")
			role_4 = discord.utils.get(member.guild.roles, name="sup 4")
			role_5 = discord.utils.get(member.guild.roles, name="sup 5")
			if rawreactionactionevent.emoji.name == "BanHammer":
				await member.remove_roles(role_ban)
			elif rawreactionactionevent.emoji.name == "OSU":
				await member.remove_roles(role_OSU)
			elif rawreactionactionevent.emoji.name == "Tiwinner":
				await member.remove_roles(role_tiwinner)
			elif rawreactionactionevent.emoji.name == "carry":
				await member.remove_roles(role_1)
			elif rawreactionactionevent.emoji.name == "mider":
				await member.remove_roles(role_2)
			elif rawreactionactionevent.emoji.name == "offlaner":
				await member.remove_roles(role_3)
			elif rawreactionactionevent.emoji.name == "sup4":
				await member.remove_roles(role_4)
			elif rawreactionactionevent.emoji.name == "sup5":
				await member.remove_roles(role_5)

def setup(bot):
    bot.add_cog(Event(bot))