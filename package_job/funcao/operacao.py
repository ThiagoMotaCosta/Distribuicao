from calculadora import lista_numeros

print(lista_numeros)

operacao = input("Escolha somar, mínimo, máximo: ")
if operacao == "somar":
    valor = sum
elif operacao == "mínimo":
    valor = min
elif operacao == "máximo":
    valor = max
else:
    print("Valor inválido. Repita a ação")

def calcular(lista_numeros):
    numeros = [int(numero) for numero in lista_numeros]
    resultado = valor(numeros)
    print(resultado)

calcular(lista_numeros)


