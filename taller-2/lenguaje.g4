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
	| buildInFunction;

buildInFunction: print | linearRegression;

print: 'print' '(' expresion ')';

linearRegression: 'linearRegression' '(' expresion ')';

asignacion: (identificador ('=' expresion)?) | (identificador accesoArray ('=' expresion)?);

condicional: 'if' comparacion bloque ('else' bloque)?;

comparacion: expresion (operadorComparacion expresion)*;

operadorComparacion: '==' | '!=' | '<' | '>' | '<=' | '>=';

operadorAritmetico: '+' | '-' | '*' | '/' | '^' | '%';

modificacion:
	(identificador accesoArray?) (operadorModificadorSimple |
	 operadorModificadorCompuesto (identificador| expresion));

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
	termino (operadorAritmetico termino)*
	| llamadaFuncion
	| expresionArray;

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
