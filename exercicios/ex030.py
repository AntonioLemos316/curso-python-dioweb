frutas = ("laranja", "pera", "uva",)
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])
pais = ("Brasil",)

print(frutas[0])
print(type(pais))

matriz = (
    (1, "a", 2),
    (3, 4, "f"),
    ("o", 5, 2),
)

print(matriz[0][1])
# a
print(matriz[1][0])
# 3
print(matriz[2][2])
# 2

print(type(matriz))