class Vkcheck():
    def __init__(self,newsfeed):
        self.newsfeed = newsfeed
        self.attachments = newsfeed['items'][0]['attachments']
        self.items = newsfeed['items'][0]

    def check_foto(self):
        for i in range(len(self.attachments)):
            check_foto_g = self.attachments[i].get('photo')
            if check_foto_g is not None:
                foto = check_foto_g['sizes'][3]['url']
                return f"{foto}"
            else:
                dlin = len(self.attachments)
                dlin = dlin - 1 
                if i == dlin:
                    return ''

    def check_audio(self):
        for i in range(len(self.attachments)):
            check_audio_g = self.attachments[i].get('audio')
            if check_audio_g is not None:
                audio_url = check_audio_g['url']
                audio_artist = check_audio_g['artist']
                audio_nameaudio = check_audio_g['title']
                return f"**Аудио:**\n{audio_artist}:{audio_nameaudio}\n`Ссылка на песню:`{audio_url}\n"
            else:
                dlin = len(self.attachments)
                dlin = dlin - 1 
                if i == dlin:
                    return ''

    def check_link(self):
        for i in range(len(self.attachments)):
            check_link_g = self.attachments[i].get('link')
            if check_link_g is not None:
                title = check_link_g['title']
                foto = check_link_g['photo']['sizes'][4]['url']
                url_stat = check_link_g["url"]
                return [f"**Статья:**\n`Название:`{title}\n`Ссылка на статью:`{url_stat}\n", f"{foto}"]
            else:
                dlin = len(self.attachments)
                dlin = dlin - 1 
                if i == dlin:
                    return ['', '']

    def check_video(self):
        for i in range(len(self.attachments)):
            check_video_g = self.attachments[i].get('video')
            if check_video_g is not None:
                video_title = check_video_g['title']
                video_description = check_video_g['description']
                source_id = self.items['source_id']
                post_id = self.items['post_id']
                video_url = f'https://vk.com/onlyezgame?w=wall{source_id}_{post_id}'
                if video_description == '':
                    video_description = 'Отсутствует'
                foto = check_video_g['photo_800']  
                return [f"**Видео:**\n`Название:`{video_title}\n`Описание:`{video_description}\n`Ссылка на видео:`{video_url}\n", f"{foto}"]
            else:
                dlin = len(self.attachments)
                dlin = dlin - 1 
                if i == dlin:
                    return ['', '']

    def check_poll(self):
        for i in range(len(self.attachments)):
            check_poll_g = self.attachments[i].get('poll')
            if check_poll_g is not None:
                question = check_poll_g['question']
                return f"**Опрос:**\n`Название:`{question}\n"
            else:
                dlin = len(self.attachments)
                dlin = dlin - 1 
                if i == dlin:
                    return ''
                    
    def check_doc(self):
        for i in range(len(self.attachments)):
            check_doc_g = self.attachments[i].get('doc')
            if check_doc_g is not None:
                title = check_doc_g['title']
                form = check_doc_g['ext']
                url = check_doc_g['url']
                return f"**Документ:**\n`Название:`{title}\n`Формат:`{form}\n`Ссылка:`{url}\n"
            else:
                dlin = len(self.attachments)
                dlin = dlin - 1 
                if i == dlin:
                    return ''