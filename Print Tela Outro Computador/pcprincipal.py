import socket
from PIL import Image

# Porta do servidor que receberá a imagem
porta = 8000

# Cria um objeto socket e aguarda por conexões
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('0.0.0.0', porta))
servidor.listen(1)

while True:
    # Aguarda por uma conexão
    conexao, endereco = servidor.accept()
    
    imagem = b''
    while True:
        parte = conexao.recv(1024)
        if not parte:
            break
        imagem += parte

    
    # Salva a imagem em um arquivo temporário
    with open("screenshot_temp.png", "wb") as arquivo:
        arquivo.write(imagem)
    
    # Abre a imagem no visualizador de imagens padrão do sistema operacional
    imagem = Image.open("screenshot_temp.png")
    imagem.show()
    
    # Pergunta ao usuário se ele deseja continuar a receber imagens
    continuar = input("Deseja continuar recebendo imagens? (s/n): ")
    if continuar.lower() == "n":
        break
    
    # Fecha a conexão com o cliente
    conexao.close()
