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
        4,0,3,31,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,4,2,26,8,2,11,2,12,
        2,27,1,2,1,2,0,0,3,1,1,3,2,5,3,1,0,1,3,0,9,10,13,13,32,32,31,0,1,
        1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,1,7,1,0,0,0,3,13,1,0,0,0,5,25,1,
        0,0,0,7,8,5,112,0,0,8,9,5,114,0,0,9,10,5,105,0,0,10,11,5,110,0,0,
        11,12,5,116,0,0,12,2,1,0,0,0,13,14,5,34,0,0,14,15,5,126,0,0,15,16,
        5,91,0,0,16,17,5,9,0,0,17,18,5,13,0,0,18,19,5,10,0,0,19,20,5,93,
        0,0,20,21,5,42,0,0,21,22,1,0,0,0,22,23,5,34,0,0,23,4,1,0,0,0,24,
        26,7,0,0,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,
        0,28,29,1,0,0,0,29,30,6,2,0,0,30,6,1,0,0,0,2,0,27,1,6,0,0
    ]

class Ejercicio6Lexer(Lexer):

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


