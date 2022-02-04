'''Listando os arquivos de uma determinada extensão'''

import os

#Define o diretório a procurar
folder = './Downloads'

# Criar uma lista com todos os arquivos
# que estão contidos no diretório e que 
# possuem a extensão desejada
arquivos = list(
    arquivo for arquivo in os.listdir(folder)
    if arquivo.lower().endswith('.png')
)
print(arquivos)
#[arquivo_].csv, arquivo_.csv, arquivo_.csv]