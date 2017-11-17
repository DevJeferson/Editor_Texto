from funcoes_editor_texto import *
"===========================================BIG-BANG============================="
'''EstadoMundo: Texto -> Texto'''
def main(texto):
    big_bang(texto, \
             tela=TELA, \
             desenhar=desenha_texto, \
             quando_tecla=trata_texto, \
             )

main(TEXTO_INICIAL)