import os
from datetime import datetime

pasta = input('Digite o nome da pasta que deseja trabalhar (os arquivos dentro dela serão renomeados): ')

# Definindo o diretorio de trabalho
diretorio = f'/Users/zegui/VSProjects/TestePython/assets/{pasta}'

descricao_campanha = input('Digite a descrição da campanha: ').replace(' ', '_').title()

print('')

# Mudando para o diretorio de trabalho "assets"
os.chdir(diretorio)



contador = 1

# Loop que percorre todos os arquivos do diretorio
for nome_arquivo in os.listdir(diretorio):
    # Garantindo que somente arquivos serão renomeados
    if os.path.isfile(nome_arquivo):
        # Obtendo a data de criação do arquivo
        timestamp = os.path.getctime(nome_arquivo)
        data_recebimento = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

        # Separando a extensão(.png) do nome do arquivo
        nome, extensao = os.path.splitext(nome_arquivo)

        novo_nome = f'{data_recebimento}_{descricao_campanha}{extensao}'

        # Se o arquivo não existe
        if not os.path.exists(novo_nome):
            os.rename(nome_arquivo, novo_nome)
            print(f'Renomeado: {nome_arquivo} -> {novo_nome}')
        # Se o arquivo já existe, adiciona um número contador ao final
        else:
            contador += 1
            novo_nome = f'{data_recebimento}_{descricao_campanha}{contador}{extensao}'
            os.rename(nome_arquivo, novo_nome)
            print(f'Renomeado: {nome_arquivo} -> {novo_nome}')

print('')
print('Processo de renomeação concluído.')