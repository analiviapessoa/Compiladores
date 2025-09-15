# Generated from Arithmetic.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,61,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,1,
        1,1,2,1,2,1,3,1,3,1,4,4,4,35,8,4,11,4,12,4,36,1,5,1,5,1,6,1,6,1,
        7,4,7,44,8,7,11,7,12,7,45,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,11,4,11,
        56,8,11,11,11,12,11,57,1,11,1,11,0,0,12,1,1,3,2,5,3,7,4,9,5,11,6,
        13,7,15,8,17,9,19,10,21,11,23,12,1,0,3,1,0,48,57,2,0,65,90,97,122,
        3,0,9,10,13,13,32,32,63,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,
        1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,
        1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,27,
        1,0,0,0,5,29,1,0,0,0,7,31,1,0,0,0,9,34,1,0,0,0,11,38,1,0,0,0,13,
        40,1,0,0,0,15,43,1,0,0,0,17,47,1,0,0,0,19,49,1,0,0,0,21,52,1,0,0,
        0,23,55,1,0,0,0,25,26,5,43,0,0,26,2,1,0,0,0,27,28,5,45,0,0,28,4,
        1,0,0,0,29,30,5,42,0,0,30,6,1,0,0,0,31,32,5,47,0,0,32,8,1,0,0,0,
        33,35,7,0,0,0,34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,0,0,36,37,1,
        0,0,0,37,10,1,0,0,0,38,39,5,40,0,0,39,12,1,0,0,0,40,41,5,41,0,0,
        41,14,1,0,0,0,42,44,7,1,0,0,43,42,1,0,0,0,44,45,1,0,0,0,45,43,1,
        0,0,0,45,46,1,0,0,0,46,16,1,0,0,0,47,48,5,61,0,0,48,18,1,0,0,0,49,
        50,5,42,0,0,50,51,5,42,0,0,51,20,1,0,0,0,52,53,5,37,0,0,53,22,1,
        0,0,0,54,56,7,2,0,0,55,54,1,0,0,0,56,57,1,0,0,0,57,55,1,0,0,0,57,
        58,1,0,0,0,58,59,1,0,0,0,59,60,6,11,0,0,60,24,1,0,0,0,4,0,36,45,
        57,1,6,0,0
    ]

class ArithmeticLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PLUS = 1
    MINUS = 2
    MUL = 3
    DIV = 4
    INT = 5
    LPAREN = 6
    RPAREN = 7
    VAR = 8
    ASSIGN = 9
    POW = 10
    MOD = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'='", "'**'", "'%'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "MINUS", "MUL", "DIV", "INT", "LPAREN", "RPAREN", "VAR", 
            "ASSIGN", "POW", "MOD", "WS" ]

    ruleNames = [ "PLUS", "MINUS", "MUL", "DIV", "INT", "LPAREN", "RPAREN", 
                  "VAR", "ASSIGN", "POW", "MOD", "WS" ]

    grammarFileName = "Arithmetic.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


