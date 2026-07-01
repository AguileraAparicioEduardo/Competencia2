grammar Ejercicio3;

root : expr EOF;

expr : EOF;

IDT : [a-z A-Z]+;
NUM : [0-9]+;
ASIG: '=';
WS: '[\r\t\n]'+ ->skip;