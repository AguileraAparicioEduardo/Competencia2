grammar Ejercicio8;

root : expr EOF;
expr : EOF;

IDT : [a-zA-Z]+;
NUM : [0-9]+;
MR_EQ : '>=';
WS: [\r\t\n]+ ->skip;
