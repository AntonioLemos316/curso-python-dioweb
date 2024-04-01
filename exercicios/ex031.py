listaNum = set([1, 1, 2, 2, 3, 4, 5])
print(listaNum)

tupla_de_carros = set(("palio", "gol", "gol", "celta", "palio",))
print(tupla_de_carros)
# {"palio", "gol", "celta"}

numeros = {1, 2, 3, 4, 5} # set | conjunto

numeros = list(numeros)

for numero in numeros:
    print(numero)


carros = {"gol", "palio", "celta"} 
for indice, carro in enumerate(carros):
    print(f"{indice} : {carro}")

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.union(conjunto_b))
# {}.union
# {1, 2, 3, 4}
print(conjunto_a.intersection(conjunto_b))
# {}.intersection
# {2, 3}
print(conjunto_a.difference(conjunto_b))
# {1}
print(conjunto_b.difference(conjunto_a))
# {4}
print(conjunto_a.symmetric_difference(conjunto_b))
# {1, 4}
print(conjunto_a.issubset(conjunto_b))
# False
print(conjunto_b.issubset(conjunto_a))
# False
print(conjunto_a.issuperset(conjunto_b))
# False
print(conjunto_b.issuperset(conjunto_a))
# False
print(conjunto_a.isdisjoint(conjunto_b))
# False
print(conjunto_b.isdisjoint(conjunto_a))
# False

sorteio = {1, 23, 24}
sorteio.add(5)
print(sorteio)

sorteio.copy()
print(sorteio)

sorteio.discard(1)
print(sorteio)

sorteio.pop()
print(sorteio)

sorteio.remove(23)
print(sorteio)

print(1 in sorteio)

print(len(sorteio))

sorteio.clear()
print(sorteio)

