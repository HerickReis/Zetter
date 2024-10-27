from Downloader.main_downloader import run
from utils.paths_manipulation import verificar_arquivo

opcoes_funcionais = {1 : run, 2 : None, 3 : False}
opcoes_printaveis = ["Downloader - Baixar videos da internet", None]

switch = True

while switch:
    for pos, ops in enumerate(opcoes_printaveis):
        print(f"{pos + 1} - {ops}")
        
    escolha = int(input("Escolha uma opção: "))
    opcoes_funcionais[escolha]() if opcoes_funcionais[escolha] else print("\n",None, "\n")
