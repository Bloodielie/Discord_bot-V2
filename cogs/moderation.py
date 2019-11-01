import discord, datetime, random, config, asyncio
from discord.ext import commands

class moderation(commands.Cog):
	def __init__(self,bot):
		self.bot = bot

	@commands.command(aliases = ["очистка"])
	async def clear(self, ctx, amount = None):
		member_id = ctx.message.author.id
		if member_id in config.owner_list:
			if amount is None:
				await ctx.channel.purge(limit=10)
			else:
				amount = int(amount)
				amount += 1
				await ctx.channel.purge(limit=amount)
		else:
			await ctx.send("У вас нету прав для использования этой комманды!", delete_after = 30)

	@commands.command(aliases = ["бан"])
	async def ban(self, ctx, member: discord.Member = None, tm = "infinite", *, reason = "Не указана"):
		member_id = ctx.message.author.id
		channel = self.bot.get_channel(config.server_channel)
		if member_id in config.owner_list:
			if not member:
				await ctx.send("Укажите пользователя!", delete_after = 30)
			else:
				if tm == "infinite":
					banid = discord.Embed(description=f'**{member.mention} забанен!**\n**Время:**\nДо снятия админом\n**Причина:**\n{reason}', colour= 0xFF0000)
					banid.set_author(name = f'{ctx.message.author}', icon_url = ctx.message.author.avatar_url)
					await channel.send(embed = banid)
					await member.ban()
				else:
					t = (int(tm) * 60)
					await member.ban()
					banid = discord.Embed(description=f'**{member.mention} забанен!**\n**Время:**\n{tm} минут.\n**Причина:**\n{reason}', colour= 0xFF0000)
					banid.set_author(name= f'{ctx.message.author}',icon_url=ctx.message.author.avatar_url)
					await channel.send(embed= banid)
					await asyncio.sleep(t)
					await member.unban()
					await channel.send(embed=discord.Embed(description=f'**{member.mention} разбанен!**', colour= 0x0080FF).set_author(name= f'{ctx.message.author}',icon_url=ctx.message.author.avatar_url))
		else:
			await ctx.send("У вас нету прав для использования этой комманды!", delete_after = 30)

	@commands.command(aliases = ["размут"])
	async def unmute(self, ctx, member:discord.Member = None, *, reason = "Не указана"):
		member_id = ctx.message.author.id
		channel = self.bot.get_channel(config.server_channel)
		role = discord.utils.get(ctx.guild.roles, name = config.mute_role)
		if member_id in config.owner_list:
			if not member:
				await ctx.send("Укажите пользователя!", delete_after = 30)
			else:
				await member.remove_roles(role)
				await channel.send(embed=discord.Embed(description=f'**{member.mention} размучен!**\n**Причина:**\n{reason}', colour= 0x0080FF).set_author(name= f'{ctx.message.author}',icon_url=ctx.message.author.avatar_url))
		else:
			await ctx.send("У вас нету прав для использования этой комманды!", delete_after = 30)

	@commands.command(aliases = ["мут"])
	async def mute(self, ctx, member:discord.Member = None, tm = "infinite", *, reason = "Не указана"):
		role = discord.utils.get(ctx.guild.roles, name=config.mute_role)
		member_id = ctx.message.author.id
		channel = self.bot.get_channel(config.server_channel)
		if member_id in config.owner_list:
			if not member:
				await ctx.send("Укажите пользователя!", delete_after = 30)
			else:
				if tm == 'infinite':
					muteid = discord.Embed(description=f'**{member.mention} замучен!**\n**Время:**\nДо снятия админом\n**Причина:**\n`{reason}`', colour= 0xFF0000)
					muteid.set_author(name= f'{ctx.message.author}',icon_url=ctx.message.author.avatar_url)
					await channel.send(embed = muteid)
					await member.add_roles(role)
				else:
					t = (int(tm) * 60)
					await member.add_roles(role)
					muteid = discord.Embed(description=f'**{member.mention} замучен!**\n**Время:**\n`{tm}`минут.\n**Причина:**\n`{reason}`', colour= 0xFF0000)
					muteid.set_author(name= f'{ctx.message.author}',icon_url=ctx.message.author.avatar_url)
					await channel.send(embed= muteid)
					await asyncio.sleep(t)
					await member.remove_roles(role)
					await channel.send(embed=discord.Embed(description=f'**{member.mention} размучен!**', colour= 0x0080FF).set_author(name= f'{ctx.message.author}',icon_url=ctx.message.author.avatar_url))
		else:
			await ctx.send("У вас нету прав для использования этой комманды!", delete_after=30)

	@commands.command(aliases = ["роль"])
	async def role(self, ctx, action = None, member:discord.Member = None, *, role_name = None):
		member_id = ctx.message.author.id
		channel = self.bot.get_channel(config.server_channel)
		if member_id in config.owner_list:
			if not action:
				await ctx.send("Укажите что вы хотите сделать!", delete_after = 20)
			elif not member:
				await ctx.send("Укажите пользователя!", delete_after=20)
			elif not role_name:
				await ctx.send("Укажите название роли!", delete_after=20)
			else:
				if action == 'add':
					try:
						role = discord.utils.get(ctx.guild.roles, name=role_name)
						await member.add_roles(role)
						await channel.send(embed=discord.Embed(description=f'{member.mention} выдана роль **{role}**\nРоль выдал:{ctx.message.author}',colour=0x39d0d6))
					except:
						await ctx.send('Произошла ошибка!', delete_after=20)
				elif action == 'remove':
					try:
						role = discord.utils.get(ctx.guild.roles, name=role_name)
						await member.remove_roles(role)
						await channel.send(embed=discord.Embed(description=f'У {member.mention} удалена роль **{role}**\nРоль удалил:{ctx.message.author}',colour=0x39d0d6))
					except:
						await ctx.send('Произошла ошибка!!!', delete_after=20)
		else:
			await ctx.send("У вас нету прав для использования этой комманды!", delete_after=30)

	@commands.command(aliases = ["создать_роль"])
	async def create_role(self, ctx, permissions = None, *, name = None):
		member_id = ctx.message.author.id
		channel = self.bot.get_channel(config.server_channel)
		if member_id in config.owner_list:
			if not permissions:
				await ctx.send("Укажите permissions!", delete_after=30)
			elif not name:
				await ctx.send("Укажите имя!", delete_after=30)
			else:
				try:
					embed = discord.Embed(title = 'Роль созданна!', description=f'***Название:***\n{name}\n***Permissions:***\n{permissions}',colour=0x39d0d6).set_author(name = f'{ctx.message.author}',icon_url = ctx.message.author.avatar_url).set_footer(text=str(datetime.datetime.utcnow()+datetime.timedelta(hours=3))[:19])
					await ctx.guild.create_role(name=name, permissions = discord.Permissions(int(permissions)))
					await channel.send(embed = embed)
				except:
					await ctx.send('Произошла ошибка, скорее всего вы не правельно указали permissions!!!', delete_after=30)
		else:
			await ctx.send("У вас нету прав для использования этой комманды!", delete_after=30)

	@commands.command(aliases = ["переместить"])
	async def move(self, ctx, channel: discord.VoiceChannel = None, channel2: discord.VoiceChannel = None):
	    member_id = ctx.message.author.id
	    if member_id in config.owner_list:
	        if channel == None:
	            await ctx.send('Укажите канал откуда перемещать!!!', delete_after=20)
	        elif channel2 == None:
	            await ctx.send('Укажите канал куда переместить!!!', delete_after=20)
	        else:
	            x = channel.members
	            for member in x:
	                await member.edit(voice_channel = channel2)
	    else:
	        await ctx.send("У вас нету прав для использования этой комманды!", delete_after=20)

	@commands.command(aliases = ["репорт", "жалоба"])
	async def report(self, ctx, member:discord.Member = None, *, reason = "Не указана"):
		channel = self.bot.get_channel(config.server_channel)
		author = ctx.author
		try:
			emb = discord.Embed(title='Report!!!',
				description=f'**Пользователь:**\n<@{member.id}>\n`ID: {member.id}`\n**Канал:**\n<#{ctx.message.channel.id}>\n**Причина:**`{reason}`',
				colour= 0xd4858d)
			emb.set_author(name= f'{ctx.message.author}',
				icon_url=ctx.message.author.avatar_url)
			emb.set_footer(text=str(datetime.datetime.utcnow()+datetime.timedelta(hours=3))[:19])
			await channel.send(embed=emb)

			report_embed=discord.Embed(description= f'Ваша жалоба на <@{member.id}> принята.', colour= 0xd4858d)
			report_embed.set_footer(text='Большая просьба воздержаться от спама, 1 жалобы на пользователя вполне достаточно.')
			await author.send(embed= report_embed)
		except:
			await author.send('Произошла ошибка просьба обратиться к админу сервера!!!', delete_after = 30)

def setup(bot):
    bot.add_cog(moderation(bot))
