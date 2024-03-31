# Python na dio

## Visão Geral

- Linguagem amigal e intuitiva
- Código aberto
- Código tão inteligível quanto o inglês
- Adequada para tarefas diárias e produtiva
- Lançada em 1991 a versão 0.9.0
- Em 2000 na sua segunda versão nasce list comprehensions e a melhoria feita no coletor de lixo
- Em 2001 nasce a PSF que contem toda a documentação
- Em 2008 nasce a versão 3.0 que vem com uma melhora brutal na performance

## Onde devo utilizar o Python

- Tipagem dinâmica e forte
- Multiplataforma e multiparadigma
- Comunidade gigante e ativa
- Curva de aprendizado baixa
- Não é forte em desenvolvimento mobile

## Programar é uma receita

- Programar consiste no ato de informar o computador uma sequência de passos que devem ser processadas
- Arquivo em python tem extensão py

## Primeiros passos em Python

- O padrão Hello World

```bash
    print('Hello World')
```

- Para exibir no terminal só é ir até o local do aquivo atraves do cd e digitar python nome do arquivo(ex001.py) no meu caso, é bom sempre olhar com ls onde estamos localizado e em seguida usar o cd para mover entre as pastas.

<img src="./img/python001.PNG">

## Tipos em python

- Serve para definir caracteristicas e comportamentos de um valor (objeto) para o interpretador:
- Texto = str
- Númerico = int, float, complex
- Sequência = list, tuple, range > array
- Mapa = dict > chave:valor > nome:lemos
- Coleção = set, fronzenset > parecido com array
- Booleano = bool > true e false
- Binário = bytes, bytearray, memoryview

<img src="./img/python002.PNG">

## Modo interativo, funções dir e help em python

- O interpretador do Python pode exercutar em modo que permite ao desenvolvedor escrever e ver o resultado na hora
- Colocando (python) no terminal ou executando o scipt com a flag -i(python -i app.py) para sair escrevo exit()
- Dir sem argumentos dir() e com argumentos dir(100), retorna a lista de nomes dos metodos que podemos exercutar no escopo local atual
- Help sem argumentos help() e com argumentos help(100), vai falar quais são os argumentos que o metodo recebe, o que ele retorna e como funciona
- Dir e Help são basicamente uma documentação offline

## Variáveis e constantes em python

- Variáveis

```bash
    age = 18
    name = 'Silva'
    print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')
    // Meu nome é Silva e eu tenho 18 ano(s) de idade.
```

```bash
    age2, name2 = (18, 'Silva')
    print(f'Meu nome é {name2} e eu tenho {age2} ano(s) de idade.')
    // Meu nome é Silva e eu tenho 18 ano(s) de idade.
```

- Variáveis: alterando valores em python precisamos declarar as variáveis por que é dessa forma que ele consegue indentificar os tipos delas e para substituir só é atribuir um novo valor

```bash
    age = 25
    name = 'Lemos'
    print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')
    // Meu nome é Lemos e eu tenho 25 ano(s) de idade.
```

```bash
    age2, name2 = (21, 'Maria')
    print(f'Meu nome é {name2} e eu tenho {age2} ano(s) de idade.')
    // Meu nome é Maria e eu tenho 21 ano(s) de idade.
```

- Constantes: em python não tem palavra reservada para constantes igual em javascript que colocamos, const nome = 'Silva' por exemplo, em python usamos uma convenção escrevendo a variável toda em maíuscula NOME = 'Lemos'

- Boas práticas: em python é bom escrever em snake case ESTADOS_BRASILEIROS, NOME_COMPLETO, limite_saque_diario e sobre constantes o interpretador não consegue bloquear a alteração de uma 'constante'

## Convertendo tipos em python

- Inteiro para float

```bash
    preco = 10
    print(preco)
    // 10

    preco = float(preco)
    print(preco)
    // 10.0

    preco = 10 / 2
    print(preco)
    // 5.0
```

- Float para inteiro

```bash
    preco = 10.30
    print(preco)
    // 10.3

    preco = int(preco)
    print(preco)
    // 10
```

- Conversão por divisão com // o numero int é preservado como inteiro, com apenas / o numero int é transformado em float

```bash
    preco = 10
    print(preco)
    // 10

    print(preco / 2)
    // 5.0

    print(preco // 2)
    // 5
```

- Número para string

```bash
    preco = 10.50
    idade = 19

    print(str(preco))
    // 10.5

    print(str(idade))
    // 19

    texto = f"idade {idade} preco {preco}"
    print(texto)
    // idade 19 preco 10.5
```

- String para número

```bash
    preco = "10.50"
    idade = "19"

    print(float(preco))
    // 10.5

    print(int(idade))
    // 19
```

- Erro de conversão

```bash
    preco = "python"
    print(float(preco))

    Traceback (most recent call last):
    File "C:\Users\Toni\Documents\MeusProjetos\curso-python-dioweb\exercicios\ex004.py", line 34, in <module>
    print(float(preco))
    ValueError: could not convert string to float: 'python'
```

## Funções de entrada e saída em python

- Função builtin input é utilizada para ler dados de entrada(teclado) basicamente fazer uma interação com o usuário

- Função print é utilizada para exibir dados de saída(tela), posso atribuir argumentos opcionais (sep, end, file e flush) todos são convertidos para string e é exibida para o usário

```bash
    nome = input("Informe o seu nome abaixo: \n")
    print('Seu nome é', nome, end="...\n")
    print('Seu nome é', nome, sep="#")
    // Informe o seu nome abaixo:
    // Silva
    // Seu nome é Silva...
    // Seu nome é#Silva
```

## Operadores artiméticos em python

```bash
# Adição
print(1 + 1)
# 2

# Subtração
print(10 - 5)
# 5

# Multiplicação
print(10 * 5)
# 50

# Divisão
print(10 / 2)
# 5.0

# Divisão inteira
print(10 // 2)
# 5

# Módulo
print(10 % 3)
# 1

# Exponenciação
print(2 ** 3)
# 8
```

## Operadores de comparação em python

```bash
saldo = 450
saque = 200
print(saldo == saque)
# == igual
# false
print(saldo != saque)
# != diferente
#true
print(saldo >= saque)
# >= maior ou igual
#true
print(saldo <= saque)
#<= menor ou igual
#false
```

## Operadores de atribuição em python

```bash
saldo = 500
print(saldo)
# = atribuir
# 500
# saldo += 200
# print(saldo)
# saldo = saldo + 200
# 700
saldo -= 100
print(saldo)
# saldo = saldo - 100
# 400
```

## Operadores Lógicos em python

```bash
saldo = 1000
saque = 200
limite = 100
print(saldo >= saque and saque <= limite)
# True and False = False
# False
# Operador and em python, similar/igual ao && em js
```

```bash
saldo = 1000
saque = 200
limite = 100
print(saldo >= saque or saque <= limite)
# True and False = True
# True
# Operador or em python, similar/igual ao || em js
```

```bash
saldo = 1000
saque = 200
limite = 100
print(not saldo >= saque)
# A negação de True é False
# False
# Operador not em python, similar/igual ! em js
```

## Operadores de identidade em python

```bash
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) # ocupa o mesmo espaço na mémoria ? False
print(a is not b) # não ocupa o mesmo espaço na mémoria ? True
```

```bash
curso = 'curso em python'
curso_python = curso

print(curso is curso_python) # ocupa o mesmo espaço na mémoria ? True
print(curso is not curso_python) # não ocupa o mesmo espaço na mémoria ? False
```

## Operador de associação em python

```bash
curso = "Curso de Python"
frutas = ["Maçã", "Uva", "Pera"]
saques = [1500, 500]

print("Python" in curso)
# "Python" está dentro da variável curso = True
# True
print("Laranja" not in frutas)
# "Laranja" não está dentro do array frutas = True
# True
print(200 in saques)
# 200 está dentro do array saques = False
# False
```

## Identação e blocos em python

- Em python identar alem de manter o código legível e manutenível ele também exerce um papel importante de definir onde um bloco de comando inicia e onde ele termina em javascript seria {} para delimitar inicio/fim de um bloco, em python não tem, ele tem apenas : para definir o inicio do bloco
- Em python utilizamos uma convenção de 4 espaçoes em branco para identar um bloco

```bash
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire o dinheiro na boca do caixa!")

    print("Obrigado por ser nosso cliente tenha um bom dia!")

sacar(500)
# Valor sacado!
# Retire o dinheiro na boca do caixa!
# Obrigado por ser nosso cliente tenha um bom dia!
```

## Estruturas condicionais em python

```bash
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")
# if se o saque for maior exibir Realizando saque!
# if se o saque for menor exibir Saldo insuficiente!
```

```bash
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")
# if se o saque for maior exibir Realizando saque!
# else se o saque não for maior exibir Saldo insuficiente!
```

```bash
opcao = int(input("Informe uma opção: \n[1] Sacar\n[2] Extrato\n"))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    exit("Opção inválida")
# if se opcao for igual a 1 pedimos a quantia que será sacada
# elif se não, se igual a 2 exiba o extrato
# else se não opção inválida
```

## if aninhado em python

```bash
conta_normal = True
conta_universidade = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Saldo insuficiente!")
elif conta_universidade:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")
else:
    print("Sistema não reconhece essa opção, entre em contato com o banco")
```

## If ternário em python

```bash
saldo = 500
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")
# Sucesso ao realizar o saque!
```

## Estrutura de repetição em python

```bash
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()
# python
# o
# Geralmente utilizamos o for quando temos um valor predeterminado
```

## Função range com for no python

```bash
for numero in range(0, 11):
    print(numero, end=" ")
# 0 1 2 3 4 5 6 7 8 9 10
# Geralmente utilizamos o for quando temos um valor predeterminado
```

```bash
# Tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")
# 0 5 10 15 20 25 30 35 40 45 50
# Geralmente utilizamos o for quando temos um valor predeterminado
```

## While em python

```bash
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibir o extrato...")

print("Obrigado por utilizar nosso Sistema")
# Geralmente utilizamos o while quando não temos um valor predeterminado
```

```bash
while True:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibir o extrato...")
    elif opcao == 0:
        break

print("Obrigado por utilizar nosso Sistema")
# Bem parecido com o outro exemplo só que contem o break
# Geralmente o break é utilizado em um loop infinito como no exemplo acima
```
