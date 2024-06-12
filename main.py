### Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.


# produtos = [
#     {'id': 1, 'nome':'teclado', 'preco': 10.20},
#     {'id': 2, 'nome':'Mouse', 'preco': 80},
#     {'id': 3, 'nome':'Monitor', 'preco': 100}
# ]

# # Atualizar o preço do produto com id 2 para 90

# for produto in produtos:
#     if produto['id'] == 2:
#         produto['preco'] = 90
    
# print(produtos)

#Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario_merged = {**dicionario1, **dicionario2}
print(dicionario_merged)