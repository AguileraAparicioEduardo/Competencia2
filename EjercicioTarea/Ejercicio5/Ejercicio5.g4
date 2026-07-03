grammar Ejercicio5;

root : expr EOF;

expr : EOF;

PRINT: 'print';
CADENA: '"'~[\t\r\n]*'"';
WS: [\r\t\n ]+ -> skip;