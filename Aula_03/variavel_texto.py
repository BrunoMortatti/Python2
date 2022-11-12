from os import system
#importa as bibliotecas do sistema operacional
system('cls')
#criação de variável texto
#As variáveis devem seguir um padrão
#snake_case, PascalCase ou camelCase
#nome_completo
#Nome_Completo
#nomeCompleto
nome_completo ='Laercio Azevedo de Sá'
print(len(nome_completo))
nome_completo ='Bruno Cesar Mortatti'
print(len(nome_completo)) #len = conta a quantidade de caracteres
print(nome_completo.count('e', 5, 8)) #conta a repetiçção de um caracter
print(nome_completo.upper())
print(nome_completo.lower())
print(nome_completo.capitalize())
print(nome_completo.find(' '))
espaco = nome_completo.find(' ')
nome = nome_completo [0:espaco]
print(nome)
print(nome_completo.replace(' ', '#'))
print(nome_completo.center(80,"*"))
print(nome_completo.split(' '))