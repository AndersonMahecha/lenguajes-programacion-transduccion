# Taller 2

## Definicion de la gramatica

La gramatica de este lenguaje sera parecida a la de Golang.

```none
<programa> ::= <declaracion>* | <sentencia>* EOF

<declaracion> ::= <declaracionVariable> | <declaracionFuncion>

<declaracionVariable> ::= "var" <identificador> (<tipo>? "=" <expresion>)?

<tipo> ::= "int" | "float" | "string" | "bool"

<declaracionFuncion> ::= "func" <identificador> "(" <listaParametros> ")" (<tipo>)? <bloque>

<listaParametros> ::= <parametro> ("," <parametro>)* | ε

<parametro> ::= <identificador> <tipo>

<bloque> ::= "{" <sentencia>* "}"

<sentencia> ::= <declaracionVariable>
            | <asignacion>
            | <condicional>
            | <cicloFor>
            | <llamadaFuncion>
            | <modificacion>
            | <retorno>

<asignacion> ::= <identificador> ("=" <expresion>)?

<condicional> ::= "if" <comparacion> <bloque> ("else" <bloque>)?

<comparacion> ::= <expresion> (<operadorComparacion> <expresion>)*

<operadorComparacion> ::= "==" | "!=" | "<" | ">" | "<=" | ">="

<operadorAritmetico> ::= "+" | "-" | "*" | "/" | "^" | "%"

<modificacion> ::= <identificador> (<operadorModificadorSimple> | <operadorModificadorCompuesto> (<identificador> | <expresion>))

<operadorModificadorSimple> ::= "++" | "--"

<operadorModificadorCompuesto> ::= "+=" | "-=" | "*=" | "/=" | "^=" | "%="

<cicloFor> ::= "for" <declaracionVariable> ";" <comparacion> ";" <modificacion> <bloque>

<llamadaFuncion> ::= <identificador> "(" <listaArgumentos> ")"

<listaArgumentos> ::= <expresion> ("," <expresion>)* | ε

<retorno> ::= "return" <expresion>?

<expresion> ::= <termino> (<operadorAritmetico> <termino>)* | <llamadaFuncion>

<termino> ::= <factor> ((("^" | "%") <factor>)*

<factor> ::= <identificador> | <entero> | <decimal> | <cadena> | "true" | "false" | "(" <expresion> ")"

<identificador> ::= <LETRA> (<LETRA> | <DIGITO>)*

<entero> ::= <DIGITO>+

<decimal> ::= <entero> "." <entero>

<cadena> ::= '"' .*? '"'

<LETRA> ::= [a-zA-Z]

<DIGITO> ::= [0-9]
```
## Analizador lexico
Esta definicion puede ser encontrada en el archivo [lenguaje.g4](lenguaje.g4).  
Se hace uso de la libreria [antlr4](https://www.antlr.org/) para generar el analizador lexico y sintactico.

## Analizador semantico
Para generar el analizador semantico, se debe ejecutar el comando 
