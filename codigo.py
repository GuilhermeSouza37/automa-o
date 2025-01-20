#1 - Entrar no sistema 
#2 - Fazer Login
#3 - importar banco de dados
#4 - Cadastrar Produtos
#5 - Repetir processo de cadastro

import pyautogui
import time

#pyautogui.click -> clicar com o mouse
#pyautogui.write -> escrever um texto
#pyautogui.press -> apertar 1 tecla
#pyautogui.hotkey -> atalho (combinação de teclas)

pyautogui.PAUSE = 0.5


#Abrir Chrome
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

#entrar no link
link =  "http://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#esperar loading do site
time.sleep(5)

#1 - Fazer LoginProduto Preco   Custo   
pyautogui.click(x=760, y=487)
pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.press("tab") # passar para o campo de senha
pyautogui.write("sua senha aqui")

pyautogui.press("tab") # passar para dar enter
pyautogui.press("enter") 

time.sleep(3)
#2 - Importar o banco de dados  OBS 
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    #3 - Cadastrar 1 produto
    pyautogui.click(x=721, y=370)

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]

    #preencher os campos
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(marca)
    pyautogui.press("tab")
    pyautogui.write(tipo)
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco)) 
    pyautogui.press("tab")
    pyautogui.write(str(custo)) 
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
   
    #Enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    #Voltar ao topo
    pyautogui.scroll(50000)


#4 - Repetir o cadastro para todos os produtos

