from antlr4 import *

from Ejercicio10Lexer import Ejercicio10Lexer
import sys

input_stream = FileStream(sys.argv[1], encoding="utf-8")

lexer = Ejercicio10Lexer(input_stream)

tokens = CommonTokenStream(lexer)
tokens.fill()

print(tokens)

for token in tokens.tokens:
    print("Texto ", token.text)
    print("Tipo ", token.type)
    print("Linea ", token.line)
    print("columna ", token.column)
    nombre_token = lexer.symbolicNames[token.type]

    print("Nombre del token: ", nombre_token)

    print("---------------------")