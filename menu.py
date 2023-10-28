import os
from algoritmos import rc4_encript, rc4_decript, cesar_encript, cesar_decript

texto = ""

def menu_desencriptar():
    global texto 
    acao = 1
    while True:

        print('descriptografando')

        print('1-cifra de cesar')
        print('2-rc4')
        print('0-sair')
        acao = int(input())
        os.system("clear")
        if acao == 0:
            break

        key = input("digite sua chave de criptografia:  ")
        os.system("clear")

        if acao == 1:
            texto = cesar_decript(texto,int(key))
            print("seu texto descriptografado: \n", texto, "\n")
            return

        elif acao == 2:
            texto = rc4_decript(texto, key)
            print("seu texto descriptografado: \n", texto, "\n")
            return

def menu_encriptar():
    global texto
    acao = 1
    while True:

        print('encriptando')

        print('1-cifra de cesar')
        print('2-rc4')
        print('0-sair')

        acao = int(input())
        os.system("clear")
        if acao == 0:
            break

        key = input("digite sua chave de criptografia: ") 
        os.system("clear")

        if acao == 1:
            texto = cesar_encript(texto,int(key))
            print("seu texto criptografado: \n", texto, "\n")
            return


        elif acao == 2:
            texto = rc4_encript(texto, key)
            print("seu texto criptografado: \n", texto, "\n")
            return

def menu_principal():
    acao = 1
    global texto
    texto = input("Coloque o seu texto a ser trabalho ")
    os.system("clear")

    while acao>0:

        print('1-cripitografar')
        print('2-descriptografar')
        print('0-sair')

        acao = int(input())
        os.system("clear")

        if acao == 1:
            menu_encriptar()

        elif acao == 2:
            menu_desencriptar()

menu_principal()

