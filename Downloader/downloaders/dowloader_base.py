import os

class Downloader:
    def __init__(self, download_path, proxy_manager, user_agent):
        self.download_path = download_path
        self.proxy_manager = proxy_manager
        self.user_agent = user_agent

    async def download(self, url):
        raise NotImplementedError("Método de download deve ser implementado.")

    def _save_file(self, content, file_name):
        file_path = os.path.join(self.download_path, file_name)
        with open(file_path, 'wb') as f:
            f.write(content)
        print(f"Arquivo salvo em {file_path}")
