import os
from googleapiclient.discovery import build
import isodate
from datetime import timedelta

api_key: str = os.getenv('YT_API_KEY')


class PlayList:
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id: str):

        self.playlist_id = playlist_id
        self.title = self.playlist_info()['items'][0]['snippet']['localized']['title']  # название плейлиста
        self.url = f'https://www.youtube.com/playlist?list={playlist_id}'  # ссылка на плейлист
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id, part='contentDetails',
                                                                 maxResults=50).execute()  # получение данных по видеороликам в плейлисте

        self.video_ids = [video['contentDetails']['videoId'] for video in
                          self.playlist_videos['items']]  # получение всех id видеороликов из плейлиста
        # print(self.video_ids)
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                         id=','.join(self.video_ids)).execute()  # получение длительности видеороликов из плейлиста

    def playlist_info(self):
        """получение данные по play-листам канала"""
        playlist_videos = self.youtube.playlists().list(part='snippet', id=self.playlist_id, ).execute()
        return playlist_videos

    @property
    def total_duration(self):
        """возвращает объект класса datetime.timedelta с суммарной длительность плейлиста"""
        max_time = timedelta()
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            # print(duration)
            max_time += duration
        return max_time

    def show_best_video(self):
        """возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)"""
        likes = 0
        best_video_url = ''

        for video_id in self.video_ids:
            request_to_videos = self.youtube.videos().list(part='statistics', id=video_id).execute()

            like_count = request_to_videos['items'][0]['statistics']['likeCount']
            # print(like_count)

            if int(like_count) > likes:
                likes = int(like_count)
                best_video_url = f"https://youtu.be/{request_to_videos['items'][0]['id']}"
        # print(best_video_url)

        return best_video_url
