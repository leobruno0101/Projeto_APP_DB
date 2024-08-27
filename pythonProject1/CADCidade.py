from tkinter import *

from cidade import *

class CADcidade:
    def __init__(self,master=None):
        self.Modelofont = ("Arial", 15)
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.Cabecalio = Label(self.widget1,text='Informe os dados',font=('Arial',25,'bold'))
        self.Cabecalio.pack()

        self.widget2 = Frame(master)
        self.widget2.pack()
        self.IdCIDLabel = Label(self.widget2,text='IdCidade: ',font=self.Modelofont, width=15)
        self.IdCIDLabel.pack(side=LEFT)
        self.IdCID = Entry(self.widget2,font=self.Modelofont, width=18)
        self.IdCID.pack(side=LEFT)
        self.Buscar = Button(self.widget2,text='Buscar',font=self.Modelofont,width=10, command=self.buscarcidade)
        self.Buscar.pack(side=LEFT)

        self.widget3 = Frame(master)
        self.widget3.pack()
        self.Nomelabel = Label(self.widget3,text='Nome da Cidade: ',font=self.Modelofont,height=2)
        self.Nomelabel.pack(side=LEFT)
        self.Nome = Entry(self.widget3,font=self.Modelofont,width=30)
        self.Nome.pack(side=LEFT)

        self.widget4 = Frame(master)
        self.widget4.pack()
        self.UFlabel = Label(self.widget4, text='Unidade Federativa: ', font=self.Modelofont)
        self.UFlabel.pack(side=LEFT)
        self.UF = Entry(self.widget4, font=self.Modelofont, width=28)
        self.UF.pack(side=LEFT)

        self.widget5 = Frame(master)
        self.widget5.pack()
        self.CEPlabel = Label(self.widget5, text='CEP:', font=self.Modelofont,width=14,height=2)
        self.CEPlabel.pack(side=LEFT)
        self.CEP = Entry(self.widget5, font=self.Modelofont, width=30)
        self.CEP.pack(side=LEFT)

        self.widget8 = Frame(master)
        self.widget8.pack()
        self.inserir = Button(self.widget8,text='Inserir',font=self.Modelofont,width=10, command=self.inserirCidade)
        self.inserir.pack(side=LEFT)
        self.alterar = Button(self.widget8,text='Alterar',font=self.Modelofont,width=10, command=self.alterarCidade)
        self.alterar.pack(side=LEFT)
        self.excluir = Button(self.widget8,text='Excluir',font=self.Modelofont,width=10, command=self.excluirCidade)
        self.excluir.pack(side=LEFT)
        self.fechar = Button(self.widget8, text='Fechar', font=self.Modelofont, width=10,command=self.widget8.quit).pack()

        self.widget9 = Frame(master)
        self.widget9.pack()
        self.msg = Label(self.widget9, text='', font=self.Modelofont)
        self.msg.pack()

    def buscarcidade(self):
        CID = AplicacaoCID()
        idcidade = self.IdCID.get()
        self.msg["text"] = CID.selectcidade(idcidade)
        print(self.msg["text"])
        self.IdCID.delete(0, END)
        self.IdCID.insert(INSERT, CID.idcidade)
        self.Nome.delete(0, END)
        self.Nome.insert(INSERT, CID.nome)
        self.UF.delete(0, END)
        self.UF.insert(INSERT, CID.UF)
        self.CEP.delete(0, END)
        self.CEP.insert(INSERT, CID.CEP)

    def inserirCidade(self):
        CID = AplicacaoCID()
        CID.nome = self.Nome.get()
        CID.UF = self.UF.get()
        CID.CEP = self.CEP.get()
        self.msg["text"] = CID.insertcidade()
        self.Nome.delete(0, END)
        self.UF.delete(0, END)
        self.CEP.delete(0, END)


    def alterarCidade(self):
        CID = AplicacaoCID()
        CID.idcidade = self.IdCID.get()
        CID.nome = self.Nome.get()
        CID.UF = self.UF.get()
        CID.CEP = self.CEP.get()
        self.msg["text"] = CID.updatecidade()
        self.Nome.delete(0, END)
        self.UF.delete(0, END)
        self.CEP.delete(0, END)

    def excluirCidade(self):
        CID = AplicacaoCID()
        CID.idcidade = self.IdCID.get()
        self.msg["text"] = CID.deletecidade()
        self.Nome.delete(0, END)
        self.UF.delete(0, END)
        self.CEP.delete(0, END)


root = Tk()
CADcidade(root)
root.state('zoomed')
root.title('Cadastro')
root.mainloop()