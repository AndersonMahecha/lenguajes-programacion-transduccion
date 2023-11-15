# Taller 2

## Definicion de la gramatica

La gramatica de este lenguaje sera parecida a la de Golang.

## Ejemplos
### Declara una variable
#### Variables sin inicializar
Es posible declarar una variable sin inicializarla, en este caso, el valor por defecto sera el valor cero del tipo de dato de la variable.
Por ejemplo:

```None
var b int
print(b)
>>> 0
var a float
print(a)
>>> 0.0
var c bool
print(c)
>>> False
var d string
print(d)
>>>
var e [5][2]int
print(e)
>>> [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
```
#### Variables inicializadas
Es posible declarar una variable inicializada, en este caso, el valor por defecto sera el valor asignado.
Por ejemplo:

```None
var b int = 5
print(b)
>>> 5
var a float = 5.5
print(a)
>>> 5.5
var c bool = True
print(c)
>>> True
var d string = "Hola mundo"
print(d)
>>> "Hola mundo"
var e [2][2] int = {{1, 2}, {3, 4}}
print(e)
>>> [[1, 2], [3, 4]]
```

#### Variables con inferencia de tipo
Es posible declarar una variable sin especificar el tipo de dato, en este caso, el tipo de dato sera inferido por el valor asignado.
Esto solo es posible en variables inicializadas.
Por ejemplo:

```None
var b = 5
print(b)
>>> 5
var a = 5.5
print(a)
>>> 5.5
var c = True
print(c)
>>> True
var d = "Hola mundo"
print(d)
>>> "Hola mundo"
var e = {{1, 2}, {3, 4}}
print(e)
>>> [[1, 2], [3, 4]]
```
### Condicionales
#### If
Es posible declarar una condicion if, en este caso, se ejecutara el bloque de codigo si la condicion es verdadera.
Por ejemplo:

```None
var edad int = 15
if edad >= 18 {
    print("Eres mayor de edad.")
} else {
    print("Eres menor de edad.")
}
>>> Eres menor de edad.
```
En caso de que la condicion sea falsa, se ejecutara el bloque de codigo del else, si este existe.
Por ejemplo:

```None
var edad int = 21
if edad >= 18 {
    print("Eres mayor de edad.")
} else {
    print("Eres menor de edad.")
}  
>>> Eres mayor de edad.
```
Es posible tener condiciones con multiples valores de entrada. En este caso se evaluaran el resultado de toda la condicion.
Por ejemplo:

```None
var edad int = 21
var nombre string = "Juan"
if edad >= 18 and nombre == "Juan" {
    print("Eres mayor de edad y te llamas Juan.")
} else {
    print("No eres mayor de edad o no te llamas Juan.")
}
>>> Eres mayor de edad y te llamas Juan.
```

un ejemplo usando el operador or:

```None
var edad int = 10
var nombre string = "Juan"
if edad >= 18 or nombre == "Juan" {
    print("Eres mayor de edad o te llamas Juan.")
} else {
    print("No eres mayor de edad y no te llamas Juan.")
}
>>> Eres mayor de edad o te llamas Juan.
```

### Ciclos
#### For
Es posible declarar un ciclo for, en este caso, se ejecutara el bloque de codigo mientras la condicion sea verdadera.
Por ejemplo:
(Nota: los ciclos aun no se pueden ejecutar, solo se validan)
```None
var i int=0

for var i=0; i<40; i*=3{
    print(i)
    i++
}
>>> 0
>>> 3
>>> 9
```

### Funciones
Es posible declarar una funcion, en este caso, se ejecutara el bloque de codigo cuando se llame a la funcion.
Por ejemplo:
(Nota: las funciones aun no se pueden ejecutar, solo se validan)
```None
funcion suma(a int, b int) int {
    return a + b
}
```

#### Built-in functions
##### Print
Es posible imprimir en consola usando la funcion print.
Por ejemplo:
```None
print("Hola mundo")
>>> Hola mundo
```
#### Regresion lineal
Es posible calcular la regresion lineal de un conjunto de datos usando la funcion linearRegression.
(Nota: Los datos de entrada deben ser una matriz de 2xN, donde la primera fila son los valores de x y la segunda fila son los valores de y)
Por ejemplo:
```None
var data [2][10] float = {{1.1,2.5,3.1,4.2,2,2.5,2.8,2.7,1.8,3.8},{13.64,24.05,26.78,30.63,21.22,24.05,25.49,25.03,19.88,29.36}}
linearRegression(data)
>>>ecuacion de la regresion lineal: y = 5.2112x+10.2033
>>>{{Imagen de los datos}}
>>>> {{Imagen de la regresion lineal}}
```
#### Plot
Es posible graficar un conjunto de datos usando la funcion plot.
(Nota: Los datos de entrada deben ser una matriz de 2xN, donde la primera fila son los valores de x y la segunda fila son los valores de y)
Por ejemplo:
```None
var data [2][10] float = {{1.1,2.5,3.1,4.2,2,2.5,2.8,2.7,1.8,3.8},{13.64,24.05,26.78,30.63,21.22,24.05,25.49,25.03,19.88,29.36}}
plot(data)
>>>{{Imagen de los datos}}
```
### Operaciones matematicas soportadas
- Suma (+)
- Resta (-)
- Multiplicacion (*)
- Division (/)
- Modulo (%)
### Operaciones logicas soportadas
- Igualdad (==)
- Mayor que (>)
- Menor que (<)
- Mayor o igual que (>=)
- Menor o igual que (<=)
- Diferente (!=)
- And (and)
- Or (or)
### Operaciones trigonometricas soportadas
- Seno (sin(angle))
- Coseno (cos(angle))
- Tangente (tan(angle))
- Arcoseno (asin(angle))
- Arcocoseno (acos(angle))
- Arcotangente (atan(angle))

### Operaciones de matrices soportadas
- Suma (matrixSuma(matrix1, matrix2))
- Resta (matrixResta(matrix1, matrix2))
- Multiplicacion (matrixMultiplicacion(matrix1, matrix2))
- Transpuesta (matrixTranspuesta(matrix))
- Inversa (matrixInversa(matrix))

#### Ejemplo de uso de operaciones de matrices
```None
var a [2][2] int = {{1,2},{3,4}}
var b [2][2] int = {{5,6},{7,8}}

print(matrixSuma(a,b))
print(matrixResta(a,b))
print(matrixMultiplicacion(a,b))
print(matrixTranspuesta(a))
print(matrixInversa(a))
>>>[[6, 8], [10, 12]]
>>>[[-4, -4], [-4, -4]]
>>>[[19, 22], [43, 50]]
>>>[[1, 3], [2, 4]]
>>>[[-1.9999999999999996, 0.9999999999999998], [1.4999999999999998, -0.4999999999999999]]
```

## Analizador lexico
Esta definicion puede ser encontrada en el archivo [lenguaje.g4](lenguaje.g4).  
Se hace uso de la libreria [antlr4](https://www.antlr.org/) para generar el analizador lexico y sintactico.

## Analizador semantico
Para generar el analizador semantico, se debe ejecutar el comando 
```
antlr4 -v 4.13.0 -Dlanguage=Python3 -visitor -no-listener lenguaje.g4  -o generatedcode
```
Luego para ejecutar el analizador semantico, se debe ejecutar el comando
```
python semantic.py {{archivo de entrada}}
```