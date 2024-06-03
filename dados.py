import sqlite3

# Conectando ao BD.
conn = sqlite3.connect('dados.db')

# Criando tabela de Livros.
conn.execute('CREATE TABLE livros (\
            id INTEGER PRIMARY KEY, \
            titulo TEXT, \
            autor TEXT, \
            editora TEXT, \
            ano_publicacao INTEGER, \
            isbn TEXT)')

# Criando tabela de Usuarios.
conn.execute('CREATE TABLE usuarios (\
            id INTEGER PRIMARY KEY, \
            nome TEXT, \
            sobrenome TEXT, \
            endereco TEXT, \
            email TEXT, \
            telefone TEXT)')

# Criando tabela de Emprestimo.
conn.execute('CREATE TABLE emprestimos (\
            id INTEGER PRIMARY KEY, \
            id_livro INTEGER, \
            id_usuario INTEGER, \
            data_emprestimo TEXT, \
            data_devolucao TEXT, \
            FOREIGN KEY (id_livro) REFERENCES livros (id), \
            FOREIGN KEY (id_usuario) REFERENCES usuarios (id))')

# Confirmando a transação
conn.commit()

# Fechando a conexão
conn.close()

print("Tabelas criadas com sucesso!")
