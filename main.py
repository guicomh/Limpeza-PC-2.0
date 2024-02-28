import os
import shutil

def limpar_pasta_temp():

    os.system("rd/s/q %temp%")
    os.system("rd /s /q C:\Windows\Temp")
    return 


def limpar_lixeira():

    os.system("rd /s /q Lixeira")
    return




