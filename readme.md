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

## Modo interativo, funções dir e help

- O interpretador do Python pode exercutar em modo que permite ao desenvolvedor escrever e ver o resultado na hora
- Colocando (python) no terminal ou executando o scipt com a flag -i(python -i app.py) para sair escrevo exit()
- Dir sem argumentos dir() e com argumentos dir(100), retorna a lista de nomes dos metodos que podemos exercutar no escopo local atual
- Help sem argumentos help() e com argumentos help(100), vai falar quais são os argumentos que o metodo recebe, o que ele retorna e como funciona
- Dir e Help são basicamente uma documentação offline

## Variáveis e constantes no python

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

## Funções de entrada e saída

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

