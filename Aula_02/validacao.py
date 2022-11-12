"""
Calcular área do retângulo
"""
print("***Cálculo da Área do retângulo***\n")
print("")
print("Informe o primeiro lado")
lado1 = input()
print("informe o segundo lado:")
lado2 = input()
# variável.isnumeric = verifica se pode ser um número inteiro
# variável.isdecimal = verifica se pode ser um número com casas decimais 
print("O primeiro valor é número?", lado1.isnumeric())
print("O segundo valor é númnero inteiro?", lado2.isnumeric())
print("Será que vai dar certo ou vai dar erro?")
# int = transforma o valor da variável em inteiro
# float = transforma o valor da variável em float (decimal)
area = int(lado1) * int(lado2)
print("A área do retângulo é {} m² sendo os lados de {} x {}" .format(area, lado1, lado2))
print("A área do retângulo é", area, "m² sendo os lados de", lado1, "x", lado2)