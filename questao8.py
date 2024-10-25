def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = calcular_imc(peso, altura)

classificacao = classificar_imc(imc)

print(f"O IMC é: {imc:.2f}")
print(f"Classificação segundo a OMS: {classificacao}")

# Relatório:
# Saída obtida: O IMC é: (valor calculado) e Classificação segundo a OMS: (classificação)
# Resposta correta: Depende dos valores de peso e altura inseridos pelo usuário.
# Resposta escrita: Errada
# Análise dos erros: Errei no uso dos else e if, pois o código não estava funcionando corretamente.
