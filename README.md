# Renomeador de Arquivos em Massa

Automatize a organização de arquivos no departamento de marketing com este script Python que renomeia arquivos em massa seguindo um padrão específico.


## Funcionalidades

- **Renomeação em Massa:** Renomeie todos os arquivos de uma pasta especificada de forma automática.
- **Formato Personalizado:** Inclui a data de criação do arquivo e uma descrição personalizada da campanha (YYYY-MM-DD_Descricao.extensao).
- **Evita Sobrescritas:** Adiciona um contador para arquivos com nomes duplicados, evitando perda de dados.
- **Interface Simples:** Solicita inputs básicos do usuário para operação fácil e intuitiva.


## Instalação

1. **Clone o Repositório ou Baixe o Projeto:**

   Você pode clonar este repositório ou simplesmente copiar o projeto para o seu ambiente de trabalho.


## Uso

2. **Altere o diretório:**

   No script, a variável diretorio define o caminho da pasta onde os arquivos estão localizados. No código fornecido, o caminho padrão é: diretorio = f'/Users/zegui/VSProjects/TestePython/assets/{pasta}'

   Para ajustar o diretório do seu ambiente basta clicar com o botão direito do mouse na pasta "assets" e copiar o caminho da pasta.

   Exemplo: diretorio = f'C:/Seu/Projetos/TestePython/assets/{pasta}'

2. **Execute o Script:**

   Abra o terminal ou prompt de comando e navegue até o diretório onde o script está salvo. Execute o script com o seguinte comando:

   Windows:
   python main.py

   Mac:
   python3 main.py

3. **Forneça as Informações Solicitadas:**

   - **Nome da Pasta:** Insira o nome da pasta dentro de `/Users/zegui/VSProjects/TestePython/assets/` que contém os arquivos a serem renomeados.
   - **Descrição da Campanha:** Insira uma descrição para a campanha. Espaços serão substituídos por underscores (`_`) e a descrição será formatada com a primeira letra de cada palavra em maiúscula.

4. **Acompanhe o Processo:**

   O script irá iterar por todos os arquivos na pasta especificada, renomeando-os conforme o padrão definido. Mensagens serão exibidas no terminal para cada arquivo renomeado ou para arquivos que já existirem.
