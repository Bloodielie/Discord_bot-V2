import discord, config, asyncio, datetime, vk_api
from discord.ext import commands
from cogs.Utils.vk_post import Vkcheck
import os
import mysql.connector
from mysql.connector import Error

login = os.environ.get('login')
password_vk = os.environ.get('password_vk')
host = os.environ.get('host')
database = os.environ.get('database')
user = os.environ.get('user')
password = os.environ.get('password')

vk = vk_api.VkApi(login = login, password = password_vk)
vk.auth()

conn = mysql.connector.connect(host=host,
                   database=database,
                   user=user,
                   password=password)
cursor = conn.cursor()

class On_ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def check_vk(self):
        id1 = 0
        while True:
            while not self.bot.is_closed():
                await asyncio.sleep(60)
                newsfeed = vk.method("newsfeed.get", {"count": 1,"source_ids": -182028902})

                if newsfeed['items'][0]['post_id'] == id1:
                    pass
                else:
                    id1 = newsfeed['items'][0]['post_id']
                    channel = self.bot.get_channel(604790384098279487)

                    text = newsfeed['items'][0]['text']
                    group_icon_url = newsfeed['groups'][0]['photo_100']
                    screen_name = newsfeed['groups'][0]['screen_name']

                    check_attachments = newsfeed['items'][0].get('attachments')
                    check_copy_history = newsfeed['items'][0].get('copy_history')

                    time = newsfeed['items'][0]['date']
                    time_post = str(datetime.datetime.fromtimestamp(time)+datetime.timedelta(hours=3))[:19]

                    if text == '':
                        text = 'Отсутствует'

                    if check_copy_history is not None:
                        repost_text = check_copy_history[0]['text']
                        if repost_text == '':
                                repost_text = 'Отсутствует'
                        time_repost = check_copy_history[0]['date']
                        from_id = check_copy_history[0]['from_id']
                        id_post = check_copy_history[0]['id']
                        if str(from_id)[:1] == '-':
                            vk_url = f'https://vk.com/club{str(from_id)[1:]}'
                            post_url = f'https://vk.com/onlyezgame?w=wall{from_id}_{id_post}'
                        else:
                            vk_url = f'https://vk.com/id{from_id}'
                            post_url = f'https://vk.com/onlyezgame?w=wall{from_id}_{id_post}'

                        timerepost = str(datetime.datetime.fromtimestamp(time_repost)+datetime.timedelta(hours=3))[:19]
                        emb=discord.Embed(description= f'**Текст поста:**\n{text}\n***<Репост>***\n`Текст поста:`\n{repost_text}\n`Время поста:`\n{timerepost}\n`Ссылка на автора:`\n{vk_url}\n`Ссылка на пост:`\n{post_url}',colour= 0xB22222)
                        emb.set_author(icon_url=group_icon_url,url=f"https://vk.com/{screen_name}",name="Инсайды и рофлы")
                        emb.set_footer(text=f'Пост опубликован|{time_post}')
                        await channel.send(embed= emb)
                    elif check_attachments is None:
                        emb=discord.Embed(description= f'**Текст поста:**\n{text}',colour= 0xB22222)
                        emb.set_author(icon_url=group_icon_url,url=f"https://vk.com/{screen_name}",name="Инсайды и рофлы")
                        emb.set_footer(text=f'Пост опубликован|{time_post}')
                        await channel.send(embed= emb)
                    else:

                        Vk_Check = Vkcheck(newsfeed)

                        audio = Vk_Check.check_audio()
                        link = Vk_Check.check_link()
                        video = Vk_Check.check_video()
                        foto1 = Vk_Check.check_foto()
                        poll = Vk_Check.check_poll()
                        doc = Vk_Check.check_doc()

                        text_video = video[0]

                        text_link = link[0]

                        if foto1 != '':
                            foto_emb = foto1
                        elif video[1] != '':
                            foto_emb = video[1]
                        elif link[1] != '':
                            foto_emb = link[1]
                        else:
                            foto_emb = ''

                        emb=discord.Embed(description= f'**Текст поста:**\n{text}\n{audio}{text_link}{text_video}{poll}{doc}',colour= 0xB22222)
                        emb.set_image(url=foto_emb)
                        emb.set_author(icon_url=group_icon_url,url=f"https://vk.com/{screen_name}",name="Инсайды и рофлы")
                        emb.set_footer(text=f'Пост опубликован|{time_post}')
                        await channel.send(embed= emb)

    @commands.Cog.listener()
    async def on_ready(self):
        print('[Discord/INFO]         <Jojobot ready!>\n')

        type = discord.ActivityType
        activ = discord.Activity(name= f"!help", type= type.watching)
        await self.bot.change_presence(status=discord.Status.online, activity=activ)

        self.bot.loop.create_task(self.check_vk())

def setup(bot):
    bot.add_cog(On_ready(bot))
