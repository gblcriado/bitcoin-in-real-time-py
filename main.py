from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image

# import ---------

import requests
import json

# cores ---------

co0 = "#444466"  # preto 
co1 = "#feffff"  # branco
co2 = "#6f9fbd"  # azul

fundo = "#484f60" 


# Criação da janela ------------
janela = Tk()
janela.title('')
janela.geometry('320x300')
janela.configure(bg=fundo)

# Dividindo a janela em 2 frames ----------
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

primeira_parte = Frame(janela, width=320, height=50, bg = co1, pady=0, padx=0, relief='flat')
primeira_parte.grid(row=1, column=0)

segunda_parte = Frame(janela, width=320, height=300, bg = fundo, pady=0, padx=0, relief='flat')
segunda_parte.grid(row=2, column=0, sticky=NW)


# função para dados

def info():
    api_link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CBRL'


    # ----HTTP requests---
    response = requests.get(api_link)

    # converter os dados em dicionario
    dados = response.json()

    # Valor em Dolar

    valorUSD = float(dados['USD'])
    formatoUSD = "{:,.3f}".format(valorUSD)
    l_precoUSD['text'] = 'Valor em Dolar: $' + formatoUSD

    # Valor em Euro
    valorEUR = float(dados['EUR'])
    formatoEUR = "{:,.3f}".format(valorEUR)
    l_precoEUR['text'] = 'Valor em Euro: €' + formatoEUR

    
    # Valor em Real
    valorBRL = float(dados['BRL'])
    formatoBRL = "{:,.3f}".format(valorBRL)
    l_precoBRL['text'] = 'Valor em Real: R$' + formatoBRL

    # Atualizar em tempo real
    segunda_parte.after(1000, info)





# configurando o frame cima ---------------


l_titulo = Label(primeira_parte, text='Bitcoin Price Tracker', bg= co1,fg=co2, relief=FLAT, anchor = 'center', font=('Arial 20'))
l_titulo.place(x=0, y=5)

# configurando o frame baixo --------------

l_precoBT = Label(segunda_parte, text='Valor de 1 Bitcoin em tempo real', bg= fundo,fg=co1, relief=FLAT, anchor = 'center', font=('Arial 16'))
l_precoBT.place(x=10, y=30)

l_precoUSD = Label(segunda_parte, text='', bg= fundo,fg=co1, relief=FLAT, anchor = 'center', font=('Arial 12'))
l_precoUSD.place(x=10, y=100)

l_precoEUR = Label(segunda_parte, text='', bg= fundo,fg=co1, relief=FLAT, anchor = 'center', font=('Arial 12'))
l_precoEUR.place(x=10, y=130)

l_precoBRL = Label(segunda_parte, text='', bg= fundo,fg=co1, relief=FLAT, anchor = 'center', font=('Arial 12'))
l_precoBRL.place(x=10, y=160)


info()

janela.mainloop()