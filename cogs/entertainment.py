import discord, asyncio, random, nekos, config
from discord.ext import commands

class entertainment(commands.Cog):
	def __init__(self,bot):
		self.bot = bot

	@commands.command(aliases= ["рулетка","ролл"])
	async def roll(self, ctx, *, number = None):
		if not number:
			roll = random.randint(0, 100)
			author = ctx.message.author
			await ctx.send(embed = discord.Embed(description= f"{author.mention} заролли {roll}\nДиапазон:0-100", colour= 0x333333).set_image(url = config.roll_url), delete_after = 20)			
		else:
			number = str(number)
			number = number.split("-")
			number1 = number[0]
			number2 = number[1]
			if number1.isdigit() and number2.isdigit():
				roll = random.randint(int(number1), int(number2))
				author = ctx.message.author
				await ctx.send(embed = discord.Embed(description= f"{author.mention} заролли {roll}\nДиапазон:{number1}-{number2}", colour= 0x333333).set_image(url = config.roll_url), delete_after = 20)
			else:
				await ctx.send("Укажите правильно диапазон!", delete_after = 20)

	@commands.command(aliases= ["фото"])
	async def picture(self, ctx, category = None):
		if not category:
			await ctx.send('Укажите категорию!', delete_after = 20)
		elif category == 'cat' or category == 'кот':
			cate = nekos.cat()
			emb = discord.Embed(title ='Котик', colour = 0xFFFF00).set_image(url = cate)
			await ctx.send(embed = emb, delete_after = 30)
		elif category == 'niga' or category == 'негр':
			niga = ['https://pp.userapi.com/c854220/v854220634/85517/DHd7sQSMj1w.jpg','https://pp.userapi.com/c7003/v7003293/6666f/HXL2tqecltc.jpg','https://pp.userapi.com/c845120/v845120976/107eda/eXrmmB7e1mU.jpg','https://pp.userapi.com/c848632/v848632123/f08ea/lIbE35c1-xo.jpg','https://pp.userapi.com/c635103/v635103260/53ce5/fPqWBHrwxDs.jpg','https://sun9-11.userapi.com/c848528/v848528900/de57b/yCRj3AzAjhk.jpg','https://pp.userapi.com/c846021/v846021236/158e98/zk5D9NbQKWU.jpg','https://pp.userapi.com/c846217/v846217824/1034ec/VdG0wv6bjU8.jpg','https://pp.userapi.com/c540100/v540100156/5004a/5I-R0zGmXF8.jpg'] 
			num = random.choice(niga)
			await ctx.send(embed = discord.Embed(title='**niga**', colour=0x0000FF).set_image(url=num), delete_after = 30)
		elif category == 'anime_t9n' or category == 'wallpaper' or category == 'content' or category == 'hentai' or category == '4len':
			if ctx.message.channel.is_nsfw() == True:
				if category == 'anime_t9n' or category == 'аниме_тян':
					num = random.randint(1,2)
					if num == 1:
						ngif = nekos.img('ngif')
						await ctx.send(embed=discord.Embed(title='**Аниме тян +18**', colour=0xFF00FF).set_image(url=ngif), delete_after = 20)
					else:
						fox_girl = nekos.img('fox_girl')
						await ctx.send(embed=discord.Embed(title='**Аниме тян +18**', colour=0xFF00FF).set_image(url=fox_girl), delete_after = 20)
				elif category == 'wallpaper':
					wallpaper = nekos.img('wallpaper')
					await ctx.send(embed=discord.Embed(title='**Рандомныя картинка +18**', colour=0x0080FF).set_image(url=wallpaper), delete_after = 20)
				elif category == 'content' or category == 'контект':
					porno = ['https://pp.userapi.com/c635107/v635107235/10bac/U_4n0s8Wauo.jpg','https://pp.userapi.com/c849120/v849120574/176655/S0KgWg937vU.jpg','https://pp.userapi.com/c848524/v848524215/183447/XpVd2kwa1CI.jpg','https://sun9-33.userapi.com/c852024/v852024215/11b6f0/K_FKn3gyzAA.jpg','https://pp.userapi.com/c847221/v847221473/1f420c/PKDlfWiW_Zo.jpg','https://pp.userapi.com/c850336/v850336379/13d5d7/u3eofibL0yc.jpg','https://pp.userapi.com/c851032/v851032957/116ae2/E5J3wz9UiN4.jpg','https://pp.userapi.com/c846017/v846017918/1f3761/8vmSoG8bdzU.jpg','https://pp.userapi.com/c635107/v635107566/11a8a/USsHHOERPGU.jpg','https://pp.userapi.com/c856136/v856136919/9da41/wj0YYV2Fylw.jpg','https://pp.userapi.com/c850136/v850136926/192169/rRsbEIqHhVU.jpg','https://pp.userapi.com/c831409/v831409001/16ceee/VFoGYjBY4G4.jpg','https://pp.userapi.com/c849136/v849136855/1d37bc/j1hKpqizpXM.jpg','https://pp.userapi.com/c851228/v851228650/174f23/UWu-M7gD38s.jpg','https://pp.userapi.com/c848620/v848620571/d17ac/3E-y7uMSQEU.jpg','https://sun9-17.userapi.com/c846419/v846419643/1a0b5d/CBgobtBeS_s.jpg','https://pp.userapi.com/c849432/v849432403/1bc592/xbZggYVA6yY.jpg','https://pp.userapi.com/c850628/v850628647/159645/vn180hkZ5AM.jpg','https://pp.userapi.com/c851132/v851132957/15e3f8/FGwzk6VTqQg.jpg','https://pp.userapi.com/c851132/v851132957/15e402/Z0HAP7pPluA.jpg','https://pp.userapi.com/c852032/v852032400/13edaf/9E0aIPTzIWY.jpg','https://pp.userapi.com/c847124/v847124187/b8f60/BUrl9OE3Lxw.jpg','https://pp.userapi.com/c854220/v854220906/5aef2/R7T0naIrfcY.jpg']
					num = random.choice(porno)
					await ctx.send(embed=discord.Embed(title='**Content** `+18`', colour=0x0000FF).set_image(url=num), delete_after = 20)
				elif category == 'hentai' or category == 'хентай':
					hentai = nekos.img('random_hentai_gif')
					await ctx.send(embed=discord.Embed(title='**Hentai +18**', colour=0x0000FF).set_image(url=hentai), delete_after = 20)
				elif category == '4len' or category == 'Член':
					chlen = ['https://cdn.gayboystube.com/galleries/1815445a37fea083e17/5a37feec52e00.jpg','https://img-hw.xvideos.com/videos/profiles/galleries/8a/00/71/joy1972/gal153886/pic_118_big.jpg','http://www.allpornhome.com/aegalleries/02-amateurbigcocks-52/004.jpg','http://x.imagefapusercontent.com/u/eldivino/3479589/1646560075/pollazos_1428345662.jpg','http://dattr.com/p_content_dattr/d0beda63b295538ae1bcfee8a531a962fd3e7508/dattrcom9363cc08932408cc87c46d66f325b5762c2427a5.jpg','https://dl.backbook.me/full/5f92b8a03b.jpg','https://www.hoodtube.com/images/galleries/0386/3475/a014fc48834cba870880c3c383a35510.jpg','https://thumb-p9.xhcdn.com/a/w1HFdnPGBczNkc1LIeZ-wg/000/046/216/729_1000.jpg','http://x.fap.to/images/full/42/333/333608989.jpg','https://annamilk.com/wp-content/uploads/2015/05/bolshoj-chlen-u-parnyabolshoj-chlen-u-parnya_07.jpg']
					num = random.choice(chlen)
					await ctx.send(embed=discord.Embed(title='**4len +18**', colour=0x0000FF).set_image(url=num), delete_after = 20)
			else:
				await ctx.send('Чтобы использовать эту команду перейдите в NSFW канал!', delete_after = 30)
		else:
			await ctx.send('Напишите правильно команду!', delete_after = 20)

	@commands.command(aliases= ["монетка"])
	async def coin(self, ctx):
		rcoin = random.randint(1,2)
		author = ctx.message.author
		if rcoin == 1:
			emb = discord.Embed(description = f'**{author.mention} подкидывает монетку и выпадает ОРЁЛ**', colour = 0x333333)
			emb.set_image(url = config.coin_url)
			await ctx.send(embed= emb, delete_after = 30)
		else:
			emb = discord.Embed(description = f'**{author.mention} подкидывает монетку и выпадает РЕШКА**' , colour = 0x333333)
			emb.set_image(url= config.coin_url)
			await ctx.send(embed= emb, delete_after = 30)

	@commands.command(aliases= ["уважение", "Ф"])
	async def F(self, ctx, member: discord.Member = None):
		if not member:
			author = ctx.message.author
			emb = discord.Embed(description = f'**{author.mention} выражает уважение**' , colour = 0x333333).set_image(url = config.F_url)
			await ctx.send(embed = emb, delete_after = 30)
		else:
			author = ctx.message.author
			emb = discord.Embed(description = f'**{author.mention} выражает уважение {member.mention}**', colour = 0x333333).set_image(url = config.F_url)
			await ctx.send(embed = emb, delete_after = 30)
			try:
				await member.send(content=f'Вам выразил уважение {author.mention}!')
			except:
				pass

	@commands.command(aliases= ["есказать"])
	async def esay(self, ctx, *, text):
		color = [0x333333, 0x00ff80, 0x39d0d6, 0xFF0000]
		colors = random.choice(color)
		emd = discord.Embed(description = f'***Текст:***\n```{text}```', colour = colors).set_author(name = f'{ctx.message.author}',icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = emd, delete_after = 120)

	@commands.command(aliases= ["сказать"])
	async def say(self, ctx, *, text):
		await ctx.send(text, delete_after = 20)

def setup(bot):
    bot.add_cog(entertainment(bot))