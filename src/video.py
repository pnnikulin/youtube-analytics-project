import os
import json
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')


class Video:
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str) -> None:
        self.video_id = video_id  # id video
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails,'
                                                              'liveStreamingDetails,player',
                                                         id=video_id).execute()  # запрос к youtube по id video

        #print(json.dumps(self.video_response, indent=2, ensure_ascii=False))  # для просмотра в JSON формате
        self.video_title: str = self.video_response['items'][0]['snippet']['title']  # название видео
        self.video_url: str = self.video_response['items'][0]['player']['embedHtml']  # ссылка на видео в HTML  строке
        self.video_url_direct = f"www.youtube.com/embed/{self.video_id}"  #ссылка на видео через video_id
        self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']  # количество просмотров
        self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']  # количество лайков
        self.comment_count: int = self.video_response['items'][0]['statistics']['commentCount']  # количество комментов

    def __str__(self):
        return f"{self.video_title}"


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str) -> None:
        super().__init__(video_id)
        self.playlist_id = playlist_id
