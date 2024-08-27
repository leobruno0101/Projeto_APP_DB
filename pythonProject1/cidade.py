from Banco import BancoCID

class AplicacaoCID:
    def __init__(self, idcidade=0, nome="", UF="", CEP=""):
        self.idcidade = idcidade
        self.nome = nome
        self.UF = UF
        self.CEP = CEP

    def insertcidade(self):
        banco = BancoCID()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO tbl_cidade (nome, UF, CEP) VALUES (?, ?, ?)",
                      (self.nome, self.UF, self.CEP))
            banco.conexao.commit()
            c.close()
            return "Cidade cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção da cidade: {str(e)}"

    def updatecidade(self):
        banco = BancoCID()
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE tbl_cidade SET nome = ?, UF = ?, CEP = ? WHERE idcidade = ?",
                      (self.nome, self.UF, self.CEP, self.idcidade))
            banco.conexao.commit()
            c.close()
            return "Cidade atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração da cidade: {str(e)}"

    def deletecidade(self):
        banco = BancoCID()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM tbl_cidade WHERE idcidade = ?", (self.idcidade,))
            banco.conexao.commit()
            c.close()
            return "Cidade excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão da cidade: {str(e)}"

    def selectcidade(self, idcidade):
        banco = BancoCID()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_cidade WHERE idcidade = ?", (self.idcidade,))
            linha = c.fetchone()
            if linha:
                self.idcidade, self.nome, self.UF, self.CEP = linha
            c.close()
            return "Busca feita com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na busca da cidade: {str(e)}"
