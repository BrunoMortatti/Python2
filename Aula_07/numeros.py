'''
    Docstring é as 3 aspas = documentação do código.
    Programa para mostrar números inteiros por extenso. Somente números de 1 a 100.
    Array = use símbolo de [].
    Tupla = use o símbolo de ().
'''
from os import system
system('cls')
dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez" "onze", "doze", "treze",
"quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove")
valor = input('Informe um número de 1 a 99:')
numerico = int(valor)
extenso = ''
if(numerico < 20):
    #print(numeros[numerico])
    extenso = numeros[numerico]
elif(numerico < 100):
    #print(valor[1:1])
    #print(dezenas[int(valor[0:1])], 'e', numeros [int(valor[1:2])])
    extenso = dezenas[int(valor[0:1])]
if (valor[1:2]!="0"):
    extenso = f"{extenso} e {numeros[int(valor[1:2])]}"
print(extenso)