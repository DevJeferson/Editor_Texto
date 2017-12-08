from constantes_editor_texto import *
'''==============================================DEFINICOES DE DADOS================================================='''
'''
No arquivo dados temos as definicoes de cada dado que sera necessario para o editor de texto, as definicoes aqui 
expressas auxiliam para entender como funcionara cada dado do programa
'''
"-----------------------------------------------------EDITOR_TEXTO-----------------------------------------------------"
from namedlist import namedlist
Editor_texto = namedlist("Editor_texto","texto")  #estrutura do editor

'''Editor_texto pode ser criado como: Editor_texto(Texto)
Interp.: Um Editor_Texto é composto por um Editor_texto que eh um dado que contem as funcoes e dados necessarios
para o programa funcionar corretamente  
'''
"_____________________________________________________Exemplos_________________________________________________________"
TEXTO_INICIAL = [""]
EDITOR_TEXTO_INICIAL = Editor_texto(TEXTO_INICIAL)
"____________________________________________________Template__________________________________________________________"
'''
def fn_para_Editor_texto(editor):
    ...editor.texto
        ...
'''

'''
"-------------------------------------------------------TEXTO----------------------------------------------------------"
O Texto é uma lista de Strings, ou seja é uma lista de palavras
interp. representa o que o usuario digita no teclado 
'''

"______________________________________________________Exemplos________________________________________________________"
TEXTO_1= ["Hello World"]
TEXTO_2 = ["teste", ""]
TEXTO_1_DEPOIS_DO_ENTER = ["Jefer", ""]
DIGITEI_A = ["Jefer", "A"]

"_______________________________________________________Template_______________________________________________________"
'''
def fn_para_texto(t):
    ... t    #faz algo com t
'''


'''
Para que haja as opcoes de trocar a fonte e o tamanho do texto digitado temos que ter um dado que saiba a posicao
e indice atual, para isso criei o que chamei de selecao,tambem houve a necessidade de um cursor.
Obs: Faltou implementar essas funcoes
'''

"------------------------------------------------------SELECAO---------------------------------------------------------"
import collections
from collections import namedtuple
Selecao = namedtuple("Selecao", "Lin_Ini,Col_Ini,Lin_Fin,Col_Fin") #estrutura da selecao
'''
A selecao e uma representacao do inicio e final de uma linha e coluna 
Interp. selecao representara o inicio e o final da selecao de um texto
'''

"_________________________________________________________Exemplos_____________________________________________________"
#SELECAO_INICIAL = [0,2][0,4]
# SELECAO_MAIOR = [2,3][2,15]=
# SELECAO_DUAS_LINHAS = [1,4][2,12]
# SELECAO_TUDO = [0,0][15,30]

"_______________________________________________________Template_______________________________________________________"
'''
def selecao(s):
    ....
'''


"______________________________________________________(THE END)_______________________________________________________"