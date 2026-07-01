grammar if;

root : expr EOF;

//expr: expr MAS expr | NUM;

expr: EOF;

IF: 'if';
IDT: '[A-Za-z]+';
MAYOR_QUE: '>';
NUM: [0-9]+;
MAS: '+';
WS : '[\n\r\t]'+ -> skip;