grammar Ejercicio4;
//if x>7
root : expr EOF;

expr : EOF;

IF: 'if';
IDT : [a-zA-Z]+;
NUM : [0-9]+;
MAYOR_QUE : '>';
WS : [\r\t\n]+ ->skip;