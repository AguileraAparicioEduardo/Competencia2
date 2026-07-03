grammar Ejercicio9;
//if (edad>17)
root : expr EOF;

expr : EOF;

IF: 'if';
IDT : [a-zA-Z]+;
NUM : [0-9]+;
MAYOR_QUE : '>';
PARENTESIS_OPEN : '(';
PARENTESIS_CLOSE : ')';
WS : [\r\t\n]+ ->skip;