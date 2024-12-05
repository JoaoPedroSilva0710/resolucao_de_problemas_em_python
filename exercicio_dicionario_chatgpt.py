# Nome: João Pedro Silva Barbosa
# Data: 03/19/2024
# este projeto foi proposto pelo chatGPT para se resolver um problema envolvendo dicionarios,
# segue abaixo o enunciado:

# Desafio: Contagem de Palavras Únicas

# Escreva uma função em Python chamada contagem_palavras_unicas que aceita uma lista de palavras
# como entrada e retorna um dicionário onde as chaves são as palavras únicas na lista e 
# os valores são as contagens de quantas vezes cada palavra aparece na lista. Por exemplo:
# def contagem_palavras_unicas(lista_palavras):

# # Exemplo de uso
# palavras = ["gato", "cachorro", "gato", "cavalo", "cachorro", "gato"]
# print(contagem_palavras_unicas(palavras))

# Saída esperada:

# {'gato': 3, 'cachorro': 2, 'cavalo': 1}



from collections import Counter

def contagem_palavras_unicas(lista_palavras):
    # contador = Counter(cod_cliente for cod_cliente, *_ in lista_palavras)
    lista_qtde = []
    contador = {}
    for x in lista_palavras:
     lista_qtde =  lista_palavras.count(x)
     contador[x] = lista_qtde

    return contador
#Exemplo de uso
palavras = ["gato", "cachorro", "gato", "cavalo", "cachorro", "gato"]
print(contagem_palavras_unicas(palavras))