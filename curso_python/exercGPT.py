
"""
Exercício: Calculadora de Média

Crie um programa em Python que solicite ao usuário três notas (N1, N2 e N3) e calcule a média aritmética dessas notas. Em seguida, exiba a média calculada na tela.

Dicas:

Use a função input() para solicitar ao usuário as três notas separadamente.
Converta as notas para o tipo float para permitir números decimais.
Calcule a média aritmética somando as três notas e dividindo por 3.
Utilize a função print() para exibir a média calculada na tela.

"""
nota1= float(input("DIGITA N1: "))
nota2= float(input("DIGITA N2: "))
nota3= float(input("DIGITA N3: "))

media = (nota1+nota2+nota3)/3

print(media)