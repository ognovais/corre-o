alpha = float(input('Informe alpha: '))
x = float(input('Informe X: '))

if alpha > 0.1:
    print('Valor inválido para alpha')
else:
    if x < 0:
        print(alpha * x)
    else:
        print(x)

alpha = float(input('Informe alpha: '))
x = float(input('Informe X: '))

if alpha > 0.1:
    print('Valor inválido para alpha')
else:
    if x < 0:
        print(alpha * x)
    else:
        print(x)

# Relatório:
# O código solicita ao usuário que insira os valores de alpha e x.
# Se alpha for maior que 0.1, uma mensagem de erro é exibida.
# Caso contrário, se x for negativo, o código retorna o resultado de alpha * x.
# Se x for maior ou igual a zero, ele simplesmente retorna x.

# Saída obtida: 
# - Se alpha > 0.1: "Valor inválido para alpha"
# - Se alpha <= 0.1 e x < 0: resultado de alpha * x
# - Se alpha <= 0.1 e x >= 0: valor de x

#Análise de erros: Tudo
