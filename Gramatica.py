class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


def precedencia(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def construir_arbol(expresion):
    operadores = []
    operandos = []

    def aplicar_operador():
        op = operadores.pop()
        der = operandos.pop()
        izq = operandos.pop()
        nodo = Nodo(op)
        nodo.izq = izq
        nodo.der = der
        operandos.append(nodo)

    tokens = list(expresion.replace(" ", ""))

    for token in tokens:
        if token.isalnum():
            operandos.append(Nodo(token))

        elif token == '(':
            operadores.append(token)

        elif token == ')':
            while operadores and operadores[-1] != '(':
                aplicar_operador()
            operadores.pop()

        else:
            while (operadores and
                   precedencia(operadores[-1]) >= precedencia(token)):
                aplicar_operador()
            operadores.append(token)

    while operadores:
        aplicar_operador()

    return operandos[0]


def dibujar_arbol(nodo, nivel=0):
    if nodo is not None:
        dibujar_arbol(nodo.der, nivel + 1)
        print('   ' * nivel + nodo.valor)
        dibujar_arbol(nodo.izq, nivel + 1)

#Prueba

with open("pruebaGr.txt", "r") as archivo:
    for linea in archivo:
        expresion = linea.strip()

        if expresion == "":
            continue

        print("\nExpresión:", expresion)

        try:
            arbol = construir_arbol(expresion)

            print("Árbol:\n")
            dibujar_arbol(arbol)

        except:
            print("Error en la expresión")
