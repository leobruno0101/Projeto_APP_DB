from tkinter import *

class Usuarios:
    def __init__(self,master=None):
        self.Modelofont = ("Arial", 15)
        self.widget1 = Frame(master).pack()
        self.Cabecalio = Label(self.widget1,text='Informe os dados',font=('Arial',25,'bold')).pack()

        self.widget2 = Frame(master)
        self.widget2.pack()
        self.IdCIDLabel = Label(self.widget2,text='IdCidade: ',font=self.Modelofont, width=15).pack(side=LEFT)
        self.IdCID = Entry(self.widget2,font=self.Modelofont, width=18).pack(side=LEFT)
        self.Buscar = Button(self.widget2,text='Buscar',font=self.Modelofont,width=10).pack(side=LEFT)

        self.widget3 = Frame(master)
        self.widget3.pack()
        self.Nomelabel = Label(self.widget3,text='Nome da Cidade: ',font=self.Modelofont,height=2).pack(side=LEFT)
        self.Nome = Entry(self.widget3,font=self.Modelofont,width=30).pack(side=LEFT)

        self.widget4 = Frame(master)
        self.widget4.pack()
        self.UFlabel = Label(self.widget4, text='Unidade Federativa: ', font=self.Modelofont).pack(side=LEFT)
        self.UF = Entry(self.widget4, font=self.Modelofont, width=28).pack(side=LEFT)

        self.widget5 = Frame(master)
        self.widget5.pack()
        self.CEPlabel = Label(self.widget5, text='CEP:', font=self.Modelofont,width=14,height=2).pack(side=LEFT)
        self.CEP = Entry(self.widget5, font=self.Modelofont, width=30).pack(side=LEFT)

        self.widget8 = Frame(master)
        self.widget8.pack()
        self.inserir = Button(self.widget8,text='Inserir',font=self.Modelofont,width=10).pack(side=LEFT)
        self.alterar = Button(self.widget8,text='Alterar',font=self.Modelofont,width=10).pack(side=LEFT)
        self.excluit = Button(self.widget8,text='Excluir',font=self.Modelofont,width=10).pack(side=LEFT)


root = Tk()
Usuarios(root)
root.state('zoomed')
root.title('Cadastro')
root.mainloop()