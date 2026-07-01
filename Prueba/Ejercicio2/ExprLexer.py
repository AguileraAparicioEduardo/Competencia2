# Generated from ./Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,3,25,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,9,8,0,11,0,12,0,10,
        1,1,1,1,1,2,1,2,1,2,1,2,1,2,4,2,20,8,2,11,2,12,2,21,1,2,1,2,0,0,
        3,1,1,3,2,5,3,1,0,1,1,0,48,57,26,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,1,8,1,0,0,0,3,12,1,0,0,0,5,19,1,0,0,0,7,9,7,0,0,0,8,7,1,0,0,
        0,9,10,1,0,0,0,10,8,1,0,0,0,10,11,1,0,0,0,11,2,1,0,0,0,12,13,5,43,
        0,0,13,4,1,0,0,0,14,15,5,91,0,0,15,16,5,10,0,0,16,17,5,13,0,0,17,
        18,5,9,0,0,18,20,5,93,0,0,19,14,1,0,0,0,20,21,1,0,0,0,21,19,1,0,
        0,0,21,22,1,0,0,0,22,23,1,0,0,0,23,24,6,2,0,0,24,6,1,0,0,0,3,0,10,
        21,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUM = 1
    MAS = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "MAS", "WS" ]

    ruleNames = [ "NUM", "MAS", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


