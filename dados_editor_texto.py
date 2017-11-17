from constantes_editor_texto import *

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
