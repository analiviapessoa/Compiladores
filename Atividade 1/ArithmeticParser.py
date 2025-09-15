# Generated from Arithmetic.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,57,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,5,3,31,8,3,10,3,12,3,34,9,3,1,4,1,4,1,4,5,4,39,8,4,10,
        4,12,4,42,9,4,1,5,1,5,1,5,3,5,47,8,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,
        55,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,2,1,0,1,2,2,0,3,4,11,11,56,0,
        15,1,0,0,0,2,21,1,0,0,0,4,23,1,0,0,0,6,27,1,0,0,0,8,35,1,0,0,0,10,
        43,1,0,0,0,12,54,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,
        0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,22,3,4,2,0,20,22,3,
        6,3,0,21,19,1,0,0,0,21,20,1,0,0,0,22,3,1,0,0,0,23,24,5,8,0,0,24,
        25,5,9,0,0,25,26,3,6,3,0,26,5,1,0,0,0,27,32,3,8,4,0,28,29,7,0,0,
        0,29,31,3,8,4,0,30,28,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,
        1,0,0,0,33,7,1,0,0,0,34,32,1,0,0,0,35,40,3,10,5,0,36,37,7,1,0,0,
        37,39,3,10,5,0,38,36,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,
        0,0,0,41,9,1,0,0,0,42,40,1,0,0,0,43,46,3,12,6,0,44,45,5,10,0,0,45,
        47,3,10,5,0,46,44,1,0,0,0,46,47,1,0,0,0,47,11,1,0,0,0,48,55,5,5,
        0,0,49,55,5,8,0,0,50,51,5,6,0,0,51,52,3,6,3,0,52,53,5,7,0,0,53,55,
        1,0,0,0,54,48,1,0,0,0,54,49,1,0,0,0,54,50,1,0,0,0,55,13,1,0,0,0,
        6,17,21,32,40,46,54
    ]

class ArithmeticParser ( Parser ):

    grammarFileName = "Arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "<INVALID>", 
                     "'('", "')'", "<INVALID>", "'='", "'**'", "'%'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "MUL", "DIV", "INT", 
                      "LPAREN", "RPAREN", "VAR", "ASSIGN", "POW", "MOD", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expr = 3
    RULE_term = 4
    RULE_factor = 5
    RULE_base = 6

    ruleNames =  [ "program", "statement", "assignment", "expr", "term", 
                   "factor", "base" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    MUL=3
    DIV=4
    INT=5
    LPAREN=6
    RPAREN=7
    VAR=8
    ASSIGN=9
    POW=10
    MOD=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.StatementContext,i)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ArithmeticParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 352) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(ArithmeticParser.AssignmentContext,0)


        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ArithmeticParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ArithmeticParser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(ArithmeticParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = ArithmeticParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(ArithmeticParser.VAR)
            self.state = 24
            self.match(ArithmeticParser.ASSIGN)
            self.state = 25
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.TermContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.PLUS)
            else:
                return self.getToken(ArithmeticParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.MINUS)
            else:
                return self.getToken(ArithmeticParser.MINUS, i)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ArithmeticParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.term()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 28
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 29
                self.term()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.FactorContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.MUL)
            else:
                return self.getToken(ArithmeticParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.DIV)
            else:
                return self.getToken(ArithmeticParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.MOD)
            else:
                return self.getToken(ArithmeticParser.MOD, i)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = ArithmeticParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.factor()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2072) != 0):
                self.state = 36
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2072) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 37
                self.factor()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def base(self):
            return self.getTypedRuleContext(ArithmeticParser.BaseContext,0)


        def POW(self):
            return self.getToken(ArithmeticParser.POW, 0)

        def factor(self):
            return self.getTypedRuleContext(ArithmeticParser.FactorContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = ArithmeticParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.base()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 44
                self.match(ArithmeticParser.POW)
                self.state = 45
                self.factor()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ArithmeticParser.INT, 0)

        def VAR(self):
            return self.getToken(ArithmeticParser.VAR, 0)

        def LPAREN(self):
            return self.getToken(ArithmeticParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ArithmeticParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase" ):
                listener.enterBase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase" ):
                listener.exitBase(self)




    def base(self):

        localctx = ArithmeticParser.BaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_base)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(ArithmeticParser.INT)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(ArithmeticParser.VAR)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.match(ArithmeticParser.LPAREN)
                self.state = 51
                self.expr()
                self.state = 52
                self.match(ArithmeticParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





