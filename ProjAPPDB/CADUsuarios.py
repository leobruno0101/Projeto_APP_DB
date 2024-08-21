from tkinter import *

class Usuarios:
    def __init__(self,master=None):
        self.Modelofont = ("Arial", 15)
        self.widget1 = Frame(master).pack()
        self.Cabecalio = Label(self.widget1,text='Informe os dados',font=('Arial',25,'bold')).pack()

        self.widget2 = Frame(master)
        self.widget2.pack()
        self.IdUsuLabel = Label(self.widget2,text='IdUsuário: ',font=self.Modelofont).pack(side=LEFT)
        self.IdUsu = Entry(self.widget2,font=self.Modelofont, width=16).pack(side=LEFT)
        self.Buscar = Button(self.widget2,text='Buscar',font=self.Modelofont,width=10).pack(side=LEFT)

        self.widget3 = Frame(master)
        self.widget3.pack()
        self.Nomelabel = Label(self.widget3,text='Nome: ',font=self.Modelofont).pack(side=LEFT)
        self.Nome = Entry(self.widget3,font=self.Modelofont,width=30).pack(side=LEFT)

        self.widget4 = Frame(master)
        self.widget4.pack()
        self.Telelabel = Label(self.widget4, text='Telefone: ', font=self.Modelofont).pack(side=LEFT)
        self.Tele = Entry(self.widget4, font=self.Modelofont, width=28).pack(side=LEFT)

        self.widget5 = Frame(master)
        self.widget5.pack()
        self.Emaillabel = Label(self.widget5, text='E-mail: ', font=self.Modelofont).pack(side=LEFT)
        self.Email = Entry(self.widget5, font=self.Modelofont, width=30).pack(side=LEFT)

        self.widget6 = Frame(master)
        self.widget6.pack()
        self.Usuariolabel = Label(self.widget6, text='Usuário: ', font=self.Modelofont).pack(side=LEFT)
        self.Usuario = Entry(self.widget6, font=self.Modelofont, width=29).pack(side=LEFT)

        self.widget7 = Frame(master)
        self.widget7.pack()
        self.senhalabel = Label(self.widget7, text='Senha: ', font=self.Modelofont).pack(side=LEFT)
        self.senha = Entry(self.widget7, font=self.Modelofont, width=30,show='*').pack(side=LEFT)

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