import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror

import os
import PyPDF2 as pdf
from glob import glob

def getDiretorioDestino():
    caminho = fd.askdirectory(title='Escolher local que o arquivo será salvo')
    return caminho
    
def select_files():
    filetypes = (
        ('PDFs', '*.pdf'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Escolher arquivos para Mesclar',
        filetypes=filetypes)
    
    return filenames   

def concatenaPdf():

    arquivos = select_files()
    
    caminho = getDiretorioDestino()
    os.chdir(caminho)
    
    nomeArquivo = inputNome.get()
    if(nomeArquivo==""):
        nomeArquivo = "NomeNaoInformado"
    destino = caminho + '\\' + nomeArquivo + '.pdf'

    #Cria o diretório de resultado, caso não exista
    if not os.path.exists(caminho):
        os.makedirs(r'.\\' + caminho)
        print('Diretório de destino criado\nProsseguindo...')
    else:
        print('Diretório de destino já existente\nProsseguindo...')

    try:
        #Abertura dos arquivos
        pdfWriter = pdf.PdfFileWriter()

        #Leitura de todos os arquivos do diretório
        for j in range(0, len(arquivos)):
            # rb Read Binary
            pdfDoc = open(arquivos[j], 'rb')

            pdfReader = pdf.PdfFileReader(pdfDoc)

            #Adiciona todas as páginas de cada arquivo
            for k in range(0, pdfReader.numPages):
                pagina = pdfReader.getPage(k)
                pdfWriter.addPage(pagina)

            pdfResultado = open(destino, 'ab')
            pdfWriter.write(pdfResultado)
            
            pdfDoc.close()
            pdfResultado.close()
            
    except Exception as exc:
        print('Administrador: verificar existência de exceções')
        showerror(
            title='FALHA',
            message=f'FALHA em:\n{os.getcwd()}\{destino}\nDetalhe do erro:\n{exc}'
        )
        pdfResultado.close()
        
        if os.path.exists(destino):
            os.remove(destino)
        else:
            print(destino + ' não encontrado')
        
        return str(exc)

    print(f'Arquivo gerado em:\n{os.getcwd()}\{destino}')
    showinfo(
        title='Sucesso',
        message=f'Arquivo gerado em:\n{os.getcwd()}\{destino}'
    )
    os.startfile(caminho)
    return f'Arquivo gerado em:\n{os.getcwd()}\{destino}'


# Criação da janela
root = tk.Tk()
root.title("Mesclar PDF") 
root.resizable(False, False)
root.geometry('400x200')

root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

root.iconbitmap('icone.ico')

texto = """
Aplicação para MESCLAR arquivos .pdf
Etapas:
1) Inserir o nome do arquivo no campo abaixo
2) Ao pressionar o botão, duas janelas serão exibidas:
    a. A primeira será para escolher quais arquivos serão mesclados
    b. A segunda será para escolher a pasta onde o arquivo será criado
"""

#Criação dos elemantos da interface 
label = Label(root, justify=tk.LEFT,text = texto)
label.grid(row=0,columnspan = 2)

labeNome = Label(root, text='Nome Arquivo Destino')
labeNome.grid(row=1,column=0, sticky = W, pady = 2)

inputNome = Entry(root)
inputNome.grid(row=1,column=1, sticky = W, pady = 2)

labelLinha = Label(root, text = "           ")
labelLinha.grid(row=2,columnspan = 2)

# Botão para escolher os arquivos
btMesclar = ttk.Button(
    root,
    text='Mesclar PDFs',
    command=concatenaPdf
)
btMesclar.grid(row=3,columnspan = 2)

root.mainloop()