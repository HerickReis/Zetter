import yt_dlp
import os
from .dowloader_base import Downloader

class YTDLPDownloader(Downloader):
    async def download(self, url, audio_only=False):
        ydl_opts = {
            'format': 'bestaudio' if audio_only else 'best',
            'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
            'proxy': self.proxy_manager.get_random_proxy(),
            'http_headers': {'User-Agent': self.user_agent},
            'cookiefile': './Downloader/cookies.txt',
        }

        if audio_only:
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192', 
            }]
        
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                return True
        except Exception as e:
            print(f"yt-dlp falhou para {url}: {e}")
            return False