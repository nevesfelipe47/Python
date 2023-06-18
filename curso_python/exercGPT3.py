"""
Exercício: Contagem regressiva

Crie um programa em Python que solicite ao usuário um número inteiro positivo e faça uma contagem regressiva a partir desse número até zero. Em cada iteração, exiba na tela o número atual da contagem.

Dicas:

Use a função input() para solicitar ao usuário um número inteiro positivo.
Converta o número para o tipo int para garantir que seja um valor inteiro.
Utilize um laço de repetição while para fazer a contagem regressiva.
Inicie uma variável com o valor digitado pelo usuário e, em cada iteração, decremente o valor da variável em 1.
Verifique se o valor da variável é maior ou igual a zero para continuar a contagem.
Utilize a função print() para exibir o número atual da contagem.


"""
numero =int(input("Digita ai galeroso: "))

while numero >= 0:
 print(numero)

 numero-=1