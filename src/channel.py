import json
from googleapiclient.discovery import build
import os

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)

channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'
channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self, youtube) -> str:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return json.dumps(channel, indent=2, ensure_ascii=False)