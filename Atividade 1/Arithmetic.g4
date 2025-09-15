grammar Arithmetic;

// Regras do Parser
program: statement+ ;
statement: assignment | expr ;
assignment: VAR ASSIGN expr ;
expr: term ( (PLUS | MINUS) term )* ;
term: factor ( (MUL | DIV | MOD) factor )* ;
factor: base (POW factor)? ;
base: INT | VAR | LPAREN expr RPAREN ;

// Regras do Lexer
PLUS: '+' ;
MINUS: '-' ;
MUL: '*' ;
DIV: '/' ;
INT: [0-9]+ ;
LPAREN: '(' ;
RPAREN: ')' ;
VAR: [a-zA-Z]+ ;
ASSIGN: '=' ;
POW: '**';
MOD: '%';
WS: [ \t\r\n]+ -> skip ;