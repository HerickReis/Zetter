import yt_dlp
import os

from .dowloader_base import Downloader

class YTDLPDownloader(Downloader):
    async def download(self, url):
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
            'proxy': self.proxy_manager.get_random_proxy(),
            'http_headers': {'User-Agent': self.user_agent},
            'cookiefile': 'cookies.txt',
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                return True
        except Exception as e:
            print(f"yt-dlp falhou para {url}: {e}")
            return False
