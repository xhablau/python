import socket
from PIL import ImageGrab

# IP do computador que receberá a imagem
ip_destino = '192.168.200.150'

# Porta do servidor que receberá a imagem
porta = 8000

# Captura a tela inteira
screenshot = ImageGrab.grab()

# Salva a captura de tela em um arquivo temporário
screenshot.save("screenshot_temp.png")

# Lê a imagem do arquivo temporário
with open("screenshot_temp.png", "rb") as arquivo:
    imagem = arquivo.read()

# Cria um objeto socket e conecta ao servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((ip_destino, porta))

# Envia a imagem para o servidor
cliente.sendall(imagem)

# Fecha a conexão com o servidor
cliente.close()
