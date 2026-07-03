# Generated from ./Ejercicio8.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,4,29,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,11,8,0,11,
        0,12,0,12,1,1,4,1,16,8,1,11,1,12,1,17,1,2,1,2,1,2,1,3,4,3,24,8,3,
        11,3,12,3,25,1,3,1,3,0,0,4,1,1,3,2,5,3,7,4,1,0,3,2,0,65,90,97,122,
        1,0,48,57,2,0,9,10,13,13,31,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,1,10,1,0,0,0,3,15,1,0,0,0,5,19,1,0,0,0,7,23,1,0,0,0,
        9,11,7,0,0,0,10,9,1,0,0,0,11,12,1,0,0,0,12,10,1,0,0,0,12,13,1,0,
        0,0,13,2,1,0,0,0,14,16,7,1,0,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,
        1,0,0,0,17,18,1,0,0,0,18,4,1,0,0,0,19,20,5,62,0,0,20,21,5,61,0,0,
        21,6,1,0,0,0,22,24,7,2,0,0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,
        0,0,25,26,1,0,0,0,26,27,1,0,0,0,27,28,6,3,0,0,28,8,1,0,0,0,4,0,12,
        17,25,1,6,0,0
    ]

class Ejercicio8Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDT = 1
    NUM = 2
    MR_EQ = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'>='" ]

    symbolicNames = [ "<INVALID>",
            "IDT", "NUM", "MR_EQ", "WS" ]

    ruleNames = [ "IDT", "NUM", "MR_EQ", "WS" ]

    grammarFileName = "Ejercicio8.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


