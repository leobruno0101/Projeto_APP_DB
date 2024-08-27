import sqlite3

class BancoUSU:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS tbl_usuarios (
                    idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    telefone TEXT,
                    email TEXT,
                    usuario TEXT,
                    senha TEXT)""")
        self.conexao.commit()
        c.close()

class BancoCID:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS tbl_cidade(
                            idcidade INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT,
                            UF TEXT,
                            CEP TEXT)""")
        self.conexao.commit()
        c.close()

class BancoCLI:
    def __init__(self):
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS tbl_clientes(
                    idclientes INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    dataNascimento TEXT,
                    genero TEXT,
                    CPF TEXT,
                    telefone TEXT,
                    Email,
                    endereco TEXT,
                    NomeCID TEXT,
                    CONSTRAINT fk_NomeCID FOREIGN KEY (nome) REFERENCES tbl_cidade(nome)""")
        self.conexao.commit()
        c.close()

