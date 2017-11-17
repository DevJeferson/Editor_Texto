from dados_editor_texto import *

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



