from dados_editor_texto import *
'''
No arquivo funcoes temos as funcoes necessarias para o editor de texto ja implementadas 
'''
'''======================================================FUNCOES====================================================='''

"---------------------------------------------------DESENHA_TEXTO------------------------------------------------------"
'''
A funcao desenha_texto representa as definicoes necessarias para que haja um texto 
Interp. essa funcao tem todos os componentes necessarios para o dado texto funcionar, nela esta definido como iniciara
o texto na tela do usuario.
obs: Cada linha que tera o editor texto sera uma string
'''
def desenha_texto(texto):
    fonte = pg.font.SysFont("times new roman", 30)
    alinhamento = 10
    if len(texto) != 0:                                     #Caso o tamanho do texto seja diferente de ZERO
        escrita = ""
        for itens in texto:
            escrita = ""
            texto = fonte.render(itens, 1, (0, 0, 0))
            TELA.blit(texto, (0, alinhamento))
            alinhamento += 40  #alinhamento eh igual a alinhamento+40
            escrita += itens  #escrita eh igual a escrita+itens

"------------------------------------------------DESENHA_EDITOR_TEXTO--------------------------------------------------"
'''desenha_editor_texto: Editor_texto -> Editor_texto"
Interp. a funcao desenha_editor_texto recebe todos os parametros definidos na funcao desenha_texto. 

'''
def desenha_editor_texto(Editor_texto):
    desenha_texto(Editor_texto.texto)  #fnc

"-------------------------------------------------------TRATA_TEXTO----------------------------------------------------"
'''trata_texto: Texto, tecla -> Texto
interp. trata_texto recebe o texto atual, e a tecla nova que foi digitada,
se nao for Espaço ou BackSpace, ela é adicionada no Texto'''
'''
'''

def trata_texto(texto,tecla):
    #-----------Tecla apagar--------------------------------------------------------------------------------------------
    if tecla == pg.K_BACKSPACE:
        ultima_linha = texto[-1]                     #texto[-1] é o último elemento da lista
        ultima_linha = ultima_linha[0:-1]       #ultima_linha[0:-1] fatia a lista e pega o primeiro e o ultimo caractere
        texto[-1] = ultima_linha
        return texto

    #-----------Tecla Enter---------------------------------------------------------------------------------------------
    elif tecla == pg.K_RETURN:
        nova_linha = ""
        texto.append(nova_linha)    #funcao append acresenta a nova_linha ao texto
        return texto

    #----------Quebra de Linha Automatico-------------------------------------------------------------------------------
    else:
        ultima_linha = texto[-1]
        if len(ultima_linha) > 85:             #85 eh o maximo de caracteres que cabem em uma linha
            nova_linha = ""
            texto.append(nova_linha)
        ultima_linha = texto[-1]
        ultima_linha = ultima_linha +(chr(tecla))   #chr retorna uma string de um caractere cujo código ASCII
        texto[-1] = ultima_linha
        return texto

"-----------------------------------------------TRATA-CURSOR-----------------------------------------------------------"
    #'DIREITA'
    #if tecla == pg.K_RIGHT:

    #if tecla == pg.K_LEFT:

    #if tecla == pg.K_UP:

   # if tecla == pg.K_DOWN:

'''
trata_editor_texto : Editor_texto, EventoTecla -> Editor_texto
Interp. a funcao trata_editor_texto recebe todos os trata_texto e retorna o Editor_texto
'''
def trata_editor_texto(Editor_texto,tecla):
    Editor_texto.texto = trata_texto(Editor_texto.texto,tecla)
    return Editor_texto


