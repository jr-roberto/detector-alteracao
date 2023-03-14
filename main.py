import os
import time

caminho_arquivo = ".\\arquivo.txt"

def detec_modifica():
    return os.path.getmtime(caminho_arquivo)

ul_modificacao = detec_modifica()

while True:
    st_atual = detec_modifica()

    if ul_modificacao != st_atual:
        print("Alteração detectada !")
        ul_modificacao = st_atual

    time.sleep(1)
    