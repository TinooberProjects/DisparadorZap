
#zona de imports
import tkinter as tk
from tkinter.constants import DISABLED
from typing import Text

import tkinter.filedialog
from tkinter import messagebox


#bibliteca para importar e manipular as tabelas
import pandas as pd

#modificações selenium 15-12-2021 atualiazado  através do site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
# import webdriver
from selenium import webdriver

#bibliotecas para controlar o tempo e configuração de url
import time
import urllib







#instanciando a janela principal
janela=tk.Tk()


#icone da janela

janela.tk.call("wm","iconphoto",janela._w,tk.PhotoImage(file="/media/ton/bck_full/docs/professional/myprograms/Automatização_zap/Versao_teste/logo.png"))

#título da janela
janela.title("Disparador WhatsApp")
janela.geometry("300x150")
janela.config(bg="white")
janela.resizable(False,False)


############################################## Funções ###########################################################################
def conectar_celular():
    messagebox.showinfo("<<< Conectar Celular >>>","1-Abra o WhatsApp\n2-Clique nos 3 pont. à direita\n3-Aparelhos conectados")
    
def mostrar_manual():

     messagebox.showinfo("Disparador de Mensagens Zap","Em Construção!")


 

  

def mostrar_sobre():
    messagebox.showinfo("Sobre Disparador Zap","Disparador Zap\n\nVERSÂO 1.0!\n\nDisparador automatizado de mensagens\nEverton Santos\nevertonsantos@tinoober.com")

    
   

###################### Enviar MSG PARA CLIENTES ##################
def enviar_msg():

  #  print("Enviar Mensagens")
    #Janela de busca do arquivo fonte

    messagebox.showinfo("INFO","1-Abra a base de dados\n2-Aguarde o carregamento do Navegador")
    


    arquivo = tkinter.filedialog.askopenfilename(title="Selecione o arquivo XLS")


    


    #importando os contatos da planilha de nome Enviar.xlsx
    #contatos_df = pd.read_excel("Enviar.xlsx")
    contatos_df = pd.read_excel(arquivo,sheet_name="Lista")

    #descomentar o print, se queiser fazer o debug dos nomes que foram importados
    #print(contatos_df)


    #abrindo o navegador
    navegador = webdriver.Firefox( )

    #acessando o site do whatapp
    navegador.get("https://web.whatsapp.com/")

    while len(navegador.find_elements(By.NAME,"rememberMe"))<1:
        time.sleep(1)
    #nao permite que o relembre-me fique ativo
    navegador.find_element(By.NAME,"rememberMe").click()
    




    #verificador de que a página carregou
    #lógica: caso o navegador no encontre um elemento com id Side, aguarde um segundo

    while len(navegador.find_elements(By.ID, "side")) < 1: 
        
        time.sleep(1)


    #chamando página oculta



    # já estamos com o login feito no whatsapp web
    for i, mensagem in enumerate(contatos_df['Mensagem']):
        pessoa = contatos_df.loc[i, "Pessoa"]
        numero = contatos_df.loc[i, "Número"]
        #etapa que espera carregar a tela de msgs
        texto = urllib.parse.quote(f"{mensagem.replace('_x000D_','  ')}")
        texto2 = texto.replace("x000D","")
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto2}"
        navegador.get(link)
   
        while len(navegador.find_elements(By.CSS_SELECTOR,"._1LbR4 > div:nth-child(2)"))<1:
            time.sleep(1)
        #teste de implementacao
        #time.sleep(30)

        #verifica se carregou
        while len(navegador.find_elements(By.ID, "side")) < 1:
            time.sleep(1)
        navegador.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.ENTER) 
        #print(i)
        contador= i+1;
        time.sleep(5)
    #fechando o navegador
    navegador.quit()


    #Janela de aviso de finalização
    
    contador_str=str(contador)
    messagebox.showinfo("Disparador de Mensagens Zap","O envio de "+ contador_str+ " mensagens foi concluído com Sucesso!")


    

#################### Função Enviar Grupos
def enviar_grupos():

   # print("Enviar Grupos")
    #Janela de busca do arquivo fonte
    #print("Limpar grupos")
    
    messagebox.showinfo("INFO","1-Abra a base de dados\n2-Aguarde o carregamento do Navegador")
    

    

    arquivo = tkinter.filedialog.askopenfilename(title="Selecione o arquivo XLS")


   


    #contatos_df = pd.read_excel("Enviargrupos.xlsx")
    contatos_df = pd.read_excel(arquivo,sheet_name="Lista_2")

    #Descomentar caso queira fazer uma verificação de quem esta sendo copiado
    #print(contatos_df)


    navegador = webdriver.Firefox( )


    navegador.get("https://web.whatsapp.com/")
    #time.sleep(5)
    #Verifica se o rememberMe foi carregado

    while len(navegador.find_elements(By.NAME,"rememberMe")) < 1:
        time.sleep(1)


    #nao permite que o relembre-me fique ativo
    navegador.find_element(By.NAME,"rememberMe").click()
    

    # Def enviar midia
    def enviar_midia(midia,texto_grupo):
        navegador.find_element(By.CSS_SELECTOR,"span[data-icon='clip']").click()
        attach = navegador.find_element(By.CSS_SELECTOR,"input[type='file']")
        attach.send_keys(midia)
        while len(navegador.find_elements(By.CSS_SELECTOR,".Z2O8p > div:nth-child(2)")) <1:
            time.sleep(1)
        msg_attach=navegador.find_element(By.CSS_SELECTOR,".Z2O8p > div:nth-child(2)")
        
        msg_attach.send_keys(texto_grupo)
        while len(navegador.find_elements(By.CSS_SELECTOR,"span[data-icon='send']")) < 1:
            time.sleep(1)
        send = navegador.find_element(By.CSS_SELECTOR,"span[data-icon='send']")
        send.click()

    while len(navegador.find_elements(By.ID,"side")) < 1:
        time.sleep(1)
        time.sleep(10)

    for i, mensagem in enumerate(contatos_df['grupo']):

        grupo = contatos_df.loc[i, "grupo"]

        midia = contatos_df.loc[i, "imagem"]

        texto_grupo = contatos_df.loc[i,"mensagem"].replace('_x000D_','  ')
        texto_grupo_2 = texto_grupo.replace("x000D","")
        





      #verifica 1 inseri agora
        while len(navegador.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')) < 1:
            time.sleep(1)


        navegador.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]').send_keys(grupo)
        #time.sleep(5)
        while len(navegador.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')) < 1:
            time.sleep(1)
        
        navegador.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]').send_keys(Keys.ENTER)
       # time.sleep(5)
        enviar_midia(midia,texto_grupo_2)
        time.sleep(5)
        contador= i+1;
    navegador.quit()

 


    cpntador_str=str(contador)

    messagebox.showinfo("Disparador ZAP","Disparo de Msg de "+ cpntador_str+" anúncios, para os grupos do ZAP concluído")



    

#################### Função Limpar Grupos
def limpar_grupos():#

    #print("Limpar grupos")
    
    messagebox.showinfo("INFO","1-Abra a base de dados\n2-Aguarde o carregamento do Navegador")
    
    
    #Janela de busca do arquivo fonte


    arquivo = tkinter.filedialog.askopenfilename(title="Selecione o arquivo XLS")


  



    #importando os contatos do arquivo grupos

    #contatos_df = pd.read_excel("grupos.xlsx")
    contatos_df = pd.read_excel(arquivo,sheet_name="Base_dados_grupos_2")




    
    
    #abrindo o navegador
    navegador = webdriver.Firefox( )


    #abrindo o whatApp
    navegador.get("https://web.whatsapp.com/")
    #time.sleep(10)

    #Verifica se o rememberMe foi carregado

    while len(navegador.find_elements(By.NAME,"rememberMe")) < 1:
        time.sleep(1)


    #nao permite que o relembre-me fique ativo
    navegador.find_element(By.NAME,"rememberMe").click()

    #garantindo que  a página carregou
    while len(navegador.find_elements(By.ID,"side")) < 1:
        time.sleep(1)
        time.sleep(10)
    contador=0
    contadorerro=0
    #Disparando as mensagens com o laço de repetiçao for
    for i, mensagem in enumerate(contatos_df['grupo']):

        grupo = contatos_df.loc[i, "grupo"]

     #inseri agora
        while len(navegador.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')) < 1: 
            time.sleep(1)  
    
        navegador.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]').send_keys(grupo)
        time.sleep(5)

        #inserir verificacao se o elemento nao existe
        if len(navegador.find_elements(By.XPATH,'//*[@id="pane-side"]/div[1]/div/span'))<1 : 
         

            #inseri agora
            while len(navegador.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')) < 1: 
                time.sleep(1)  


            navegador.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]').send_keys(Keys.ENTER)
            time.sleep(5) 

            #Verifica se é bussines ou nao
            if i ==0:
                time.sleep(3)
            
                if len(navegador.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/span/div[1]/div/div/div/div[2]/div'))==1:
                    #time.sleep(3)
                    navegador.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/span/div[1]/div/div/div/div[2]/div').send_keys(Keys.ENTER)
                ##  while len(navegador.find_elements(By.XPATH,'//*[@id="main"]/header/div[3]/div/div[2]/div/div/span')) < 1: 
                    #   time.sleep(1)
                    
                # navegador.find_element(By.XPATH,'//*[@id="main"]/header/div[3]/div/div[2]/div/div/span').click()             
                else:
                    while len(navegador.find_elements(By.XPATH,'//*[@id="main"]/header/div[3]/div/div[2]/div/div/span')) < 1: 
                        time.sleep(1)
                    
                    navegador.find_element(By.XPATH,'//*[@id="main"]/header/div[3]/div/div[2]/div/div/span').click()
                    #############################################################################################
                    
                




            
            while len(navegador.find_elements(By.XPATH,'//*[@id="main"]/header/div[3]/div/div[2]/div/div/span')) < 1: 
                time.sleep(1)  

            #modificacao teste
            navegador.find_element(By.XPATH,'//*[@id="main"]/header/div[3]/div/div[2]/div/div/span').click()
            # time.sleep(3)

            #inseri agora
            
            while len(navegador.find_elements(By.XPATH,'//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[4]/div[1]')) < 1: 
                time.sleep(1) 
            navegador.find_element(By.XPATH,'//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[4]/div[1]').click()
            #time.sleep(3)

                    #inseri agora
            
            while len(navegador.find_elements(By.XPATH,'//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]')) < 1: 
                time.sleep(1) 
            navegador.find_element(By.XPATH,'//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]').click()
            contador=i+1
            time.sleep(5)
        else:
            navegador.quit()
            #neste caso, devido ao processamento retirar  o problema + 1 Pra apeanas i
            problema=i +1
            problema_str=str(problema)
            messagebox.showinfo("ERRO","Verifique o grupo  "+ problema_str+ ".\nVerifique se o nome do grupo esta correto\nVerifique a conta vinculada\nReinicie a limpeza")
            
    #Termina o for
    #fechando o navegador    
    navegador.quit()


    
    contador_str=str(contador)
   
    messagebox.showinfo("Limpeza zap","Limpeza de "+ contador_str+ " Grupos Finalizada")

  #final da funcao limpar grupos
    








####################################################################################################################################





# Barra de menu
barra_menu=tk.Menu()


#menu arquivo
menu_arquivo=tk.Menu(tearoff=0)
menu_arquivo.add_command(label="Sair",command=janela.quit)
barra_menu.add_cascade(label="Arquivo",menu=menu_arquivo)


#menu ajuda
menu_ajuda=tk.Menu(tearoff=0)

menu_ajuda.add_command(label="Manual",command= mostrar_manual)
menu_ajuda.add_command(label="Sobre",command= mostrar_sobre)
menu_ajuda.add_command(label="Conectar Celular",command=conectar_celular)
barra_menu.add_cascade(label="Ajuda",menu=menu_ajuda)
janela.config(menu=barra_menu)






#titulo dentro da janela com grid
titulo=tk.Label(text="Escolha uma das opções abaixo:",bg="white",height=2)
titulo.grid(row=0,columnspan=3, sticky="NESW")

#botao com imagem esquerda envio clientes
botao=tk.Button(command=enviar_msg)
img_button=tk.PhotoImage(file="/media/ton/bck_full/docs/professional/myprograms/Automatização_zap/Versao_teste/botaocliente.png")
botao.config(image=img_button,bg="white",bd=0,highlightthickness=0,highlightbackground=None,activebackground="white")
botao.grid(row=1,column=0)
#label com grid esquerda
msg=tk.Label(text="Envio Clientes",bg="white")
msg.grid(row=3,column=0)



#botao com imagem centro Envio grupos
botao2=tk.Button(command=enviar_grupos)
img_button2=tk.PhotoImage(file="/media/ton/bck_full/docs/professional/myprograms/Automatização_zap/Versao_teste/botaogrupos.png")
botao2.config(image=img_button2,bg="white",bd=0,highlightthickness=0,highlightbackground=None,activebackground="white")
botao2.grid(row=1,column=1)
#label com grid esquerda
msg=tk.Label(text="Envio Grupos",bg="white")
msg.grid(row=3,column=1)


#botao com imagem direita limpar grupos
botao3=tk.Button(command=limpar_grupos)
img_button3=tk.PhotoImage(file="/media/ton/bck_full/docs/professional/myprograms/Automatização_zap/Versao_teste/botaoLimpeza.png")
botao3.config(image=img_button3,bg="white",bd=0,highlightthickness=0,highlightbackground=None,activebackground="white")
botao3.grid(row=1,column=2)
#label com grid esquerda
msg=tk.Label(text="Limpar Grupos",bg="white")
msg.grid(row=3,column=2)



janela.mainloop()



