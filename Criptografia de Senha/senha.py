
# # Esperar alguns segundos para o usuário selecionar o campo de mensagem
# time.sleep(5)

# valor = "k"

# for i in range(0, 100):  # repetir 5 vezes, adicionando um k a mais a cada iteração
#     mensagem = f"{'k'*i}"
#     pyautogui.typewrite(mensagem + valor)
#     pyautogui.press("enter")

# # Pressionar a tecla Enter para enviar a mensagem
# pyautogui.press("enter")

# import time
# import pyautogui
# from cryptography.fernet import Fernet

# # Gerar uma chave de criptografia
# key = Fernet.generate_key()

# # Criar um objeto Fernet com a chave
# fernet = Fernet(key)

# # Mensagem a ser criptografada
# mensagem = input("Digite a mensagem a ser criptografada: ")

# # Criptografar a mensagem
# mensagem_cifrada = fernet.encrypt(mensagem.encode())

# # Esperar alguns segundos para o usuário selecionar o campo de mensagem
# time.sleep(5)

# # Digitar a mensagem criptografada na tela
# pyautogui.typewrite(mensagem_cifrada.decode())

# # Exibir a mensagem criptografada
# print(mensagem_cifrada)



import random
import string
import time
import pyautogui
import socket
import platform
import os
import pyperclip


# Obtendo informações sobre o sistema operacional e o nome do computador
uname = platform.uname()
computer_name = uname.node
os_name = uname.system
os_version = uname.version

# Obtém o endereço IP da máquina
ip_address = socket.gethostbyname(socket.gethostname())

# Converte o endereço IP em um número inteiro
seed = int(ip_address.replace('.', ''))

# Verifica se o arquivo com a seed já existe
if os.path.isfile("seed.txt"):
    # Se o arquivo existe, lê o valor da seed salvo nele
    with open("seed.txt", "r") as f:
        seed = int(f.readline())
else:
    # Se o arquivo não existe, cria um novo arquivo com o valor da seed
    with open("seed.txt", "w") as f:
        f.write(str(seed))

# Exibindo as informações no console
print("========================================================================================================================")
print("")
print("                                                      \033[34m NEXEUS TECHNOLOGY\033[0m")
print("")
print("========================================================================================================================")
print("========================================================================================================================")
print("")
print("                                \033[34mUSER:\033[0m", os.getlogin(), "| \033[34mCOMPUTERNAME:\033[0m", computer_name, "| \033[34mCURRENT OS:\033[0m", os_name, os_version)
print("")
print("========================================================================================================================")


def encrypt(message, seed):
    # Definindo a semente para a geração de números aleatórios
    random.seed(seed)
    
    # Gerando uma chave aleatória com 16 caracteres, incluindo letras e números
    key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

    encrypted = ''
    for i in range(len(message)):
        # Realizando a operação XOR entre o caractere da mensagem e da chave na mesma posição
        encrypted += chr(ord(message[i]) ^ ord(key[i % len(key)]))

    return encrypted, key


loopingInicio = True
while loopingInicio:
    print("")

    # Pedindo para o usuário digitar a mensagem a ser criptografada
    message = input("Digite a mensagem a ser criptografada: ")
    while True:
        tempo = input("Digite o tempo em segundos: ")
        if tempo.isdigit():
            break
        else:
            print("Valor inválido. Digite um número inteiro positivo.")



    # Criptografando a mensagem e recebendo a chave
    encrypted_message, key = encrypt(message, seed)
    
    # Esperar alguns segundos para o usuário selecionar o campo de mensagem
    time.sleep(int(tempo))

    # Digitar a mensagem criptografada usando o PyAutoGUI
    pyautogui.typewrite(encrypted_message)

    # copia a mensagem para a área de transferência
    pyperclip.copy(encrypted_message)

    # Exibindo a mensagem criptografada e a chave
    print("")
    print("Mensagem criptografada: ", encrypted_message)
    print("Chave: ", key)
    print("Seed: ", seed)    

    # Pedir ao usuário se ele deseja criar uma nova senha
    print()  # Limpar o buffer do teclado
    resposta = input("Deseja criar uma nova senha? (Sim/Não): ")
    if resposta.strip().lower() == "não" or resposta.strip().lower() == "nao":
        print("")
        print("Encerrando o programa...")
        for i in range(5, 0, -1):
            print("Encerrando em", i, "segundos...")
            time.sleep(1)
        break
    elif resposta.strip().lower() == "sim" or resposta.strip().lower() == "Sim":
        continue
    else:
        print("Resposta inválida. Por favor, digite 'Sim' ou 'Não'.")
        loopingFinal = True
        while loopingFinal:
            respostadois = input("Deseja criar uma nova senha? (Sim/Não): ")
            if respostadois.strip().lower() == "não" or respostadois.strip().lower() == "nao":
                print("")
                print("Encerrando o programa...")
                for i in range(5, 0, -1):
                    print("Encerrando em", i, "segundos...")
                    time.sleep(1)
                loopingFinal = False
                loopingInicio = False
                break
            elif respostadois.strip().lower() == "sim" or respostadois.strip().lower() == "Sim":
                loopingFinal = False
                continue
            else:
                print("Resposta inválida. Por favor, digite 'Sim' ou 'Não'.")
                loopingFinal = True

         
               

           




















