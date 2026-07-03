# Generated from ./Ejercicio5.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,3,29,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,
        1,1,1,5,1,16,8,1,10,1,12,1,19,9,1,1,1,1,1,1,2,4,2,24,8,2,11,2,12,
        2,25,1,2,1,2,0,0,3,1,1,3,2,5,3,1,0,2,2,0,9,10,13,13,3,0,9,10,13,
        13,32,32,30,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,1,7,1,0,0,0,3,13,
        1,0,0,0,5,23,1,0,0,0,7,8,5,112,0,0,8,9,5,114,0,0,9,10,5,105,0,0,
        10,11,5,110,0,0,11,12,5,116,0,0,12,2,1,0,0,0,13,17,5,34,0,0,14,16,
        8,0,0,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,
        18,20,1,0,0,0,19,17,1,0,0,0,20,21,5,34,0,0,21,4,1,0,0,0,22,24,7,
        1,0,0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,
        27,1,0,0,0,27,28,6,2,0,0,28,6,1,0,0,0,3,0,17,25,1,6,0,0
    ]

class Ejercicio5Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PRINT = 1
    CADENA = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'print'" ]

    symbolicNames = [ "<INVALID>",
            "PRINT", "CADENA", "WS" ]

    ruleNames = [ "PRINT", "CADENA", "WS" ]

    grammarFileName = "Ejercicio5.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


