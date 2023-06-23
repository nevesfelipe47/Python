"""
No contexto do Python, o termo "format" refere-se ao método format() disponível em objetos do 
tipo string. Esse método permite formatar uma string substituindo partes específicas por valores dinâmicos.

A sintaxe básica do método format() é a seguinte:
"""
 #      string.format(valor1, valor2, ...)

# Aqui está um exemplo simples que demonstra o uso do método format():

nome = str(input('Nome: '))
idade = int(input('Idade: '))
peso = float(input('Peso: '))

mensagem = "Ola, meu nome é {} e eu tenho {} anos e peso {:.2f}.".format(nome,idade,peso)

print(mensagem)

"""
Nesse exemplo, a string "Olá, meu nome é {} e eu tenho {} anos." contém dois espaços reservados 
para os valores de nome e idade. O método format() substitui esses espaços pelos valores correspondentes, 
resultando na saída:

"""

# Olá, meu nome é Alice e eu tenho 25 anos.


"""
Você também pode especificar o índice dos valores na função format() para controlar a ordem das substituições. 
Por exemplo:

"""

nome = "Bob"
idade = 30
mensagem = "Olá, meu nome é {1} e eu tenho {0} anos.".format(idade, nome)
print(mensagem)


"""
Olá, meu nome é Bob e eu tenho 30 anos.

Além disso, o método format() também suporta formatação avançada, permitindo especificar a precisão decimal, 
largura de campo, alinhamento e outros detalhes. 
Aqui está um exemplo:

"""

preco = 19.99
mensagem = "O preço do produto é: R${:0.2f}".format(preco)
print(mensagem)

# Nesse exemplo, {:0.2f} especifica que o valor preco será formatado como um número de ponto 
# flutuante com 2 casas decimais, resultando na saída:

# O preço do produto é: R$19.99

"""
Essas são apenas algumas das funcionalidades básicas do método format(). Existem muitas outras opções e possibilidades de 
formatação disponíveis. Você pode consultar a documentação oficial do Python para obter mais detalhes e exemplos 
completos sobre o uso do método format().

"""

