#
#   Software Desenvolvido por https://github.com/guicomh
#


from tkinter import *
from tkinter import ttk
import main
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle


def apagar():

    main.limpar_pasta()
    main.limpar_pasta_temp()

janela = Tk()

style = ThemedStyle(root)
style.set_theme("equilux")

janela.resizable(False, False)
janela.geometry("800x600")
janela.title("Limpeza 2.0")

botao_apagar = Button(janela, text="Limpar", command=apagar) . pack()


janela.mainloop()
