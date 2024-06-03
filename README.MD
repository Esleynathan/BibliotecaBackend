## Sistema de Biblioteca ##

Informação do Projeto
Este é um projeto de um sistema de backend para uma biblioteca, desenvolvido como parte da graduação em Engenharia da Computação. O sistema permite gerenciar livros, usuários e empréstimos de forma eficiente.


Desenvolvedores:
Nome: Ésley Nathan Gomes Barbosa
Matrícula: 2020102355
Nome: Tayron do Amaral Moreira
Matrícula: 2020101510


Instruções de Uso:
Pré-requisitos
Python 3.x
Biblioteca sqlite3 (inclusa no Python padrão)


Passo a Passo para Execução
Clone o repositório:

bash
git clone https://github.com/Esleynathan/BibliotecaBackend
cd BibliotecaBackend
Execute o script dados.py para criar as tabelas no banco de dados:

bash
python dados.py
Execute o script main.py para iniciar o sistema:

bash
python main.py


Funcionalidades Disponíveis:
Inserir um novo livro
Inserir um novo usuário
Realizar um empréstimo
Atualizar a data de devolução de um empréstimo
Exibir todos os livros cadastrados
Exibir todos os livros disponíveis
Exibir todos os livros emprestados no momento
Exibir usuários cadastrados no sistema


Estrutura do Projeto:
dados.py: Script responsável por criar as tabelas do banco de dados.
main.py: Script principal que contém o loop do menu para interação com o usuário.
view.py: Script que contém as funções de manipulação do banco de dados.