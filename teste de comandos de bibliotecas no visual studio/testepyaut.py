import pyautogui

print("Biblioteca PyAutoGUI instalada com sucesso!")

largura, altura = pyautogui.size()
print("Tamanho da tela:")
print("Largura:", largura)
print("Altura:", altura)

posicao = pyautogui.position()
print("Posição atual do mouse:")
print(posicao)
