from pathlib import Path

def verificar_arquivo(nome_arquivo, diretorio_raiz='.', criar_arquivo = False):
    """
    A função tem como objetivo buscar um arquivo e retornar seu caminho completo
    
    Args:
        nome_arquivo (str): Nome do arquivo que será buscado.
        diretorio_raiz (str, optional): Diretório em que a busca será realizada. Padrão como '.'(Diretório atual).

    Returns:
        str: Caso encontrado o caminho para o arquivo será retornado
    """
    
    # Cria um objeto Path para o diretório raiz e para o nome do arquivo
    raiz = Path(diretorio_raiz)
    arquivo = Path(nome_arquivo)
    
    # Busca recursivamente pelo arquivo em todas as subpastas
    for caminho in raiz.rglob(nome_arquivo):

        if caminho.is_file():  # Verifica se é um arquivo (e não um diretório)
            # Retorna o caminho completo do arquivo
            return str(caminho.resolve())

    if criar_arquivo:
        arquivo.touch()
        return f"Arquivo: <{nome_arquivo}> criado em {str(arquivo.resolve())}"

    return None


def buscar_todos_arquivos(nome_arquivo, diretorio_raiz='.'):
    """A função tem como objetivo buscar todos arquivos em um diretório e retornar uma lista com seus respectivos caminhos
        

        Pode ser usado discos para busca Ex: C:/, D:/, E:/...
        
    Args:
        nome_arquivo (str): Nome do arquivo a ser buscado
        diretorio_raiz (str, optional): Diretório onde irá ser realizada a busca. Padrão como '.'(Diretório atual).

    Returns:
        list: Retorna uma lista de strings dos caminhos do arquivo procurado
    """    
    # Cria um objeto Path para o diretório raiz
    raiz = Path(diretorio_raiz)
    
    # Lista para armazenar os caminhos encontrados
    caminhos_encontrados = []
    
    # Busca recursivamente por todos os arquivos que correspondem ao nome
    for caminho in raiz.rglob(nome_arquivo):
        if caminho.is_file():  # Verifica se é um arquivo (e não um diretório)
            # Adiciona o caminho completo à lista
            caminhos_encontrados.append(str(caminho.resolve()))
    
    # Retorna a lista de caminhos encontrados
    return caminhos_encontrados


def criar_pastas(pasta:str, arquivos_internos=None,diretorio="."):
    nova_pasta = Path(pasta)
    nova_pasta.mkdir(parents=True, exist_ok=True)
    
    print(nova_pasta)
    if arquivos_internos:
        # Caso haja valores na variável arquivos_internos, irá percorrer e criar as pastas internas
        for arq in arquivos_internos:
            # adiciona o arquivo ao diretório no objeto padrão
            arquivo = nova_pasta / Path(arq)
            # cria os arquivos internos
            arquivo.touch()

