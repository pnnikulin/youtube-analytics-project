import json
from googleapiclient.discovery import build
import os

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения




#channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'



class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = 'MoscowPython'
        self.description = ''
        self.url = 'https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A'
        self.subscriberCount = ''
        self.video_count = 687
        self.viewCount = ''


    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


    def print_info(self) -> str:
        """Выводит в консоль информацию о канале."""
        youtube = self.get_service()
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriberCount = channel['items'][0]['statistics']['subscriberCount']
        self.videoCount = channel['items'][0]['statistics']['videoCount']
        self.viewCount = channel['items'][0]['statistics']['viewCount']
        return (f'id канала: {self.channel_id}\n\n'
                f'название канала: {self.title}\n\n'
                f'описание канала: {self.description}\n\n'
                f'ссылка на канал: {self.url}\n\n'
                f'количество подписчиков: {self.subscriberCount}\n\n'
                f'количество видео: {self.videoCount}\n\n'
                f'общее количество просмотров: {self.viewCount}')


    def to_json(self, data):
        self.data = data
        youtube = self.get_service()
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriberCount = channel['items'][0]['statistics']['subscriberCount']
        self.videoCount = channel['items'][0]['statistics']['videoCount']
        self.viewCount = channel['items'][0]['statistics']['viewCount']

        self.data = {self.channel_id: []}
        self.data[self.channel_id].append({'название канала': self.title, 'описание канала': self.description, 'ссылка на канал': self.url})

        print(self.data)
        print(type(self.data))

        with open('data.json', 'w', 'utf-8', indent=2, ensure_ascii=False) as outfile:
            json.dump(self.data, outfile)

#json.dumps(channel, indent=2, ensure_ascii=False)