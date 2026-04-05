# Árbol de Expresiones en Python

## Descripción

Este programa en Python permite leer expresiones matemáticas desde un archivo de texto (`pruebaGr.txt`), construir su árbol AST y mostrarlo en consola de forma jerárquica.

---

## Funcionamiento

El programa realiza los siguientes pasos:

1. Lee cada línea del archivo `pruebaGr.txt`
2. Procesa la expresión eliminando espacios
3. Construye un árbol binario:

   * Nodos internos: operadores (`+`, `-`, `*`, `/`)
   * Hojas: operandos (números o letras)
4. Imprime el árbol en consola de forma estructurada

##

---

## Ejecución

```
python3 gramatica.py < pruebaGr.txt
```

---

## Archivo de entrada

El archivo `entrada.txt` debe contener una expresión por línea. Ejemplo:

```
3+4
3+4*5
(3+4)*5
a+b*c
(a+b)*(c-d)/e
```

---

## Ejemplo de salida

Para la expresión:

```
3+4*5
```

El programa genera:

```
      5
   *
      4
+
   3
```

Esto indica que primero se realiza la multiplicación y luego la suma.

---

## Consideraciones

* Solo se permiten:

  * Números y letras como operandos
  * Operadores: `+`, `-`, `*`, `/`
  * Paréntesis
* Expresiones inválidas pueden generar errores, pero el programa intenta manejarlos sin detener la ejecución.

##
