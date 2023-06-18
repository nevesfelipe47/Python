"""

Exercício: Verificador de Número Par ou Ímpar

Crie um programa em Python que solicite ao usuário um número inteiro e verifique se esse número é par ou ímpar. Em seguida, exiba uma mensagem indicando o resultado.

Dicas:

Use a função input() para solicitar ao usuário um número inteiro.
Converta o número para o tipo int para garantir que seja um valor inteiro.
Utilize o operador % (resto da divisão) para verificar se o número é par ou ímpar. Um número é par se o resto da divisão por 2 for igual a 0, caso contrário, é ímpar.
Utilize a estrutura condicional if-else para exibir a mensagem correta de acordo com o resultado.

"""

n = int(input("Dita ai um número comparsa: "))

if n % 2 == 0:
    print(n," É par comparsa")
else: 
    print(n," É impar comparsa")