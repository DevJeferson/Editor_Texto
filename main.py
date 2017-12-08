from funcoes_editor_texto import *
"====================================================BIG-BANG=========================================================="
'''EstadoMundo: Texto -> Texto
'''
def main(texto):
    big_bang(texto, \
             tela=TELA, \
             desenhar=desenha_editor_texto, \
             quando_tecla=trata_editor_texto, \
             )

main(EDITOR_TEXTO_INICIAL)