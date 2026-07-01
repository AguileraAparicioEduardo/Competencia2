# Generated from ./if.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,46,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,4,
        3,30,8,3,11,3,12,3,31,1,4,1,4,1,5,1,5,1,5,1,5,1,5,4,5,41,8,5,11,
        5,12,5,42,1,5,1,5,0,0,6,1,1,3,2,5,3,7,4,9,5,11,6,1,0,1,1,0,48,57,
        47,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,
        11,1,0,0,0,1,13,1,0,0,0,3,16,1,0,0,0,5,26,1,0,0,0,7,29,1,0,0,0,9,
        33,1,0,0,0,11,40,1,0,0,0,13,14,5,105,0,0,14,15,5,102,0,0,15,2,1,
        0,0,0,16,17,5,91,0,0,17,18,5,65,0,0,18,19,5,45,0,0,19,20,5,90,0,
        0,20,21,5,97,0,0,21,22,5,45,0,0,22,23,5,122,0,0,23,24,5,93,0,0,24,
        25,5,43,0,0,25,4,1,0,0,0,26,27,5,62,0,0,27,6,1,0,0,0,28,30,7,0,0,
        0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,8,1,
        0,0,0,33,34,5,43,0,0,34,10,1,0,0,0,35,36,5,91,0,0,36,37,5,10,0,0,
        37,38,5,13,0,0,38,39,5,9,0,0,39,41,5,93,0,0,40,35,1,0,0,0,41,42,
        1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,44,1,0,0,0,44,45,6,5,0,0,
        45,12,1,0,0,0,3,0,31,42,1,6,0,0
    ]

class ifLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    IDT = 2
    MAYOR_QUE = 3
    NUM = 4
    MAS = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'[A-Za-z]+'", "'>'", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "IDT", "MAYOR_QUE", "NUM", "MAS", "WS" ]

    ruleNames = [ "IF", "IDT", "MAYOR_QUE", "NUM", "MAS", "WS" ]

    grammarFileName = "if.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


