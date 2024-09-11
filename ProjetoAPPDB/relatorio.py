import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF
from tkinter import ttk
from Banco import Banco
import os


class relatorio:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Relatorio")

        self.janela1 = tk.Frame(master)
        self.janela1.pack()
        self.titulo =tk.Label(self.janela1, text="Título do Relatório")
        self.titulo.pack()
        # Rótulos e campos de entrada
        self.titulo_entry = tk.Entry(self.janela1,width=20)
        self.titulo_entry.pack()

        self.janela2 = tk.Frame(master)
        self.janela2.pack()
        self.arquivos_label = tk.Label(self.janela2, text="arquivos:")
        self.arquivos_label.pack()
        self.arquivos_combobox = ttk.Combobox(self.janela2, width=27, values=["Usuarios","Cidades","Clientes"])
        self.arquivos_combobox.pack()
        self.buscar = tk.Button(self.janela2,text='Buscar', command=self.Buscar)
        self.buscar.pack()

        self.janela3 = tk.Frame(master)
        self.janela3.pack()
        self.texto = tk.Label(self.janela3, text="Conteúdo do Relatório")
        self.texto.pack()
        self.conteudo_text = tk.Text(self.janela3, height=20, width=90,)
        self.conteudo_text.pack()

        self.janela4 = tk.Frame(master)
        self.janela4.pack()
        self.gerar_btn = tk.Button(self.janela4, text="Gerar PDF", command=self.gerar_pdf)
        self.gerar_btn.pack(pady=10, side=tk.LEFT)
        self.sair_btn = tk.Button(self.janela4, text="Voltar", command=self.voltarmenu)
        self.sair_btn.pack(side=tk.LEFT)

        self.janela5 = tk.Frame(master)
        self.janela5.pack()
        self.PDF_combobox = ttk.Combobox(self.janela5, width=27)
        self.PDF_combobox.pack()
        self.LerAquivoPDF()
        self.VisuPDF = tk.Button(self.janela5, text="Abrir", command=self.visualizar_PDF)
        self.VisuPDF.pack()


    def Buscar(self):
        tipo = self.arquivos_combobox.get()
        if tipo == 'Usuarios':
            banco = Banco()
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_usuarios")
            lista = c.fetchall()
            self.conteudo_text.delete(1.0, tk.END)
            for i in lista:
                self.conteudo_text.insert(tk.INSERT, f'ID: {i[0]}, Nome: {i[1]}, Telefone: {i[2]}, Email: {i[3]}, Usuario: {i[4]}\n')
        elif tipo == 'Cidades':
            banco = Banco()
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_cidades")
            lista = c.fetchall()
            self.conteudo_text.delete(1.0, tk.END)
            for i in lista:
                self.conteudo_text.insert(tk.INSERT, f'ID: {i[0]}, Nome: {i[1]}, UF: {i[2]}\n')
        else:
            banco = Banco()
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_clientes")
            lista = c.fetchall()
            self.conteudo_text.delete(1.0, tk.END)
            for i in lista:
                self.conteudo_text.insert(tk.INSERT, f'ID: {i[0]}, Nome: {i[1]}, Cidade: {i[2]}, Nascimento: {i[3]}, CPF: {i[4]}, Gênero: {i[5]}\n')



    def gerar_pdf(self):
        # Coletar o texto do campo de entrada
        titulo = self.titulo_entry.get()
        conteudo = self.conteudo_text.get("1.0", "end-1c")  # Pega o conteúdo do Text widget

        # Criar o objeto PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Adicionar título
        pdf.cell(200, 10, txt=titulo, ln=True, align='C')

        # Adicionar conteúdo
        pdf.ln(10)  # Pular uma linha
        pdf.multi_cell(0, 10, conteudo)

        # Salvar arquivo PDF
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                 filetypes=[("PDF files", "*.pdf")])
        if file_path:
            pdf.output(file_path)
            messagebox.showinfo("Sucesso", "Relatório salvo com sucesso!")

    def LerAquivoPDF(self):
        path = 'Relatorios_salvos'
        dirs = os.listdir(path)
        self.PDF_combobox['values'] = dirs

    def visualizar_PDF(self):
        dirs = self.PDF_combobox.get()
        os.startfile(f'Relatorios_salvos\\{dirs}')

    def voltarmenu(self):
        self.master.destroy()


# Abre o arquivo pdf
# lembre-se que para o windows você deve usar essa barra -> /
# lembre-se também que você precisa colocar o caminho absoluto




