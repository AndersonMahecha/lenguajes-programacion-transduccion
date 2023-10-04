

grammar lenguaje;

programa: declaracion* | sentencia* EOF;

declaracion: declaracionVariable | declaracionFuncion;

declaracionVariable: 'var' identificador tipo? ('=' (expresion | inicializacionArray))?;

tipo: 'int' | 'float' | 'string' | 'bool' | array;

array: '['expresion']' array* tipo;

declaracionFuncion:
	'func' identificador '(' listaParametros ')' (tipo)? bloque;

listaParametros: parametro (',' parametro)* |;

parametro: identificador tipo;

bloque: '{' sentencia* '}';

sentencia:
	declaracionVariable
	| asignacion
	| condicional
	| cicloFor
	| llamadaFuncion
	| modificacion
	| retorno;

asignacion: (identificador ('=' expresion)?) | (identificador accesoArray ('=' expresion)?);

condicional: 'if' comparacion bloque ('else' bloque)?;

comparacion: expresion (operadorComparacion expresion)*;

operadorComparacion: '==' | '!=' | '<' | '>' | '<=' | '>=';

operadorAritmetico: '+' | '-' | '*' | '/' | '^' | '%';

modificacion:
	identificador (
		operadorModificadorSimple
		| operadorModificadorCompuesto (
			identificador
			| expresion
		)
	);

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

inicializacionArray: array expresionArray;

accesoArray:  ('[' expresion ']')*;

termino: factor (('^' | '%') factor)*;

factor:
	identificador
	| identificador accesoArray
	| entero
	| decimal
	| CADENA
	| 'true'
	| 'false'
	| '(' expresion ')';

identificador: LETRA (LETRA | DIGITO)*;

entero: DIGITO+;

decimal: entero '.' entero;

CADENA: '"' .*? '"';

LETRA: [a-zA-Z];

DIGITO: [0-9];

WS: [ \t\r\n]+ -> skip;
