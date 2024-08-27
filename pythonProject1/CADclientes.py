import tkinter as tk
from tkinter import *

from clientes import *

class CADclientes:
    def __init__(self,master=None):
        self.Modelofont = ("Arial", 15)
        # Frame principal
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.Cabecalio = Label(self.widget1, text='Informe os dados', font=('Arial', 25, 'bold'))
        self.Cabecalio.pack()

        # Frame para ID do cliente e botão de busca
        self.widget2 = Frame(master)
        self.widget2.pack()
        self.IdcliLabel = Label(self.widget2, text='IdCliente: ', font=self.Modelofont, width=15)
        self.IdcliLabel.pack(side=tk.LEFT)
        self.Idcli = Entry(self.widget2, font=self.Modelofont, width=18)
        self.Idcli.pack(side=tk.LEFT)
        self.Buscar = Button(self.widget2, text='Buscar', font=self.Modelofont, width=10, command=self.buscarcliente)
        self.Buscar.pack(side=tk.LEFT)

        # Frame para Nome
        self.widget3 = Frame(master)
        self.widget3.pack()
        self.Nomelabel = Label(self.widget3, text='Nome: ', font=self.Modelofont, height=2)
        self.Nomelabel.pack(side=tk.LEFT)
        self.Nome = Entry(self.widget3, font=self.Modelofont, width=30)
        self.Nome.pack(side=tk.LEFT)

        # Frame para Data de nascimento
        self.widget4 = Frame(master)
        self.widget4.pack()
        self.dataNascimentolabel = Label(self.widget4, text='Data de nascimento: ', font=self.Modelofont)
        self.dataNascimentolabel.pack(side=tk.LEFT)
        self.dataNascimento = Entry(self.widget4, font=self.Modelofont, width=27)
        self.dataNascimento.pack(side=tk.LEFT)

        # Frame para Gênero
        self.widget5 = Frame(master)
        self.widget5.pack()
        self.Generolabel = Label(self.widget5, text='Genero:', font=self.Modelofont, width=14, height=2)
        self.Generolabel.pack(side=tk.LEFT)
        self.Genero = Entry(self.widget5, font=self.Modelofont, width=30)
        self.Genero.pack(side=tk.LEFT)

        # Frame para CPF
        self.widget7 = Frame(master)
        self.widget7.pack()
        self.CPFlabel = Label(self.widget7, text='CPF:', font=self.Modelofont, width=14, height=2)
        self.CPFlabel.pack(side=tk.LEFT)
        self.CPF = Entry(self.widget7, font=self.Modelofont, width=30)
        self.CPF.pack(side=tk.LEFT)

        # Frame para Telefone
        self.widget6 = Frame(master)
        self.widget6.pack()
        self.telelabel = Label(self.widget6, text='Telefone:', font=self.Modelofont, width=14, height=2)
        self.telelabel.pack(side=tk.LEFT)
        self.tele = Entry(self.widget6, font=self.Modelofont, width=30)
        self.tele.pack(side=tk.LEFT)

        # Novo Frame para E-mail
        self.widget12 = Frame(master)
        self.widget12.pack()
        self.Emaillabel = Label(self.widget12, text='E-mail:', font=self.Modelofont, width=14, height=2)
        self.Emaillabel.pack(side=tk.LEFT)
        self.Email = Entry(self.widget12, font=self.Modelofont, width=30)
        self.Email.pack(side=tk.LEFT)

        # Frame para Endereço
        self.widget10 = Frame(master)
        self.widget10.pack()
        self.Enderocolabel = Label(self.widget10, text='Endereço:', font=self.Modelofont, width=14, height=2)
        self.Enderocolabel.pack(side=tk.LEFT)
        self.Enderoco = Entry(self.widget10, font=self.Modelofont, width=30)
        self.Enderoco.pack(side=tk.LEFT)

        # Frame para Cidade
        self.widget11 = Frame(master)
        self.widget11.pack()
        self.NomeCIDlabel = Label(self.widget11, text='Cidade:', font=self.Modelofont, width=14, height=2)
        self.NomeCIDlabel.pack(side=tk.LEFT)
        self.NomeCID = Entry(self.widget11, font=self.Modelofont, width=30)
        self.NomeCID.pack(side=tk.LEFT)

        # Frame para botões
        self.widget8 = Frame(master)
        self.widget8.pack()
        self.inserir = Button(self.widget8, text='Inserir', font=self.Modelofont, width=10, command=self.inserirCliente)
        self.inserir.pack(side=tk.LEFT)
        self.alterar = Button(self.widget8, text='Alterar', font=self.Modelofont, width=10, command=self.alterarCliente)
        self.alterar.pack(side=tk.LEFT)
        self.excluir = Button(self.widget8, text='Excluir', font=self.Modelofont, width=10, command=self.excluirCliente)
        self.excluir.pack(side=tk.LEFT)
        self.fechar = Button(self.widget8, text='Fechar', font=self.Modelofont, width=10, command=master.quit)
        self.fechar.pack(side=tk.LEFT)

        # Frame para mensagem
        self.widget9 = Frame(master)
        self.widget9.pack()
        self.msg = Label(self.widget9, text='', font=self.Modelofont)
        self.msg.pack()

    def buscarcliente(self):
        CLI = AplicacaoCLI()
        idclientes = self.Idcli.get()
        self.msg["text"] = CLI.selectclientes(idclientes)
        self.Idcli.delete(0, END)
        self.Idcli.insert(INSERT, CLI.idclientes)
        self.Nome.delete(0, END)
        self.Nome.insert(INSERT, CLI.nome)
        self.dataNascimento.delete(0, END)
        self.dataNascimento.insert(INSERT, CLI.dataNascimento)
        self.Genero.delete(0, END)
        self.Genero.insert(INSERT, CLI.genero)
        self.CPF.delete(0, END)
        self.CPF.insert(INSERT, CLI.CPF)
        self.tele.delete(0, END)
        self.tele.insert(INSERT,CLI.telefone)
        self.Email.delete(0, END)
        self.Email.insert(INSERT,CLI.Email)
        self.Enderoco.delete(0, CLI.endereco)
        self.Enderoco.insert(INSERT, CLI.endereco)
        self.NomeCID.delete(0, END)
        self.NomeCID.insert(INSERT,CLI.NomeCID)

    def inserirCliente(self):
        CLI = AplicacaoCLI()
        CLI.nome = self.Nome.get()
        CLI.dataNascimento = self.dataNascimento.get()
        CLI.genero = self.Genero.get()
        CLI.CPF = self.CPF.get()
        CLI.telefone = self.tele.get()
        CLI.Email = self.Email.get()
        CLI.endereco = self.Enderoco.get()
        CLI.NomeCID = self.NomeCID.get()
        self.msg["text"] = CLI.inserirclientes()
        self.Nome.delete(0, END)
        self.dataNascimento.delete(0, END)
        self.Genero.delete(0, END)
        self.CPF.delete(0,END)
        self.tele.delete(0, END)
        self.Email.delete(0, END)
        self.Enderoco.delete(0,END)
        self.NomeCID.delete(0, END)

    def alterarCliente(self):
        CLI = AplicacaoCLI()
        CLI.idclientes = self.Idcli.get()
        CLI.nome = self.Nome.get()
        CLI.dataNascimento = self.dataNascimento.get()
        CLI.genero = self.Genero.get()
        CLI.CPF = self.CPF.get()
        CLI.telefone = self.tele.get()
        CLI.Email = self.Email.get()
        CLI.endereco = self.Enderoco.get()
        CLI.NomeCID = self.NomeCID.get()
        self.msg["text"] = CLI.updateclientes()
        self.Nome.delete(0, END)
        self.dataNascimento.delete(0, END)
        self.Genero.delete(0, END)
        self.CPF.delete(0,END)
        self.tele.delete(0, END)
        self.Email.delete(0, END)
        self.Enderoco.delete(0,END)
        self.NomeCID.delete(0, END)

    def excluirCliente(self):
        CLI = AplicacaoCLI()
        CLI.idclientes = self.Idcli.get()
        self.msg["text"] = CLI.deleteclientes()
        self.Nome.delete(0, END)
        self.dataNascimento.delete(0, END)
        self.Genero.delete(0, END)
        self.CPF.delete(0,END)
        self.tele.delete(0, END)
        self.Email.delete(0, END)
        self.Enderoco.delete(0,END)
        self.NomeCID.delete(0, END)


root = Tk()
CADclientes(root)
root.state('zoomed')
root.title('Cadastro')
root.mainloop()