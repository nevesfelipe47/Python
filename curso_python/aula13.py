nome = input("Nome: ")
altura = float(input("Altura: "))
peso = float(input("Peso: "))


imc = peso/(altura**2)

linha_1 = f'{nome} tem {altura:.2f}m de altura'
linha_2 = f'pesa {peso} quilos e seu imc é '
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
