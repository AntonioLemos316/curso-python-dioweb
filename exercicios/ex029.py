# Forma que será encontrada na maioria das vezes
frutas = ["Laranja", "Maçã", "Uva"]

# Lista vazia
# frutas = []

# Método construtor list
letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "Recife", True]

print(frutas)
print(carro[-1])
#pegando o ultimo valor

matriz = [
    [1, "a", 2],
    [3, 4, "f"],
    ["o", 5, 2]
]

print(matriz)
print(matriz[0][1])
print(matriz[1][0])
print(matriz[2][2])

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice} : {carro}")

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

lista = []
lista.append(2)
lista.append("String")
lista.append(["array", "?", "muito", "parecido", "!"])
# [2, 'String', ['array', '?', 'muito', 'parecido', '!']]
print(lista)

lista.clear()
# limpar lista
print(lista)

lista = [0, 1, 2, 3, 4]
print(len(lista))