import os
import time
import pandas as pd

#caminho_arquivo = ".\\arquivo.txt"
caminho_arquivo = ".\\base_vendas.csv"

def detec_modifica():
    return os.path.getmtime(caminho_arquivo)

def resumo_vendas():
    df = pd.read_csv(caminho_arquivo)

    resumo = df[ ["desc_produto","valor_unt"] ].groupby(by="desc_produto").sum()

    print(resumo)

    resumo.to_csv("resumo_vendas.csv",sep=";")
    

ul_modificacao = detec_modifica()

while True:
    st_atual = detec_modifica()

    if ul_modificacao != st_atual:

        # Chamar funcao resumo_vendas
        resumo_vendas()

        print("Alteração detectada !")
        ul_modificacao = st_atual

    time.sleep(1)
    