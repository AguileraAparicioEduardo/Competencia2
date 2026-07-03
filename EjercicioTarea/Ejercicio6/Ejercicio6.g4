grammar Ejercicio6;

root : expr EOF;
expr : EOF;

NUM: [0-9]+;
SUM: '+';
MULT: '*';
WS: [\r\t\n]+ ->skip;