from universe import *
'''================================================TELA E CONSTANTES================================================ '''
"--------------------------------------->Preparacao da Tela e das Constantes<------------------------------------------"
'''
No arquivo constantes temos as definicoes necessarias para criacao da TELA do editor de texto, tudo que eh constante 
esta nesse arquivo.
'''
(LARGURA, ALTURA) = (1080, 600)
TELA = pg.display.set_mode((LARGURA, ALTURA))
clock = pg.time.Clock()
CENTRO_X = LARGURA / 2;
CENTRO_Y = ALTURA / 2;
print(CENTRO_Y)

"======================================================================================================================"