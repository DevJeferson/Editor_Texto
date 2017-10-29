#!/usr/bin/env python
# -*- coding: utf-8 -*-
from universe import *

"========Developers: Jeferson e Edgar=========="

'''========================================EDITOR-DE-TEXTO-AVANÇADO(Versão 1.0)======================================'''

'''=========================================Preparacao da Tela e Constantes:======================================== '''

#Preparação da TELA:
'_________________________________________________'
(LARGURA, ALTURA) = (1080, 600)                 '|'
TELA = pg.display.set_mode((LARGURA, ALTURA))   '|'
CENTRO_X = LARGURA / 2;                         '|'
CENTRO_Y = ALTURA / 2;                          '|'
                                                '|'
print(CENTRO_Y)                                 '|'
'________________________________________________|'


'''=============================================Inicio das definições de dados======================================='''

'''
O Texto é uma lista de Strings, ou seja é uma lista de palavras
interp. representa o que o usuario digita no teclado
Exemplos:
'''

TEXTO_INICIAL = ""
TEXTO_1= "Hello World"
TEXTO_2= "Bah Tche"

'''====Template===:
def fn_para_texto(t):
    ... t    #faz algo com t
'''

#EXEMPLOS:

LISTA_INICIAL = [""]
LISTA_1 = ["Jefer"]
LISTA_2 = ["teste",""]

LISTA_1_DEPOIS_DO_ENTER = ["Jefer", ""]
DIGITEI_A = ["Jefer", "A"]

'''============================================Fim das definições de dados==========================================='''


'''=================================================Inicio das funções==============================================='''

'''desenha_texto: Texto -> Imagem
interp. recebe uma string, e desenha ela na tela'''

def desenha_texto(texto):
    fonte = pg.font.SysFont("times new roman", 30)
    if texto !="":
        texto = fonte.render(str(texto), 1, (0, 0, 0))
    else:
        texto = fonte.render("", 1, (255, 0, 0))

    ## blit: String, (Int, Int)
    #TELA.blit(texto, (0, CENTRO_Y -30))
    TELA.blit(texto,(0,10))


"===================================================DESENHA LISTA======================================================"



def desenha_lista(lista):
    fonte = pg.font.SysFont("times new roman", 30)

    alinhamento = 10
    if len(lista) != 0:
        escrita = ""
        for itens in lista:
            escrita += itens


            if itens == '\r':

                texto = fonte.render(escrita, 1, (0, 0, 0))
            else:
                texto = fonte.render("", 1, (255, 0, 0))

            TELA.blit(texto, (0, alinhamento))
            alinhamento += 40




        texto = fonte.render (escrita, 1, (0, 0, 0))
    else:
        texto = fonte.render("", 1, (255, 0, 0))




    # blit: String, (Int, Int)
    #TELA.blit(texto, (0, CENTRO_Y -30))

    TELA.blit(texto,(0,alinhamento))
    alinhamento += 40


    #TELA.blit(texto,(0,10))

#CRIAR O QUEBRA LINHA





#QUEBRA DE LINHAS AUTOMATICO


#while










'-----------Definições dos Botoes---------'










'''==================================TRATA_TECLA============================'''
'''trata_tecla: Texto, tecla -> Texto
interp. recebe o Texto atual, e a tecla nova que foi digitada,
se nao for Espaço ou BackSpace, ela é adicionada no Texto'''

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




#LISTAS

def trata_lista(lista,tecla):
    if tecla == pg.K_SPACE:
        lista.append(" ")
        return lista
    if tecla == pg.K_BACKSPACE[-1]:
        lista.pop()
        return lista
    #if tecla == pg.K_TAB:
     #   return texto+""""""

    #if tecla == pg.K_RETURN:
     #   return texto + "\r"

    else:
        lista.append(chr(tecla))
        return lista

"===========================================BIG-BANG============================="
'''EstadoMundo: Texto -> Texto'''
def main(texto):
    big_bang(texto, \
             tela=TELA, \
             desenhar=desenha_lista, \
             quando_tecla=trata_lista, \
             )

main(LISTA_INICIAL)