from timeit import timeit
from memory_profiler import profile

lista_grande = list(range(1000000))
lista_com_duplicata = lista_grande + [1]


#Solução 1
def tem_duplicados_sol_1(lista):
  for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
      if lista[i] == lista[j]:
        return True
  return False
tempo1 = timeit(lambda: tem_duplicados_sol_1(lista_com_duplicata))

@profile
def memoria_tem_duplicados_sol_1(lista):
  for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
      if lista[i] == lista[j]:
        return True
  return False


#Solução 2
def tem_duplicados_sol_2(lista):
  lista_ordenada = sorted(lista)
  for i in range(len(lista_ordenada) - 1):
    if lista_ordenada[i] == lista_ordenada[i + 1]:
      return True
  return False
tempo2 = timeit(lambda: tem_duplicados_sol_2(lista_com_duplicata))

@profile
def memoria_tem_duplicados_sol_2(lista):
  lista_ordenada = sorted(lista)
  for i in range(len(lista_ordenada) - 1):
    if lista_ordenada[i] == lista_ordenada[i + 1]:
      return True
  return False

#Solução 3
def tem_duplicados_sol_3(lista):
  elementos_vistos = set()
  for elemento in lista:
    if elemento in elementos_vistos:
      return True
    elementos_vistos.add(elemento)
  return False
tempo3 = timeit(lambda: tem_duplicados_sol_3(lista_com_duplicata))

@profile
def memoria_tem_duplicados_sol_3(lista):
  elementos_vistos = set()
  for elemento in lista:
    if elemento in elementos_vistos:
      return True
    elementos_vistos.add(elemento)
  return False



print("### Solução 1 ###")
print(f"{tempo1} segundo")
memoria_tem_duplicados_sol_1(lista_com_duplicata)
print(tem_duplicados_sol_1(lista_com_duplicata))


print("\n### Solução 2 ###")
print(f"{tempo2} segundo")
memoria_tem_duplicados_sol_2(lista_com_duplicata)
print(tem_duplicados_sol_2(lista_com_duplicata))
print("\n### Solução 2 ###")
print(f"{tempo2} segundo")
memoria_tem_duplicados_sol_2(lista_com_duplicata)
print(tem_duplicados_sol_2(lista_com_duplicata))


print("\n### Solução 3 ###")
print(f"{tempo3} segundo")
memoria_tem_duplicados_sol_3(lista_com_duplicata)
print(tem_duplicados_sol_3(lista_com_duplicata))


'''
# Relatório

# Após a análise utilizando a biblioteca "timeit", 
# observamos que a Solução 3 apresenta a melhor eficiência em termos de tempo.

# Ordem de eficiência por tempo (do mais rápido ao mais lento):
# 1°) Solução 3
# 2°) Solução 2
# 3°) Solução 1

# Por outro lado, ao empregar a biblioteca "memory_profiler", 
# a Solução 1 se destaca como a mais eficiente em termos de uso de espaço.

# Ordem de eficiência por espaço (do menor ao maior):
# 1°) Solução 1
# 2°) Solução 2
# 3°) Solução 3

# As saídas obtidas foram as seguintes:
# Solução 1: True
# Solução 2: True
# Solução 3: True

Alternativa marcada: c - Abordagem 3 é mais eficiente em tempo, mas consome mais espaço
Alternativa correta: c - Abordagem 3 é mais eficiente em tempo, mas consome mais espaço
d - Abordagem 1 é mais eficiente em espaço, mas menos eficiente em tempo
'''
