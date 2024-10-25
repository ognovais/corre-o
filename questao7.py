lista = [x for x in range (5)]
print(lista)

lista = list(range(5))
print(lista)

lista = []
i = 0
while i < 5:
  lista.append(i)
  i += 1
print (lista)

# Relatório:
# Saídas obtidas:
# A: [0, 1, 2, 3, 4]
# B: [0, 1, 2, 3, 4]
# C: [0, 1, 2, 3, 4]
#
# Respostas corretas:
# Todas as saídas são iguais: [0, 1, 2, 3, 4]
#
# Resposta marcada: A e C
# Análise dos erros: Embora eu tenha marcado apenas A e C, a resposta correta inclui também o código B, que produz o mesmo resultado. Todos os três códigos produzem a mesma lista de saída. É importante revisar as alternativas para garantir que todas as opções corretas sejam consideradas.
