import hashlib
import os
import phonenumbers
import random
import string
import time
from tkinter import *
from phonenumbers import geocoder


def verificar_ip():
    def ip():
        ip_host = vip.get()
        os.system(f" ping -n 4 {ip_host}")
        time.sleep(10)

    janela_5 = Tk()
    janela_5.title("Verificador de IP")
    janela_5.geometry("355x120")
    janela_5.configure(background="#F0F8FF")
    janela_5.maxsize(355, 120)
    janela_5.minsize(355, 120)

    Label(janela_5, text="Digite o IP ou Host a ser verificado:", anchor=W, background="#00BFFF",
          font="-weight bold -size 9").place(x=10, y=10, width=200, height=20)

    vip = Entry(janela_5, background="#C0C0C0")
    vip.place(x=10, y=40, width=150, height=20)

    Label(janela_5, text="EX: 192.168.15.1", anchor=W, background="#F0F8FF",
          font="-weight bold -size 7").place(x=170, y=41)

    Button(janela_5, text="Verificar", command=ip).place(x=10, y=65)

    Label(janela_5, text="OBS: Será aberto o Prompt de Comando rodando a verificação", background="#F0F8FF",
          font="-weight bold -size 8").place(x=5, y=95)
    janela_5.mainloop()


# Função e Segunda Interface Gráfica
def gerar_senha():
    def gerar():
        pegar_dado = vsenha.get()
        tamanho = int(pegar_dado)
        chars = string.ascii_letters + string.digits + '!@#$%&*-+=§^?/|\ç'
        rnd = random.SystemRandom()
        senha_aleatoria["text"] = "".join(rnd.choice(chars) for _ in range(tamanho))

    janela_2 = Tk()
    janela_2.title("Gerador de Senhas")
    janela_2.geometry("300x200")
    janela_2.configure(background="#F0F8FF")
    janela_2.maxsize(300, 200)
    janela_2.minsize(300, 200)

    Label(janela_2, text="Informe o tamanho da senha desejada:", anchor=W, background="#00BFFF",
          font="-weight bold -size 9").place(x=10, y=10, width=250, height=30)
    vsenha = Entry(janela_2, background="#C0C0C0")
    vsenha.place(x=10, y=40, width=30, height=20)

    Button(janela_2, text="Gerar", command=gerar).place(x=10, y=70, width=50, height=20)

    senha_aleatoria = Label(janela_2, text="")
    senha_aleatoria.place(x=10, y=100, width=80, height=20)

    janela_2.mainloop()


# Função e Terceira Interface Gráfica
def verifica_telefone():
    def verificar():
        tel = vtel.get()
        phone = phonenumbers.parse(tel)
        time.sleep(1)
        res_tel["text"] = "O número informado é de " + geocoder.description_for_number(phone, 'pt')

    janela_3 = Tk()
    janela_3.title("Verificador de Telefone")
    janela_3.geometry("300x200")
    janela_3.configure(background="#F0F8FF")
    janela_3.maxsize(300, 200)
    janela_3.minsize(300, 200)

    Label(janela_3, text="Informe o telefone a ser verificado:", anchor=W, background="#00BFFF",
          font="-weight bold -size 9").place(x=10, y=10, width=210, height=30)

    vtel = Entry(janela_3, background="#C0C0C0")
    vtel.place(x=10, y=40, width=110, height=20)

    Label(janela_3, text="Ex: +551140088922", background="#F0F8FF").place(x=120, y=40, height=20)

    Button(janela_3, text="Verificar", command=verificar).place(x=10, y=70, width=50, height=20)

    res_tel = Label(janela_3, text="")
    res_tel.place(x=10, y=90, width=250, height=30)

    janela_3.mainloop()


# Função e Quarta Interface Grafica
def gerador_hashes():
    c = os.path.dirname(__file__)
    name_arquive = c + "\\hashes.txt"

    def hash_md5():
        value = htext.get()
        resultado = hashlib.md5(value.encode('utf-8'))
        arquivo = open(name_arquive, "a")
        arquivo.write("\nMD5: %s" % resultado.hexdigest())
        arquivo.write("\n\n")

    def hash_sha1():
        value = htext.get()
        resultado = hashlib.sha1(value.encode('utf-8'))
        arquivo = open(name_arquive, "a")
        arquivo.write("\nSHA1: %s" % resultado.hexdigest())
        arquivo.write("\n\n")

    def hash_sha256():
        value = htext.get()
        resultado = hashlib.sha256(value.encode('utf-8'))
        arquivo = open(name_arquive, "a")
        arquivo.write("\nSHA256: %s" % resultado.hexdigest())
        arquivo.write("\n\n")

    def hash_sha512():
        value = htext.get()
        resultado = hashlib.sha512(value.encode('utf-8'))
        arquivo = open(name_arquive, "a")
        arquivo.write("\nSHA512: %s" % resultado.hexdigest())
        arquivo.write("\n\n")

    janela_4 = Tk()
    janela_4.title("Gerador de Hashes")
    janela_4.geometry("500x200")
    janela_4.configure(background="#F0F8FF")
    janela_4.maxsize(500, 200)
    janela_4.minsize(500, 200)

    Label(janela_4, text="Digite o texto para gerar a Hash:", anchor=W, background="#00BFFF",
          font="-weight bold -size 9").place(x=10, y=10)

    htext = Entry(janela_4, background="#C0C0C0")
    htext.place(x=200, y=10, width=200, height=22)

    md5 = Button(janela_4, text="MD5", command=hash_md5)
    md5.place(x=20, y=50, width=50, height=20)

    sha1 = Button(janela_4, text="SHA1", command=hash_sha1)
    sha1.place(x=20, y=90, width=50, height=20)

    sha256 = Button(janela_4, text="SHA256", command=hash_sha256)
    sha256.place(x=90, y=90, width=50, height=20)

    sha512 = Button(janela_4, text="SHA512", command=hash_sha512)
    sha512.place(x=90, y=50, width=50, height=20)

    Label(janela_4, text="OBS: Será criado um arquivo .txt com os códigos das Hashes no mesmo diretório \n que se "
                         "encontra o programa", anchor=W, font="-weight bold -size 9").place(x=5, y=150)

    janela_4.mainloop()


# Primeira Interface Gráfica
janela = Tk()
janela.geometry("240x300")
janela.title("System")
janela.config(padx=20, pady=10)
janela.configure(background="#A9A9A9")
janela.maxsize(240, 300)
janela.minsize(240, 300)

texto_apresentacao = Label(janela, text="Olá! Seja bem-vindo(a)", font="-weight bold")
texto_apresentacao.grid(column=0, row=0, padx=10, pady=5)

texto_orientacao = Label(janela, text="Escolha uma das opções abaixo:", font=" -size 7")
texto_orientacao.grid(column=0, row=1, padx=10, pady=5)

ip = Button(janela, text="Verificar IP (CMD)", command=verificar_ip, background="#FFD700")
ip.grid(column=0, row=2, padx=10, pady=5)

senha = Button(janela, text="Gerar Senha", command=gerar_senha, background="#FFD700")
senha.grid(column=0, row=3, padx=10, pady=5)

tel = Button(janela, text="Verificar Telefone", command=verifica_telefone, background="#FFD700")
tel.grid(column=0, row=4, padx=10, pady=5)

hashs = Button(janela, text="Gerar Hash", command=gerador_hashes, background="#FFD700")
hashs.grid(column=0, row=5, padx=10, pady=5)

janela.mainloop()
