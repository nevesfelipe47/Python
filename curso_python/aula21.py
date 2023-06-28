
"""
#Operadores lógicos 
and (e) or (ou) not (não)

and - Todas as condições precisam ser verdadeiras.
Se qualquer valor for considerado falso, 
a expressão inteira será avaliada naquele valor
São considerados falso ( que vc ja viu)
0.0.0 '' false
Tambem existe o tipo None que é usado para representar um
não valor
"""

entrar = input('[E]ntrar ou [S]air:')

if entrar.lower() == 'e':
    senha = int(input('Digite a senha'))
    if senha == 123456:
        print("Bem Vindo ao sistema!")
    else:
        print("Senha Inconreta")
elif entrar.lower == 's':
    print('Saiu do Sistema!')
else: 
    print("OPÇÃO INCORRETA")