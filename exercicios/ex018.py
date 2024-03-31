texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto: 
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()
# python
# o

for letra in texto: 
    if letra.upper() in VOGAIS:
        print(letra, end="")
# else:
#     print() # excuta uma quebra de linha
#     print("Final do laço")