def func(n):
  if n == 0:
      return 1
  else:
      return n * func(n - 1)

print(func(3))

# Relatório:
# Saída obtida: 6
# Resposta correta: 6
# Resposta marcada: 6
# Análise dos erros: Não houve erro. O código calcula corretamente o fatorial de 3, que é 3 * 2 * 1 = 6.
