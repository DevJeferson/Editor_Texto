#!/usr/bin/env python
# -*- coding: utf-8 -*-
from universe import *
'''________________________________________EDITOR-DE-TEXTO-AVANÇADO(Versão 1.0)______________________________________'''

'''=====================================================TELA E CONSTANTES=========================================== '''
"========>Preparacao da Tela e das Constantes<========"
(LARGURA, ALTURA) = (1009, 507)
TELA = pg.display.set_mode((LARGURA, ALTURA))
CENTRO_X = LARGURA / 2;
CENTRO_Y = ALTURA / 2;
print(CENTRO_Y)

ImagemFundo = pg.image.load('2.png')
TELA.blit(ImagemFundo,(0,0))
'''==============================================DEFINICOES DE DADOS================================================='''
"-------Dado Principal------"
#Editor_texto = namedtuple("texto,selecao...")

'''Editor_texto e criado como: Editor_texto(Texto,selecao,........)
Interp. Um Editor_Texto é composto por um Texto,... 
'''
"====Exemplos==="
"===Template==="


"---------Dados Segundarios--------"
'''
O Texto é uma lista de Strings, ou seja é uma lista de palavras
interp. representa o que o usuario digita no teclado
'''
"===Exemplos==="

TEXTO_INICIAL = [""]
TEXTO_1= ["Hello World"]
TEXTO_2 = ["teste", ""]
TEXTO_1_DEPOIS_DO_ENTER = ["Jefer", ""]
DIGITEI_A = ["Jefer", "A"]

'''====Template===:
def fn_para_texto(t):
    ... t    #faz algo com t
'''

'''
A selecao e uma representacao do inicio e final de uma linha e coluna 
Interp. selecao representara o inicio e o final da selecao de um texto
'''
"====Exemplos==="
# SELECAO_INICIAL = [0,2][0,4]
# SELECAO_MAIOR = [2,3][2,15]
# SELECAO_DUAS_LINHAS = [1,4][2,12]
# SELECAO_TUDO = [0,0][15,30]

"===Template==="
'''
def selecao(Inicial,Final):
    ....
'''


'''=================================================================================================================='''


'''======================================================FUNCOES====================================================='''

"===================================================DESENHA EDITOR======================================================"
'''desenha_editor: Texto -> Imagem
interp. recebe uma string, e desenha ela na tela'''

# def desenha_editor(texto):
#     fonte = pg.font.SysFont("times new roman", 30)
#     if texto !="":
#         texto = fonte.render(str(texto), 1, (0, 0, 0))
#     else:
#         texto = fonte.render(1, (255, 0, 0))
#     TELA.blit(texto,(0,10))

"===================================================DESENHA TEXTO======================================================"
'''
desenha texto representa as definicoes necessarias para que haja um texto 
Interp.
obs: Cada linha e uma string
'''
def desenha_texto(texto):
    fonte = pg.font.SysFont("times new roman", 30)
    alinhamento = 10
    if len(texto) != 0:
        escrita = ""
        #cont = 0
        for itens in texto:
            escrita = ""
            texto = fonte.render(itens, 1, (0, 0, 0))
            TELA.blit(texto, (0, alinhamento))
            alinhamento += 40
            escrita += itens

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

'''
=======================TRATA_TEXTO====================
'''
def trata_texto(texto,tecla):
    "----------Tecla apagar-----------"
    if tecla == pg.K_BACKSPACE:
        ultima_linha = texto[-1]
        ultima_linha = ultima_linha[0:-1]
        # --------APAGAR LINHA ANTERIOR------
        # if ultima_linha == [""]:
        #     texto.pop()
        # else:
        texto[-1] = ultima_linha
        return texto

    #"----------Tecla Enter-----------"
    elif tecla == pg.K_RETURN:
        nova_linha = ""
        texto.append(nova_linha)    #funcao append significa acresentar
        return texto
    #"----Quebra de Linha Automatico----"
    else:
        ultima_linha = texto[-1]
        if len(ultima_linha) > 80:
            nova_linha = ""
            texto.append(nova_linha)
        ultima_linha = texto[-1]
        ultima_linha = ultima_linha +(chr(tecla))
        texto[-1] = ultima_linha
        return texto

"================SELECAO================"
#Inicial = (int,int)
#Final = (int,int)
#def selecao(Inicial, Final):



"===========================================BIG-BANG============================="
'''EstadoMundo: Texto -> Texto'''
def main(texto):
    big_bang(texto, \
             tela=TELA, \
             desenhar=desenha_texto, \
             quando_tecla=trata_texto, \
             )

main(TEXTO_INICIAL)