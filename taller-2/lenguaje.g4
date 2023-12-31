grammar lenguaje;

programa: sentencia* EOF;

declaracionVariable: 'var' identificador tipo? ('=' (expresion | expresionArray))?;

tipo: 'int' | 'float' | 'string' | 'bool' | array;

array: '['expresion']' array* tipo;

declaracionFuncion:
	'func' identificador '(' listaParametros ')' (tipo)? bloque;

listaParametros: parametro (',' parametro)* |;

parametro: identificador tipo;

bloque: '{' sentencia* '}';

sentencia:
	declaracionVariable
	| declaracionFuncion
	| asignacion
	| condicional
	| cicloFor
	| llamadaFuncion
	| modificacion
	| retorno
	| expresion
	| buildInFunction;

buildInFunction: print | linearRegression | plot | trigonometricFunctions | matrixFuctions;

print: 'print' '(' expresion ')';

linearRegression: 'linearRegression' '(' expresion ')';

plot: 'plot' '(' expresion ')';

trigonometricFunctions: trigonometricFunction '(' expresion ')';

trigonometricFunction: 'sin' | 'cos' | 'tan' | 'asin' | 'acos' | 'atan';

matrixFuctions: matrixFunction '(' expresion (',' expresion)* ')';

matrixFunction: 'matrixSuma' | 'matrixResta' | 'matrixMultiplicacion' | 'matrixTranspuesta' | 'matrixInversa';

asignacion: (identificador ('=' expresion)?) | (identificador accesoArray ('=' expresion)?);

condicional: 'if' comparacion bloque ('else' bloque)?;

comparacion: expresion ((operadorComparacion|operadorBoolean) expresion)*;

operadorComparacion: '==' | '!=' | '<' | '>' | '<=' | '>=';

operadorBoolean: 'and' | 'or';

operadorAritmetico: '+' | '-' | '*' | '/' | '^' | '%';

modificacion:
	identificador accesoArray? (operadorModificadorSimple | (operadorModificadorCompuesto (identificador| expresion)));

operadorModificadorSimple: '++' | '--';

operadorModificadorCompuesto:
	'+='
	| '-='
	| '*='
	| '/='
	| '^='
	| '%=';

cicloFor:
	'for' declaracionVariable ';' comparacion ';' modificacion bloque;

llamadaFuncion: identificador '(' listaArgumentos ')';

listaArgumentos: expresion (',' expresion)* |;

retorno: 'return' expresion?;

expresion:
	llamadaFuncion
	| termino (operadorAritmetico termino)*
	| expresionArray
	| trigonometricFunctions
	| matrixFuctions;

expresionArray:'{' expresion (',' expresion)* '}';

accesoArray:  ('[' expresion ']')*;

termino:
	identificador
	| identificador accesoArray
	| entero
	| decimal
	| CADENA
	| booleanos
	| '(' expresion ')';

booleanos: 'true' | 'false';

identificador: LETRA (LETRA | DIGITO)*;

entero: DIGITO+;

decimal: entero '.' entero;

CADENA: '"' .*? '"';

LETRA: [a-zA-Z];

DIGITO: [0-9];

WS: [ \t\r\n]+ -> skip;
