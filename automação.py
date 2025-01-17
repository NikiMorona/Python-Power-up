# passo 1: abrir o sistema da empresa; 
# sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login; 
# passo 2: fazer login; 
# passo 3: importar a base de dados dos produtos; 
# passo 4: cadastrar um produto; 
# passo 5: repetir o passo 4 até acabar todos os produtos.

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

import pyautogui as pag

import time

pag.PAUSE = 0.3

pag.press("win")
pag.write("chrome")
pag.press("enter")
time.sleep(2)
pag.click(x=394, y=73)
pag.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pag.press("enter")

time.sleep(2)

pag.click(x=756, y=512)
pag.write("testenicole@gmail.com")
pag.press("tab")
pag.write("teste")
pag.press("enter")

import pandas as pd

tabela = pd.read_csv("produtos.csv") #aqui importamos a tabela de produtos.
print(tabela)

time.sleep(2)

for linha in tabela.index:
    pag.click(x=758, y=370)
    pag.write(str(tabela.loc[linha, "codigo"]))
    pag.press("tab")
    pag.write(str(tabela.loc[linha, "marca"]))
    pag.press("tab")
    pag.write(str(tabela.loc[linha, "tipo"]))
    pag.press("tab")
    pag.write(str(tabela.loc[linha, "categoria"]))
    pag.press("tab")
    pag.write(str(tabela.loc[linha, "preco_unitario"]))
    pag.press("tab")
    pag.write(str(tabela.loc[linha, "custo"]))
    pag.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs): #pd.isna localiza as informação e é mais seguro.
        pag.write(str(tabela.loc[linha, "obs"]))
    pag.press("tab")

    pag.press("enter")
    pag.scroll (5000)