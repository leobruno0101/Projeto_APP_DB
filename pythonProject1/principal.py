from tkinter import *
import subprocess

class principal:
    def __init__(self, master=None):
        self.caixa1 = Frame(master)
        self.caixa1.pack()
        self.Mensagem = Label(self.caixa1, text="Sistema",font=('Arial',30)).pack()
        self.Usuario = Button(self.caixa1, text='Usuarios', font=('Arial',15), command=self.entarUSU)
        self.Usuario.pack(side=LEFT)
        self.Cidades = Button(self.caixa1, text='Cidades', font=('Arial',15), command=self.entarCidades)
        self.Cidades.pack(side=LEFT)
        self.Clientes = Button(self.caixa1, text='Clientes', font=('Arial',15), command=self.entarClientes)
        self.Clientes.pack(side=LEFT)
        self.Fechar = Button(self.caixa1, text='Fechar', font=('Arial',15),command=self.caixa1.quit)
        self.Fechar.pack(side=LEFT)

    def entarUSU(self):
        subprocess.run({"python","CADUsuarios.py"})
    def entarCidades(self):
        subprocess.run({"python","CADCidade.py"})
    def entarClientes(self):
        subprocess.run({"python","CADclientes.py"})



root = Tk()
principal(root)
root.state('zoomed')
root.title("Menu Principal")
root.mainloop()