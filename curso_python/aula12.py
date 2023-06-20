nome = input("Nome: ")
altura = float(input("Altura: "))
peso = float(input("Peso: "))


imc = peso/(altura**2)

print(nome, " tem ", altura, "m de altura, e seu peso é ",peso, "KG.")
print("Seu IMC deu: ", imc)