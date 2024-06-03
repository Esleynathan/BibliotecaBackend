import sqlite3

# Função para conectar ao BD.
def connect():
    conn = sqlite3.connect('dados.db')
    return conn

# Função para cadastrar novo livro.
def cadastrar_livro(titulo,
                    autor,
                    editora,
                    ano_publicacao,
                    isbn):    
    conn = connect()
    conn.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn)\
                 VALUES (?, ?, ?, ?, ?)", (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()
    conn.close()
    
    return print("Livro cadastrado com sucesso.")

# Função para cadastrar usuário.
def cadastrar_usuario(nome,
                      sobrenome,
                      endereco,
                      email,
                      telefone):    
    conn = connect()
    conn.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone)\
                 VALUES (?, ?, ?, ?, ?)", (nome, sobrenome, endereco, email, telefone))
    conn.commit()
    conn.close()

    return print("\nUsuário cadastrado com sucesso.")

# Função para emprestar livros.
def cadastrar_emprestimo(id_livro,
                         id_usuario,
                         data_emprestimo,
                         data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao)\
                 VALUES (?, ?, ?, ?)", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

    return print("\nEmprestimo cadastrado com sucesso.")

# Função para exibir livros.
def exibir_livros():
    conn = connect()
    try:
        livros = conn.execute("SELECT * FROM livros").fetchall()

        if not livros:
            print("\nNenhum livro encontrado.")
            return

        print("\n----------- Livros na biblioteca -----------")
        for livro in livros:
            id_livro, titulo, autor, editora, ano_publicacao, isbn = livro
            print(f"\nID: {id_livro}\nTítulo: {titulo}\nAutor: {autor}\nEditora: {editora}\nAno de Publicação: {ano_publicacao}\nISBN: {isbn}")
    except Exception as e:
        print(f"Erro ao exibir livros: {e}")
    finally:
        conn.close()

# Função para exibir usuários.
def exibir_usuarios():
    conn = connect()
    try:
        usuarios = conn.execute("SELECT * FROM usuarios").fetchall()

        if not usuarios:
            print("\nNenhum usuário encontrado.")
            return

        print("\n----------- Usuários no Sistema -----------")
        for usuario in usuarios:
            id_usuario, nome, sobrenome, endereco, email, telefone = usuario
            print(f"\nID: {id_usuario}\nNome: {nome}\nSobrenome: {sobrenome}\nEndereço: {endereco}\nE-mail: {email}\nTelefone: {telefone}")
    except Exception as e:
        print(f"Erro ao exibir usuários: {e}")
    finally:
        conn.close()

# Função para exibir emprestimos.
def exibir_emprestimos():
    conn = connect()
    try:
        result = conn.execute("SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao\
                                FROM livros\
                                INNER JOIN emprestimos ON livros.id = emprestimos.id_livro\
                                INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario\
                                WHERE emprestimos.data_devolucao IS NULL").fetchall()

        if not result:
            print("\nNão há nenhum livro emprestado.")
            return

        print("\n----------- Livros emprestados -----------")
        for livro in result:
            titulo, nome, sobrenome, data_emprestimo, data_devolucao = livro
            print(f"\nLivro: {titulo} \nUsuário: {nome} {sobrenome} \nData de Empréstimo: {data_emprestimo} \nData de Devolução: {data_devolucao}")
    except Exception as e:
        print(f"Erro ao exibir empréstimos: {e}")
    finally:
        conn.close()
        
# Função para devolver livros.
def devolver_emprestimo(id_emprestimo, data_devolucao):
    conn = connect()
    try:
        conn.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (data_devolucao, id_emprestimo))
    except Exception as e:
        print(f"Erro ao devolver emprestimo: {e}")
    finally:
        conn.commit()
        conn.close()

# Função para exibir disponiveis.
def exibir_disponiveis():
    conn = connect()
    try:
        result = conn.execute('''SELECT livros.id, livros.titulo, livros.autor, livros.editora, livros.ano_publicacao, livros.isbn
                                 FROM livros
                                 LEFT JOIN emprestimos ON livros.id = emprestimos.id_livro
                                 WHERE emprestimos.id IS NULL OR emprestimos.data_devolucao IS NOT NULL
                                 GROUP BY livros.id
                                 HAVING MAX(emprestimos.data_devolucao) IS NOT NULL OR MAX(emprestimos.id) IS NULL''').fetchall()

        if not result:
            print("\nNão há nenhum livro disponível.")
            return

        print("\n----------- Livros disponíveis -----------")
        for livro in result:
            id_livro, titulo, autor, editora, ano_publicacao, isbn = livro
            print(f"\nID: {id_livro}\nTítulo: {titulo}\nAutor: {autor}\nEditora: {editora}\nAno de Publicação: {ano_publicacao}\nISBN: {isbn}")
    except Exception as e:
        print(f"Erro ao exibir livros disponíveis: {e}")
    finally:
        conn.close()

# Exemplo de chamada da função.
# exibir_disponiveis()    
# Exemplo de funções.    
# cadastrar_livro("O Codificador Limpo", "Rober C. Martin", "Alta Books", 2009, "123456")
# cadastrar_usuario("Ésley", "Nathan", "Via B-9", "esleynathan@hotmail.com", "21990238348")
# cadastrar_emprestimo(1, 1, "31/05/2024", None)        
# devolver_emprestimo(1, "11/11/2011")
# connect()

# exibir_livros()
# exibir_usuarios()
# exibir_emprestimos()
