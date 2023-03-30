# Gerador de QR Code

    Este é um gerador de QR Code construído com Python e Flask. Ele permite que o usuário preencha um formulário com seu nome, LinkedIn e GitHub, e gere um QR Code com um link para seu perfil.

## Funcionalidades

    Geração de QR Code a partir do formulário preenchido pelo usuário
    Visualização do perfil do usuário com as informações fornecidas no formulário
    API para acessar as informações dos QR Codes gerados

## Instalação

    1.Clone o repositório para sua máquina local
    2.Instale as dependências com o comando pip install -r requirements.txt
    3.Inicie o servidor com o comando python run.py

## Uso

    4.Acesse o endereço http://localhost:5000 em seu navegador
    5.Preencha o formulário com seu nome, LinkedIn e GitHub
    6.Clique em "Gerar QR Code"
    7.O QR Code será gerado e exibido na página
    8.Clique em seu nome na página para visualizar seu perfil com as informações fornecidas
    9.Acesse http://localhost:5000/api_entries para obter as informações dos QR Codes gerados em formato JSON
