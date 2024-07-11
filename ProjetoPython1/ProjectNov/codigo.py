



import pyautogui
import time
pyautogui.PAUSE = 0.8

# Passo 1 - Entra no site da Empresa
# Entra no navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Entrando no sistema da empresa
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Passo 2 - Fazer login 
#Selecionado o campo E-mail.

pyautogui.click(x=803, y=473)

#pyautogui.press("tab")
pyautogui.hotkey("ctrl","a")
pyautogui.write("tiagodop001@gmail.com")
# Passando para o campo de SENHA
pyautogui.press("tab")
pyautogui.write("minhasenha")
#Clicando no botão de Logar
pyautogui.click(x=930, y=679)
#Carregamento de segurança da página
time.sleep(3)

# Passo 3 - Importa a Base de dados


import pandas

tabela = pandas.read_csv("ProjectNov/produtos.csv")

print(tabela)
# Passo 4 - Cadastrar produtos

for linha in tabela.index:
    # CódigoMOLO000251  marca   tipo    cate
    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.click(x=827, y=338)          

    pyautogui.write(codigo)

    # marca
    marca = str(tabela.loc[linha,"marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    #tipo
    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    #categoria
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    # preco_unitario
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)

    custo = str(tabela.loc[linha,"custo"])
    #custo
    pyautogui.press("tab")
    pyautogui.write(custo)

    #obs
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    # Se o obs for tive o valor diferente de NAN escreva
    if obs != "nan":
        pyautogui.write(obs)

    # Clica no botão de Enviar
    pyautogui.press("tab")
    pyautogui.press("enter")


    ## Volta para o inicio da tela do Formulário
    pyautogui.scroll(5000)

# Passo - 5 repetir o cadastramento para todos os protudos , Para todas as linhas da tabela.
