import json
from googleapiclient.discovery import build
import os

api_key: str = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.api_response = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.api_response['items'][0]['snippet']['title']
        self.description = self.api_response['items'][0]['snippet']['description']
        self.url = self.api_response['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriberCount = self.api_response['items'][0]['statistics']['subscriberCount']
        self.video_count = self.api_response['items'][0]['statistics']['videoCount']
        self.viewCount = self.api_response['items'][0]['statistics']['viewCount']


    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def print_info(self) -> str:
        """Выводит в консоль информацию о канале."""
        youtube = self.get_service()
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel

    def to_json(self, output_file):
        self.output_file = output_file
        self.data = [self.title, self.description, self.url, self.subscriberCount, self.video_count,
                     self.viewCount]

        self.json_data = json.dumps(self.data, ensure_ascii=False, sort_keys=False, indent=4)

        print(self.json_data)

        with open(self.output_file, 'w') as outfile:
            outfile.write(self.json_data)

