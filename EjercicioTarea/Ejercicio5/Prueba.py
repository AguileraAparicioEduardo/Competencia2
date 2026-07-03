from antlr4 import *

from Ejercicio5Lexer import Ejercicio5Lexer
import sys

input_stream = FileStream(sys.argv[1])

lexer = Ejercicio5Lexer(input_stream)

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