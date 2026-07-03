# Generated from ./Ejercicio7.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,32,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        0,1,0,1,1,4,1,17,8,1,11,1,12,1,18,1,2,4,2,22,8,2,11,2,12,2,23,1,
        3,1,3,1,4,4,4,29,8,4,11,4,12,4,30,0,0,5,1,1,3,2,5,3,7,4,9,5,1,0,
        3,2,0,65,90,97,122,1,0,48,57,2,0,9,10,13,13,34,0,1,1,0,0,0,0,3,1,
        0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,3,16,1,0,
        0,0,5,21,1,0,0,0,7,25,1,0,0,0,9,28,1,0,0,0,11,12,5,105,0,0,12,13,
        5,110,0,0,13,14,5,116,0,0,14,2,1,0,0,0,15,17,7,0,0,0,16,15,1,0,0,
        0,17,18,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,4,1,0,0,0,20,22,7,
        1,0,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,
        6,1,0,0,0,25,26,5,61,0,0,26,8,1,0,0,0,27,29,7,2,0,0,28,27,1,0,0,
        0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,10,1,0,0,0,4,0,18,
        23,30,0
    ]

class Ejercicio7Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    IDT = 2
    NUM = 3
    ASG = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "INT", "IDT", "NUM", "ASG", "WS" ]

    ruleNames = [ "INT", "IDT", "NUM", "ASG", "WS" ]

    grammarFileName = "Ejercicio7.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


