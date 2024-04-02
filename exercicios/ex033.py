def exibir_ola():
    print("Olá mundo!")
exibir_ola() # Olá mundo!

def exibir_param(param):
    print(f"Olá {param}")
exibir_param("testando") # Olá testando

def exibir_num(num = 2):
    print(f"Exibindo: {num}")
exibir_num() # Exibindo 2

def exibir_soma(num1, num2):
    return print(f"Soma: {num1 + num2}")
exibir_soma(5, 2) # Soma: 7

def calcular_total(lista_numeros):
    return sum(lista_numeros)
print(calcular_total([1, 5, 14])) # 20

def sucessor_e_antecessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1 
    return antecessor, sucessor
print(sucessor_e_antecessor(5)) # (4, 6) 

def salvar_user(nome, email, senha):
    user = (nome, email, senha,) # passando como tupla, testei a list e sempre alterava a ordem
    return print(user)
salvar_user(nome = "Lemos", email = "lemos@email.com", senha = "123")
salvar_user("Silva", "silva@email.com", "123456")
salvar_user("teste@email", "teste_nome", "123456") # passar os parametros assim pode resultar em erro
salvar_user(**{"nome":"Oliveira", "email":"oliveira@email.com", "senha":"123"}) # passando como dicionário

salario = 500

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario
# declarando uma varável que recebe 500
# criando uma função que tem um parâmetro chamado bônus
# através da palavra-chave global conseguimos enxergar a variável salario e com isso pegamos seu valor
# salario vai receber ele mesmo (salário) + o bônus que será passado através do parâmetro (bonus)
# resumo não é uma boa prática usar o global é parecido com o var do js que ficou em desuso
result = salario_bonus(100)
print(result) # 600