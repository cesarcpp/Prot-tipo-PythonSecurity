import random, phonenumbers, os, time, socket, sys, string, hashlib
from phonenumbers import geocoder
from tkinter import *

booleano = False
loop = True

print("Ferramentos de Segurança\n")

print("Boa tarde, bem vindo ao App!")
name = input("Qual o seu nome? => ")
print(f"Seja bem vindo {name}, escolha sua ferramenta")
while booleano == False:
    choose = int(input('''
                            [1] Verificador de Ip
                            [2] Gerador de Senhas
                            [3] Verificador de Telefone
                            [4] Gerador de Hashes

                            Escolha: '''))

    if choose == 1:
        print('-' * 60)
        ip_host = input("Digite o IP ou Host a ser verificado: ")
        time.sleep(2)
        os.system(f' ping -n 4 {ip_host} ')
        print('-' * 60)
    elif choose == 2:
        print('-' * 60)
        tamanho = int(input("Esolha o tamanho da senha que será gerada: "))
        chars = string.ascii_letters + string.digits + '!@#$%&*-+=§^?/|\ç'
        rnd = random.SystemRandom()
        print(''.join(rnd.choice(chars) for i in range (tamanho)))
        time.sleep(2)
        print('-' * 60)
    elif choose == 3:
        print('-' * 60)
        phone_number = input('Digite o telefone no seguinte formato (+551140028922): ')
        phone = phonenumbers.parse(phone_number)
        time.sleep(1)
        print(geocoder.description_for_number(phone, 'pt'))
        print('-' * 60)
    elif choose == 4:
        
        while loop == True: 
            print('-' * 60)
            string = input("Digite o texto a ser gerado a Hash: ")
            menu = int(input(''' #MENU - ESCOLHA O TIPO DE HASH #
                                       [1] md5
                                       [2] Sha1
                                       [3] Sha256
                                       [4] Sha512
                                       
                                       Digite o número do hash a ser gerado: '''))
            time.sleep(2)
            if menu == 1:
                resultado = hashlib.md5(string.encode('utf-8')) 
                print("O Hash da string por MD5 é: ", resultado.hexdigest())
                loop = False
            elif menu == 2:
                resultado = hashlib.sha1(string.encode('utf-8')) 
                print("O Hash da string por SHA1 é: ", resultado.hexdigest())
                loop = False
            elif menu == 3:
                resultado = hashlib.sha256(string.encode('utf-8')) 
                print("O Hash da string por SHA256 é: ", resultado.hexdigest())
                loop = False
            elif menu == 4:
                resultado = hashlib.sha512(string.encode('utf-8')) 
                print("O Hash da string por SHA256 é: ", resultado.hexdigest())
                loop = False
            else:
                print("Ocorreu um erro, tente novamente")
            print('-' * 60)

    decision = input("Deseja voltar para o menu principal ? (S/N) => ")

    if decision == 'S' or decision == 's':
        booleano = False
        print("Voltando ao menu...")
        time.sleep(2)
    elif decision == 'N' or decision == 'n':
        booleano = True
        print("Encerrando o Programa...")
        time.sleep(2)
    else:
        booleano = True
        print("Um erro ocorreu! O programa será encerrado...")
        time.sleep(1)


    
    
    
                        
