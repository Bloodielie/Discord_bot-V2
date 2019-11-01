import discord
from discord.ext import commands
import requests
import json
import os
from datetime import datetime
from cogs.utils import getdota
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class dota(commands.Cog):
	def __init__(self,bot):
		self.bot = bot

	@commands.command()
	async def info_dota(self, ctx, id: int = None):
		if id == None:
			await ctx.send("Укажите ид игрока")
		else:
			await ctx.channel.trigger_typing()
			r = requests.get(f"https://api.stratz.com/api/v1/Player/{id}/basic")
			m = requests.get(f"https://api.stratz.com/api/v1/Player/{id}/matches")
			player_basic = json.loads(r.text)
			player_matches = json.loads(m.text)

			a = os.path.join(os.path.dirname(__file__),'..','json','rank.json')
			rank = json.load(open(a, encoding="UTF-8"))

			steamAccount = player_basic['steamAccount']
			Anonymous = steamAccount['isAnonymous']
			if Anonymous == False:
				try:
					last_matches_id = player_matches[0]['id']
					seasonRank = str(steamAccount['seasonRank'])
					name = steamAccount['name']
					seasonLeaderboardRank = steamAccount.get('seasonLeaderboardRank')
					url_profil = steamAccount['profileUri']

					if seasonLeaderboardRank is None:
						emb=discord.Embed(description= f'**{name}**\nЗвание:**{rank[seasonRank]}**\nПоследний матч:**{last_matches_id}**\nСсылка на профиль steam:{url_profil}',colour= 0x5F9EA0)
						await ctx.send(embed=emb)
					else:
						emb=discord.Embed(description= f'**{name}**\nЗвание:**{rank[seasonRank]}**\nМесто в таблице лидеров:**{seasonLeaderboardRank}**\nПоследний матч:**{last_matches_id}**\nСсылка на профиль steam:{url_profil}',colour= 0x5F9EA0)
						await ctx.send(embed=emb)
				except KeyError:
					await ctx.send("У человека нету ранга!!!")
				except:
					await ctx.send("Произошла ошибка просьба обратиться к админу!!!")
			else:
				await ctx.send("Профиль анонимен!!!")

	@commands.command()
	async def last_matches(self, ctx, id: int = None):
		if id == None:
			await ctx.send("Укажите ид игрока")
		else:	
			await ctx.channel.trigger_typing()
			r = requests.get(f"https://api.stratz.com/api/v1/Player/{id}/basic")
			m = requests.get(f"https://api.stratz.com/api/v1/Player/{id}/matches")
			player_matches = json.loads(m.text)
			player_basic = json.loads(r.text)

			rank = json.load(open(os.path.join(os.path.dirname(__file__),'..','json','rank.json'), encoding="UTF-8"))
			winteam = json.load(open(os.path.join(os.path.dirname(__file__),'..','json','winteam_b.json'), encoding="UTF-8"))
			lane_players = json.load(open(os.path.join(os.path.dirname(__file__),'..','json','lane.json'), encoding="UTF-8"))

			steamAccount = player_basic['steamAccount']
			Anonymous = steamAccount['isAnonymous']
			if Anonymous == False:
				try:
					last_matches_id = player_matches[0]['id']
					name = steamAccount['name']
					seasonLeaderboardRank = steamAccount.get('seasonLeaderboardRank')
					seasonRank = str(player_basic['steamAccount']['seasonRank'])

					matches = json.loads(requests.get(f"https://api.opendota.com/api/matches/{last_matches_id}").text)

					dota = getdota.Get(id=id)

					status_game = dota.win_or_lose()

					localized_name = dota.player_hero()

					durations = dota.matches_duration()

					kill = player_matches[0]['players'][0]['numKills']
					death = player_matches[0]['players'][0]['numDeaths']
					assist = player_matches[0]['players'][0]['numAssists']

					heroDamage = player_matches[0]['players'][0]['heroDamage']
					heroHealing = player_matches[0]['players'][0]['heroHealing']
					towerDamage = player_matches[0]['players'][0]['towerDamage']

					Networth = player_matches[0]['players'][0]['goldSpent']
					LastHits = player_matches[0]['players'][0]['numLastHits']
					Denies = player_matches[0]['players'][0]['numDenies']
					level = player_matches[0]['players'][0]['level']
					GPM = player_matches[0]['players'][0]['goldPerMinute']
					XPM = player_matches[0]['players'][0]['experiencePerMinute']

					time_1 = dota.end_time()

					time = dota.fb_time()

					items0 = dota.items_1()
					items1 = dota.items_2()
					items2 = dota.items_3()
					items3 = dota.items_4()
					items4 = dota.items_5()
					items5 = dota.items_6()

					get_won = str(player_matches[0]['didRadiantWin'])
					dire_or_rediant = winteam[get_won]


					script_dir = os.path.dirname(__file__)

					fons_way = "../json/fons.png"
					radiant_way = "../json/radiant.png"
					dire_way = "../json/dire.png"
					photo_semioption = os.path.join(script_dir, fons_way)
					radiant_semioption = os.path.join(script_dir, radiant_way)
					dire_semioption = os.path.join(script_dir, dire_way)
					photo = Image.open(photo_semioption)
					radiant = Image.open(radiant_semioption)
					dire = Image.open(dire_semioption)


					font_way = "../font/hoboSTD.ttf"
					font_player_way = "../font/arial_unicode_bold.ttf"
					font_kda_way = "../font/hoboSTD.ttf"

					font_semioption = os.path.join(script_dir, font_way)
					font_player_way_semioption = os.path.join(script_dir, font_player_way)
					font_kda_way_semioption = os.path.join(script_dir, font_kda_way)	

					font = ImageFont.truetype(font_semioption, 30)
					font_player = ImageFont.truetype(font_player_way_semioption, 23)
					font_kda = ImageFont.truetype(font_kda_way_semioption, 20)

					if get_won == "True":
						side = radiant
						color = (10, 143, 19)
					else:
						side = dire
						color = (158, 11, 11)

					color_players = (255, 255, 255)

					side = side.resize((40,40))
					width, height = photo.size
					transparent = Image.new('RGBA', (width, height), (0,0,0,0))
					transparent.paste(photo, (0,0))
					transparent.paste(side, mask=side)
					drawing = ImageDraw.Draw(transparent)
					h = 32
					hero_y = 28
					text_y = 26
					items_y = 31
					for i in range(0, 10):
						h = h + 32
						hero_y = hero_y + 32
						text_y = text_y + 32
						items_y = items_y + 32
						try:
							abx = matches["players"][i]["personaname"]
							nick = abx[:15]
							drawing.text((38, text_y), nick, fill=color_players, font=font_player)

						except:
							drawing.text((38, text_y), "Anonimus", fill=color_players, font=font_player)

						hero_id = matches["players"][i]["hero_id"]
						hero_way = f"../image/{hero_id}.png"
						hero_semioption = os.path.join(script_dir, hero_way)
						hero_img = Image.open(hero_semioption)
						hero_img = hero_img.resize((30,30))
						transparent.paste(hero_img, (2,hero_y), mask=hero_img)

						try:
							kill = matches["players"][i]["kills"]
							if kill >= 10:
								drawing.text((289, h), str(kill), fill=color_players, font=font_kda)
							else:
								drawing.text((294, h), str(kill), fill=color_players, font=font_kda)
						except:
							drawing.text((294, h), 'er', fill=color_players, font=font_kda)			

						try:
							death = matches["players"][i]["deaths"]
							if death >= 10:
								drawing.text((315, h), str(death), fill=color_players, font=font_kda)
							else:
								drawing.text((320, h), str(death), fill=color_players, font=font_kda)
						except:
							drawing.text((320, h), 'er', fill=color_players, font=font_kda)		

						try:
							assist = matches["players"][i]["assists"]
							if assist >= 10:
								drawing.text((341, h), str(assist), fill=color_players, font=font_kda)
							else:
								drawing.text((346, h), str(assist), fill=color_players, font=font_kda)
						except:
							drawing.text((346, h), 'er', fill=color_players, font=font_kda)		

						try:
							GPM = matches["players"][i]["gold_per_min"]
							drawing.text((376, h), str(GPM), fill=color_players, font=font_kda)
						except:
							drawing.text((376, h), 'er', fill=color_players, font=font_kda)		

						try:
							XPM = matches["players"][i]["xp_per_min"]
							drawing.text((432, h), str(XPM), fill=color_players, font=font_kda)
						except:
							drawing.text((432, h), 'er', fill=color_players, font=font_kda)	

						try:
							damage = matches["players"][i]["hero_damage"]
							drawing.text((485, h), str(damage), fill=color_players, font=font_kda)
						except:
							drawing.text((485, h), 'er', fill=color_players, font=font_kda)				

						items_vopr_way = "../items_png/1666.png"
						items_vopr_semioption = os.path.join(script_dir, items_vopr_way)

						items_vopr = Image.open(items_vopr_semioption)
						items_vopr = items_vopr.resize((35,25))
						items = []
						for r in range(0,6):
							items_1 = matches["players"][i][f"item_{r}"]
							items.append(items_1)
							
						items.sort(reverse=True)

						items_x = 550
						for i in range(0,6):
							try:
								items_x = items_x + 40
								items_dota_way = f"../items_png/{items[i]}.png"
								items_dota_semioption = os.path.join(script_dir, items_dota_way)

								items_dota = Image.open(items_dota_semioption).convert("RGBA")
								items_dota = items_dota.resize((35,25))
								transparent.paste(items_dota, (items_x,items_y), mask=items_dota)
							except Exception as e:
								transparent.paste(items_vopr, (items_x,items_y))
								print(e)

					color_green = (10, 143, 19)
					color_red = (158, 11, 11)
					drawing.line([0, 63, 0, 212], fill=color_green, width=6)
					drawing.line([0, 213, 0, 450], fill=color_red, width=6)
					drawing.text((38, 6), dire_or_rediant, fill=color, font=font)

					image_way11 = "../cogs/fone.png"
					image_semioption = os.path.join(script_dir, image_way11)	

					way_forfile_save = os.path.dirname(os.path.abspath(image_semioption))

					transparent.save(f"{way_forfile_save}\\dota_fons.png")


					if seasonLeaderboardRank is None:
						image_way = "../cogs/dota_fons.png"
						image_semioption = os.path.join(script_dir, image_way)	

						image = discord.File(image_semioption, "fone.png")
						emb=discord.Embed(title= f"**{name} - {rank[seasonRank]}**", description= f'{status_game} a game as {localized_name} in {durations}\nMore info:First Blood in {time}Id matches:{last_matches_id}.',colour= 0x5F9EA0)
						emb.add_field(name='**Economy**', value =f'Net Worth: {Networth}\nLast Hits: {LastHits}\nDenies: {Denies}\nLevel: {level}\nGPM: {GPM}\nXPM: {XPM}')	
						emb.add_field(name='**Items**', value =f'1.{items0}\n2.{items1}\n3.{items2}\n4.{items3}\n5.{items4}\n6.{items5}')
						emb.add_field(name='**Damage**', value =f'KDA:**{kill}/{death}/{assist}**\nHero Damage: {heroDamage}\nHero Healing: {heroHealing}\nTower Damage: {towerDamage}')
						emb.set_footer(text=f'End game | {time_1}')	
						emb.set_image(url=f"attachment://{image.filename}")											
						await ctx.send(embed=emb, file=image)
					else:
						emb=discord.Embed(title= f"**{name} - {rank[seasonRank]}[{seasonLeaderboardRank}]**", description= f'{status_game} a game as {localized_name} in {durations}\nMore info:First Blood in {time}Id matches:{last_matches_id}.',colour= 0x5F9EA0)
						emb.add_field(name='**Economy**', value =f'Net Worth: {Networth}\nLast Hits: {LastHits}\nDenies: {Denies}\nLevel: {level}\nGPM: {GPM}\nXPM: {XPM}')	
						emb.add_field(name='**Items**', value =f'1.{items0}\n2.{items1}\n3.{items2}\n4.{items3}\n5.{items4}\n6.{items5}')
						emb.add_field(name='**Damage**', value =f'KDA:**{kill}/{death}/{assist}**\nHero Damage: {heroDamage}\nHero Healing: {heroHealing}\nTower Damage: {towerDamage}')
						emb.set_footer(text=f'End game | {time_1}')											
						await ctx.send(embed=emb)
				except KeyError:
					await ctx.send("У человека нету ранга!!!")
			else:
				await ctx.send("Профиль анонимен!!!")

def setup(bot):
    bot.add_cog(dota(bot))	