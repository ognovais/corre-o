def soma_diagonal_principal(matriz):
  soma = 0
  for i in range(len(matriz)):
    soma += matriz[i][i]
  return soma

def soma_diagonal_principal(matriz):
  soma = 0
  for i in range(len(matriz)): 
      soma += matriz[i][-i]
  return soma

def soma_diagonal_principal(matriz):
  soma = 0
  for linha in matriz:
    for elemento in linha:
      soma += elemento
  return soma

def soma_diagonal_principal(matriz):
  soma = 0
  for i in range(len(matriz)):
    soma += matriz[i][len(matriz)-i-1] 
  return soma

def soma_diagonal_principal(matriz):
  soma = 0
  for i in range(len(matriz)):
    soma += matriz [len(matriz)-i-1][i]
  return soma

matriz = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

resultado = soma_diagonal_principal(matriz)
print(f'Soma da diagonal principal: {resultado}')

# Relatório:
# Saída obtida: 15
# Resposta correta: 15 (diagonal principal: 1 + 5 + 9)
# Resposta marcada: D (soma da diagonal secundária: 3 + 5 + 7 = 15)
# Análise dos erros: A resposta marcada (D) é correta, mas refere-se à soma da diagonal secundária, enquanto a correta (A) é para a diagonal principal. É importante distinguir entre os dois tipos de diagonais ao analisar a matriz.
