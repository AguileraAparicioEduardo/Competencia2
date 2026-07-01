grammar Ejercicio1;

root : expr EOF;

expr: EOF;

IDT: [a-z A-Z];
NUM: [0-9]+;
MAS: '+';
WS : '[\n\r\t]'+ -> skip;