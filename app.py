#
#   Software Desenvolvido por https://github.com/guicomh
#


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import main
import web


def apagar():

    main.limpar_lixeira()
    main.limpar_pasta_temp()

def github():

    web.abrir_github()

janela = Tk()


imagem_fundo = Image.open("img/fundo.png")
imagem_fundo = imagem_fundo.resize((800, 600))
foto = ImageTk.PhotoImage(imagem_fundo)
background_label = Label(janela, image=foto)
background_label.image = foto
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

janela.resizable(False, False)
janela.geometry("800x600")
janela.title("Limpeza 2.0")

fonte = ("Helvetica", 30)

fonte_botao = ("Times New Roman", 15)




botao_apagar = Button(janela, text="Limpar", command=apagar, bg="white", fg="black", cursor="hand2", font=fonte_botao) 

botao_github = Button(janela, text="GitHub", command=github, bg="white", fg="black", cursor="hand2", font=fonte_botao) 

botao_sair = Button(janela, text="Sair", command=exit, bg="white", fg="black", cursor="hand2", font=fonte_botao) 

botao_apagar.place(relx=0.5, rely=0.4, anchor=CENTER)
botao_github.place(relx=0.5, rely=0.5, anchor=CENTER)
botao_sair.place(relx=0.5, rely=0.6, anchor=CENTER)

janela.mainloop()
