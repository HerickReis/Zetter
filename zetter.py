from Downloader.main_downloader import run
from utils.paths_manipulation import verificar_arquivo

opcoes_funcionais = {1 : run, 2 : None, 3 : False}
opcoes_printaveis = ["Downloader - Baixar videos da internet", None]

switch = True

while switch:
    for pos, opc in enumerate(opcoes_printaveis):
        print(f"{pos + 1} - {opc}")
        
    escolha = int(input("Escolha uma opção: "))
    if opcoes_funcionais[escolha]:
        opcoes_funcionais[escolha]()
        
    else:
        switch = False
