# Generated from ./Ejercicio2.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,4,29,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,1,4,1,13,
        8,1,11,1,12,1,14,1,2,1,2,1,3,1,3,1,3,1,3,1,3,4,3,24,8,3,11,3,12,
        3,25,1,3,1,3,0,0,4,1,1,3,2,5,3,7,4,1,0,2,3,0,32,32,65,90,97,122,
        1,0,48,57,30,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,1,9,
        1,0,0,0,3,12,1,0,0,0,5,16,1,0,0,0,7,23,1,0,0,0,9,10,7,0,0,0,10,2,
        1,0,0,0,11,13,7,1,0,0,12,11,1,0,0,0,13,14,1,0,0,0,14,12,1,0,0,0,
        14,15,1,0,0,0,15,4,1,0,0,0,16,17,5,45,0,0,17,6,1,0,0,0,18,19,5,91,
        0,0,19,20,5,10,0,0,20,21,5,13,0,0,21,22,5,9,0,0,22,24,5,93,0,0,23,
        18,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,
        0,27,28,6,3,0,0,28,8,1,0,0,0,3,0,14,25,1,6,0,0
    ]

class Ejercicio2Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDT = 1
    NUM = 2
    SUB = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'-'" ]

    symbolicNames = [ "<INVALID>",
            "IDT", "NUM", "SUB", "WS" ]

    ruleNames = [ "IDT", "NUM", "SUB", "WS" ]

    grammarFileName = "Ejercicio2.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


