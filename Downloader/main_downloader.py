import asyncio
import sys

from pathlib import Path 

from .downloaders.yt_dlp_downloader import YTDLPDownloader
from .downloaders.scraping_downloader import ScrapingDownloader
from .downloaders.playwright_downloader import PlaywrightDownloader
from .utils.config import load_config, update_proxy_list
from .utils.proxy_manager import ProxyManager

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils.paths_manipulation import verificar_arquivo

from fake_useragent import UserAgent


update_proxy_list(proxie_list=verificar_arquivo("proxies.txt"), config=verificar_arquivo("config.json"))

async def baixar_video(url, downloaders, audio_only):
    for downloader in downloaders:
        if await downloader.download(url, audio_only=audio_only):
            return True
    print(f"Falha ao baixar o vídeo de {url}")
    return False

async def processar_fila(queue, downloaders):
    while True:
        item = await queue.get()
        if item is None:
            break
        url, audio_only = item  # Obtém a URL e a opção de áudio da fila
        await baixar_video(url, downloaders, audio_only)  # Passa a opção para baixar apenas o áudio
        queue.task_done()

async def main():
    config = load_config(verificar_arquivo("config.json"))
    proxy_manager = ProxyManager(config["proxies"])
    user_agent = UserAgent().random

    # Inicializa os diferentes downloaders
    yt_dlp_downloader = YTDLPDownloader(config["download_path"], proxy_manager, user_agent)
    scraping_downloader = ScrapingDownloader(config["download_path"], proxy_manager, user_agent)
    playwright_downloader = PlaywrightDownloader(config["download_path"], proxy_manager, user_agent)

    # Lista de estratégias de download
    downloaders = [yt_dlp_downloader, scraping_downloader, playwright_downloader]

    queue = asyncio.Queue()

    # Inicia o processamento da fila de downloads
    consumidor = asyncio.create_task(processar_fila(queue, downloaders))

    while True:
        url = input("Insira a URL do vídeo (ou ' ' para encerrar): ")
        if str(url).isspace():
            await queue.put(None)  # Encerra a fila
            break

        audio_only = input("Deseja baixar apenas o áudio? (s/n): ").strip().lower() == 's'
        await queue.put((url, audio_only))  # Coloca a URL e a opção de áudio na fila

    # Aguarda o término dos downloads
    await consumidor

def run():
    asyncio.run(main())
