# B&S Investimentos

A aplicação B&S Investimentos foi desenvolvida como parte dos requisitos da disciplina de Banco de Dados 1, 
no curso de Engenharia de Computação. O projeto foi construído utilizando o framework Flask e o banco de dados SQLite3,
seguindo a arquitetura Blueprint. As ferramentas de marcação HTML e CSS foram empregadas para a estrutura e o design da interface, 
enquanto o Javascript foi utilizado para adicionar funcionalidades a determinadas partes da aplicação. Além disso, o DB Browser 
foi utilizado para manipular e gerenciar o banco de dados, facilitando a visualização e edição dos dados armazenados.

# Requisitos para executar a aplicação em sua máquina (Windows)

## 1ª Etapa 
Vamos clonar o repositório que contém o projeto.
```
  git clone https://github.com/SilveiraGustavo/App_Flask.git 
```

## 2º Etapa 
Certifique-se de ter o Python 3 instalado em sua máquina. Você pode baixar e instalar a versão mais recente a partir do site oficial do Python. Disponível em https://www.python.org/downloads/ 

## 3ª Etapa 
Deverá navegar até pasta que você fez o clone do projeto 
```
  cd/seudiretorio
```
## 4ª Etapa 
Após navegar até o diretório do projeto, você deverá executar o seguinte comando no CMD para criar um ambiente virtual para a aplicação:
```
python -m venv venv
```
## 5ª Etapa
Após concluir a criação do ambiente virtual, o próximo passo é ativar o ambiente virtual em sua máquina. Com o seguinte comando:
```
.\venv\Scripts\activate
```
## 6ª Etapa 
Após completar as etapas anteriores, estamos quase prontos para executar a aplicação. O próximo passo é instalar as bibliotecas necessárias que foram utilizadas no projeto.

```
pip install flask, flask_login, flask_sqlalchemy
```
## Como utilizar o sistema

Para utilizar o sistema, você poderá criar uma conta na tela principal. Preencha os campos "Username", "Email" e "Senha". Após preencher os campos, clique no botão "Registrar". Você será redirecionado para a página de login, onde poderá iniciar uma sessão com o usuário que acabou de criar.

Após realizar o login com a conta criada, você será redirecionado para uma página chamada "Home", onde poderá cadastrar seus ativos e excluir aqueles que desejar remover. 

Nessa mesma página voce poderá também navegar em um menu lateral onde tem opções de "Cadastrar Ativos" e algumas outras, mas não foi possível implementar as outras funcionalidades. O usuário pode encerrar sua seção através de um botão disponível no menu lateral na opção "Sair". 