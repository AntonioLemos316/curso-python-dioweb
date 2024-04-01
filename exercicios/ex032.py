# pessoa = {"nome": "Gui", "idade":28}
# # ambos os códigos são equivalentes
# pessoa = dict(nome="Gui", idade=28)

# nome = pessoa["nome"] # Gui
# print(nome)

contatos = {
    "gui@email.com": {"nome": "Gui", "telefone": "3333-3333"},
    "silva@email.com": {"nome": "Silva", "telefone": "3344-3333"},
    "marques@email.com": {"nome": "Marques", "telefone": "3355-3333"},
}

telefone = contatos["silva@email.com"]["telefone"] # 3344-3333
print(telefone)