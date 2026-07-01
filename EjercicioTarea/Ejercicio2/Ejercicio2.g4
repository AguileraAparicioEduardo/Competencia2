grammar Ejercicio2;

root : expr EOF;

expr : EOF;

IDT: [a-z A-Z];
NUM: [0-9]+;
SUB: '-';
WS : '[\n\r\t]'+ -> skip;

