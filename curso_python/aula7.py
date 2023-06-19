"""
 Variaveis são usadas para salvar algo na memoria do computador.
 PEP8: inicie variavei com letras minusculas, pode usar numeros e underline.
 O sinal de = é o operador de atribuição. Ele é usado para 
 atribuir um valor a um nome (variavel).
Uso: nome_variavel = expressao

"""

#nome_completo = 'Luiz Otavio Miranda'
#soma_dois_mais_dois = 2+2
#print(nome_completo, soma_dois_mais_dois) 


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

maior_idade = idade >= 18

if maior_idade:
    print(nome, "tem", idade, "anos e é de maior.",maior_idade)
else:
    print(nome, "tem", idade, "anos e não é de maior.")