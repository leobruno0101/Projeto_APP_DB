from Banco import BancoCLI

class AplicacaoCLI:
    def __init__(self, idclientes=0, nome="", dataNascimento="", genero="", CPF="", telefone="", Email="", endereco="",NomeCID = "" ):
        self.idclientes = idclientes
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.genero = genero
        self.CPF = CPF
        self.telefone = telefone
        self.Email = Email
        self.endereco = endereco
        self.NomeCID = NomeCID

    def inserirclientes(self):
        banco = BancoCLI()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO tbl_clientes (nome, dataNacimento, genero,CPF,telefone,Email,endereco,NomeCID) VALUES (?,?,?,?,?,?,?,?)",
                      (self.nome, self.dataNascimento, self.genero, self.CPF, self.telefone, self.Email, self.endereco, self.NomeCID))
            banco.conexao.commit()
            c.close()
            return "Cliente cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção do cliente: {str(e)}"

    def updateclientes(self):
        banco = BancoCLI()
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE tbl_clientes SET nome = ?, dataNacimento = ?, genero = ?, CPF = ?, telefone = ?, Email = ?, endereco = ?, NomeCID = ? WHERE idclientes = ?",
                      (self.nome, self.dataNascimento, self.genero, self.CPF, self.telefone, self.Email, self.endereco, self.NomeCID))
            banco.conexao.commit()
            c.close()
            return "Cliente atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do cliente: {str(e)}"

    def deleteclientes(self):
        banco = BancoCLI()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM tbl_clientes WHERE idclientes = ?", (self.idclientes,))
            banco.conexao.comit()
            c.close()
            return "Cliente deletado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do cliente: {str(e)}"

    def selectclientes(self):
        banco = BancoCLI()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_clientes WHERE idclientes = ?", (self.idclientes))
            linha = c.fetchone()
            if linha:
                self.idclientes, self.nome, self.dataNascimento, self.genero, self.CPF, self.telefone, self.Email, self.endereco, self.NomeCID = linha
            c.close()
            return "Busca feita com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na busca do cliente: {str(e)}"