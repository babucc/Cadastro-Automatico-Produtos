# 1 - Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
    
import pyautogui
import time

pyautogui.PAUSE = 1

#pyautogui.click -> clicar em algum lugar da tela
#pyautogui.write -> escrever um texto
#pyautogui.press -> pressionar uma tecla do teclado

# Abrindo o navegador
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")

# Dá uma pausa em um local e momento específico
time.sleep(8) 


link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write (link)
pyautogui.press("enter")

# 2 - Fazer login

# Para clicar em Login
time.sleep(8)
pyautogui.click(x=267, y=401)
pyautogui.write('python@hotmail.com')

# Tab para passar do Login pra senha
pyautogui.press("tab")
pyautogui.write('python')

# Clicar no botão para logar
pyautogui.click(x=481, y=559) # Ou colocar o tab no lugar das coordenadas
time.sleep(3)

# 3 - Importar a base de dados

import pandas # Biblioteca que lê um documento 
tabela = pandas.read_csv('produtos.csv')
print(tabela)

# 4 - Cadastrar 1 produto

# Para cada linha da minha tabela
time.sleep(5)
for linha in tabela.index:
    # Clicar no primeiro campo
    pyautogui.click(x=328, y=272)
    # Código do produto
    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')
    # Marca
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    # Tipo
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    # Categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    # Preço
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    # Custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    # Código do OBS
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(tabela.loc[linha, 'obs'])
    pyautogui.press('tab')
    # Enviar
    pyautogui.press('enter')
    pyautogui.scroll(5000)
# 5 - Repetir o processo de cadastro até acabar