import aiohttp
import os
import subprocess
from bs4 import BeautifulSoup
from .dowloader_base import Downloader

class ScrapingDownloader(Downloader):
    async def download(self, url, audio_only=False):
        proxy = self.proxy_manager.get_random_proxy()
        headers = {'User-Agent': self.user_agent}

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers, proxy=proxy) as response:
                    if response.status != 200:
                        return False
                    
                    soup = BeautifulSoup(await response.text(), 'html.parser')
                    video_tags = soup.find_all(['video', 'source'])
                    
                    for video in video_tags:
                        video_src = video.get('src')
                        if video_src:
                            await self._download_video(video_src, audio_only=audio_only)
                            return True
            return False
        except Exception as e:
            print(f"Erro no scraping: {e}")
            return False

    async def _download_video(self, video_src, audio_only=False):
        filename = os.path.join(self.download_path, "temp_video.mp4")
        
        # Baixa o vídeo diretamente
        print(f"Baixando vídeo de {video_src}...")
        async with aiohttp.ClientSession() as session:
            async with session.get(video_src) as response:
                if response.status == 200:
                    with open(filename, 'wb') as f:
                        f.write(await response.read())

        # Se apenas o áudio for necessário, converte para MP3 usando ffmpeg
        if audio_only:
            mp3_filename = os.path.join(self.download_path, "audio.mp3")
            print("Convertendo para MP3...")
            subprocess.run(["ffmpeg", "-i", filename, "-vn", "-acodec", "mp3", "-q:a", "192", mp3_filename])
            os.remove(filename)  # Remove o vídeo temporário após a conversão
        else:
            print("Vídeo baixado com sucesso.")

