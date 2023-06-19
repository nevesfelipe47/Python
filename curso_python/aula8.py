nome = str(input("Digita teu nome ai: "))
sobrenome = str(input("Digita teu sobrenome ai: "))
idade = int(input("Tua idade bença: "))
ano_nascimento = int(input("Ano que tu nasceu desgrama: "))

maior_idade = idade >=18

if maior_idade:
    maior_idade = "Sim"
else:
    maior_idade = "Não"

altura_metros = float(input ("Tua altura mermao: "))

print("Nome: ",nome)
print("Sobrenome: ",sobrenome)
print("Idade: ",idade)
print("Nascimento: ",ano_nascimento)
print("É maior de idade? ",maior_idade)
print("Altura: ",altura_metros)
