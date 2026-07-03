# Generated from ./Ejercicio4.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,33,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        0,1,1,4,1,16,8,1,11,1,12,1,17,1,2,4,2,21,8,2,11,2,12,2,22,1,3,1,
        3,1,4,4,4,28,8,4,11,4,12,4,29,1,4,1,4,0,0,5,1,1,3,2,5,3,7,4,9,5,
        1,0,3,2,0,65,90,97,122,1,0,48,57,2,0,9,10,13,13,35,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,3,15,
        1,0,0,0,5,20,1,0,0,0,7,24,1,0,0,0,9,27,1,0,0,0,11,12,5,105,0,0,12,
        13,5,102,0,0,13,2,1,0,0,0,14,16,7,0,0,0,15,14,1,0,0,0,16,17,1,0,
        0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,4,1,0,0,0,19,21,7,1,0,0,20,19,
        1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,6,1,0,0,0,24,
        25,5,62,0,0,25,8,1,0,0,0,26,28,7,2,0,0,27,26,1,0,0,0,28,29,1,0,0,
        0,29,27,1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,32,6,4,0,0,32,10,
        1,0,0,0,4,0,17,22,29,1,6,0,0
    ]

class Ejercicio4Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    IDT = 2
    NUM = 3
    MAYOR_QUE = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'>'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "IDT", "NUM", "MAYOR_QUE", "WS" ]

    ruleNames = [ "IF", "IDT", "NUM", "MAYOR_QUE", "WS" ]

    grammarFileName = "Ejercicio4.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


