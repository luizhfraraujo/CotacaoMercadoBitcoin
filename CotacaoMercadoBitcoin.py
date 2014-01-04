#ticker: indica os dados de retorno da chamada.
#high: maior valor em Reais de negociação do dia.
#low: menor valor em Reais de negociação do dia.
#vol: volume de Bitcoin ou Litecoin negociado no dia.
#last: último valor em Reais negociado.
#buy: valor atual em Reais ofertado para compra.
#sell: valor atual em Reais ofertado para venda.
#date: timestamp da última atualização do ticker.

import json
import os
import urllib.request
import datetime
import time
import smtplib
from email.mime.text import MIMEText

#Variáveis a ser definida pelo usuário
#Aqui deverá ser digitado o valor de Compra e Venda
#LiteCoin
vObjCompraLC = 40.0
vObjVendaLC = 80.0

#BitCoin
vObjCompraBC = 1500.0
vObjVendaBC = 2500.0


vObjBC = 0

def cls():
    os.system("cls")

def status_bitcoin():
    url = 'https://www.mercadobitcoin.com.br/api/ticker/'
    resp = urllib.request.urlopen(url).read()
    data = json.loads(resp.decode('utf-8'))

    return data
    
def status_litecoin():
    url = 'https://www.mercadobitcoin.com.br/api/ticker_litecoin/'
    resp = urllib.request.urlopen(url).read()
    data = json.loads(resp.decode('utf-8'))

    return data

def envia_email(titulo,mensg):
    #cria um cliente smtp que conectará em smtp.gmail.com na porta 587
    gm = smtplib.SMTP("smtp.gmail.com", 587)
    #nos identificamos no servidor
    gm.ehlo()
    #indicamos que usaremos uma conexão segura
    gm.starttls()
    #reidentificamos no servidor (necessário apos starttls )
    gm.ehlo()
    #faz o login
    gm.login("SEU EMAIL DO GMAIL", "SUA SENHA") 
    #Cria um email contendo texto e guarda em mail
    mail = MIMEText(mensg)
    #Seta destinatário e assunto
    mail["To"] = "EMAIL QUE RECEBERA O AVISO"
    mail["Subject"] = titulo
    #Envia o email. 
    gm.sendmail("remetente", "destinatario", mail.as_string())
    #fecha a conexão
    gm.close()
    
cont = 0
while cont == 0:
    data = datetime.datetime.today()
    infoLC = status_litecoin()
    infoBC = status_bitcoin()

    vAtualLC = infoLC["ticker"]["last"]
    vAtualBC = infoBC["ticker"]["last"]

    #Verificar o valor atual e faz as comparações com o valor cadastrado para compra
    if vAtualLC <= vObjCompraLC:
        envia_email("Automático: Compra de LiteCoin","Esta mensagem é automática: A hora é agora de comprar LiteCoins! Valor Atual: %s"%(str(vAtualLC)))

    #Verificar o valor atual e faz as comparações com o valor cadastrado para venda    
    if vAtualLC >= vObjVendaLC:
        envia_email("Automático: Venda de LiteCoin","Esta mensagem é automática: A hora é agora de vender LiteCoins! Valor Atual: %s"%(str(vAtualLC)))

    #Verificar o valor atual e faz as comparações com o valor cadastrado para compra
    if vAtualBC <= vObjCompraBC:
        envia_email("Automático: Compra de BitCoin","Esta mensagem é automática: A hora é agora de comprar BitCoins! Valor Atual: %s"%(str(vAtualBC)))

    #Verificar o valor atual e faz as comparações com o valor cadastrado para venda    
    if vAtualBC >= vObjVendaBC:
        envia_email("Automático: Venda de BitCoin","Esta mensagem é automática: A hora é agora de vender BitCoins! Valor Atual: %s"%(str(vAtualBC)))

        
    #conn.commit()
    
    minuto = 60
    while minuto > 0:
        cls()
        print("----------------------")
        print("-Hora:",str(data.hour) +":"+ str(data.minute) +":"+ str(data.second))
        print("-Data:",str(data.day) +"/"+ str(data.month) +"/"+ str(data.year))
        print("----------------------")

        print("Informações do BitCoin")
        print("-Maior: R$", infoBC["ticker"]["high"])
        print("-Menor: R$", infoBC["ticker"]["low"])
        print("-Volume de negociações dia: R$", infoBC["ticker"]["vol"])
        print("-Último valor: R$", infoBC["ticker"]["last"])
        print("-Valor atual para compra: R$", infoBC["ticker"]["buy"])
        print("-Valor atual para venda: R$", infoBC["ticker"]["sell"])
        
        print("\n")
        
        print("Informações do LiteCoin")
        print("-Maior: R$", infoLC["ticker"]["high"])
        print("-Menor: R$", infoLC["ticker"]["low"])
        print("-Volume de negociações dia: R$", infoLC["ticker"]["vol"])
        print("-Último valor: R$", infoLC["ticker"]["last"])
        print("-Valor atual para compra: R$", infoLC["ticker"]["buy"])
        print("-Valor atual para venda: R$", infoLC["ticker"]["sell"])
        

        print("\n")
        print("Próxima atualização em: %s segundos"%minuto)
        minuto = minuto - 1
        time.sleep(1)
    
