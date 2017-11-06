#!/usr/bin/env python
# -*- coding: utf-8 -*-
from universe import *

'''========================================EDITOR-DE-TEXTO-AVANÇADO(Versão 1.0)======================================'''

'''=========================================Preparacao da Tela e Constantes:======================================== '''

#Preparação da TELA:
'_________________________________________________'
(LARGURA, ALTURA) = (1080, 600)
TELA = pg.display.set_mode((LARGURA, ALTURA))
CENTRO_X = LARGURA / 2;
CENTRO_Y = ALTURA / 2;

print(CENTRO_Y)
'-------------------------------------------------'

'''=============================================Inicio das definições de dados======================================='''

'''
O Texto é uma lista de Strings, ou seja é uma lista de palavras
interp. representa o que o usuario digita no teclado
'''

'''
-------------------------Exemplos----------------------:
'''
TEXTO_INICIAL = ""
TEXTO_1= "Hello World"
TEXTO_2= "Bah Tche"
#================
LISTA_INICIAL = [""]
LISTA_1 = ["Jefer"]
LISTA_2 = ["teste",""]
LISTA_1_DEPOIS_DO_ENTER = ["Jefer", ""]
DIGITEI_A = ["Jefer", "A"]

'''====Template===:
def fn_para_texto(t):
    ... t    #faz algo com t
'''

'''
O intervalo tera um inicio e um fim, alem de ter uma posicao no eixo x e y
Interp. representa um intervalo
obs: lista = lista de intervalos
'''

'''
=============Template===========
def intervalos(lista_intervalos):
    len(lista_intervalos)
    ...
'''

'''============================================Fim das definições de dados==========================================='''


'''=================================================Inicio das funções==============================================='''


"===================================================DESENHA TEXTO======================================================"
'''desenha_texto: Texto -> Imagem
interp. recebe uma string, e desenha ela na tela'''

def desenha_texto(texto):
    fonte = pg.font.SysFont("times new roman", 30)
    if texto !="":
        texto = fonte.render(str(texto), 1, (0, 0, 0))
    else:
        texto = fonte.render("", 1, (255, 0, 0))
    TELA.blit(texto,(0,10))
"===================================================DESENHA LISTA======================================================"
'''
desenha lista representa as definicoes necessarias para que haja uma lista
Interp.
obs: Cada linha e uma string
'''

def desenha_lista(lista):
    fonte = pg.font.SysFont("times new roman", 30)
    alinhamento = 10
    if len(lista) != 0:
        escrita = ""
        #cont = 0
        for itens in lista:
            escrita = ""
            texto = fonte.render(itens, 1, (0, 0, 0))
            TELA.blit(texto, (0, alinhamento))
            alinhamento += 40
            escrita += itens

'-----------Definições dos Botoes---------'


'''======================================================TRATA_TECLA================================================='''
'''trata_tecla: Texto, tecla -> Texto
interp. recebe o Texto atual, e a tecla nova que foi digitada,
se nao for Espaço ou BackSpace, ela é adicionada no Texto'''

"----------------Trata_tecla------------"
def trata_tecla(texto, tecla):
    if tecla == pg.K_SPACE:
        return texto+" "
    if tecla == pg.K_BACKSPACE:
        return texto[:-1]
    if tecla == pg.K_TAB:
        return texto+""""""
    if tecla == pg.K_RETURN:
        return texto + "\n"
    else:
        return texto+chr(tecla)

"===========================TRATA MOUSE========================="
def trata_mouse(gato, x, y, ev):
    if ev == pg.MOUSEBUTTONDOWN:
        return x
    else:
        return gato



'''
=======================TRATA_LISTA====================
'''

def trata_lista(lista,tecla):
    "----------Tecla apagar-----------"
    if tecla == pg.K_BACKSPACE:
        ultima_linha = lista[-1]
        ultima_linha = ultima_linha[0:-1]
        lista[-1] = ultima_linha
        return lista
    #"----------Tecla Enter-----------"
    elif tecla == pg.K_RETURN:
        nova_linha = ""
        lista.append(nova_linha)
        return lista
    #"----Quebra de Linha Automatico----"
    else:
        ultima_linha = lista[-1]
        if len(ultima_linha) > 80:
            nova_linha = ""
            lista.append(nova_linha)
        ultima_linha = lista[-1]
        ultima_linha = ultima_linha +(chr(tecla))
        lista[-1] = ultima_linha
        return lista




#MOUSE
    #if tecla ==  pg.mouse.get_pos():
     #   len(pg.mouse.get.pos)


   # if tecla == pg.MOUSEBUTTONDOWN:

"===========================================BIG-BANG============================="
'''EstadoMundo: Texto -> Texto'''
def main(texto):
    big_bang(texto, \
             tela=TELA, \
             desenhar=desenha_lista, \
             quando_tecla=trata_lista, \
             quando_mouse=trata_mouse, \
             )

main(LISTA_INICIAL)