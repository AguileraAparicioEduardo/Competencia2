grammar Ejercicio10;

root : expr EOF;

expr : EOF;

PRINT: 'print';
CADENA: '"' (~["] | '\r' | '\n')* '"';
PARENTHESIS_OPEN : '(';
PARENTHESIS_CLOSE : ')';
SC : ';';
WS: [\r\t\n ]+ -> skip;