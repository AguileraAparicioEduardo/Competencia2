grammar Ejercicio7;

root : expr EOF;
expr : EOF;

INT: 'int';
IDT: [a-zA-Z]+;
NUM: [0-9]+;
ASG: '=';
WS: [\r\t\n]+ ->skip;