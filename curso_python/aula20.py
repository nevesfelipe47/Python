num1 = int(input('Digita um numero ai bença: '))
num2 = int(input('Digita outro numero ai bença: '))

if num1 > num2:
    maior_valor = num1
    print(maior_valor, " é o maior valor!")
elif num1 < num2 : 
    maior_valor = num2
    print(maior_valor, " é o maior valor!")
elif num1 == num2: 
    print("Valores iguais")

