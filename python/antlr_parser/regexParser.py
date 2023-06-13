# Generated from regex.g4 by ANTLR 4.12.0
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
        4,1,26,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,5,0,38,8,0,10,0,12,0,41,
        9,0,1,1,4,1,44,8,1,11,1,12,1,45,1,2,1,2,3,2,50,8,2,1,3,1,3,3,3,54,
        8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,67,8,6,1,7,1,
        7,3,7,71,8,7,1,7,4,7,74,8,7,11,7,12,7,75,1,7,1,7,1,8,1,8,1,9,1,9,
        1,9,3,9,85,8,9,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,3,12,95,8,
        12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,16,0,0,17,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,0,4,1,0,11,16,1,0,17,19,3,0,
        4,4,7,7,24,26,4,0,1,5,8,10,17,20,23,26,99,0,34,1,0,0,0,2,43,1,0,
        0,0,4,47,1,0,0,0,6,53,1,0,0,0,8,55,1,0,0,0,10,59,1,0,0,0,12,66,1,
        0,0,0,14,68,1,0,0,0,16,79,1,0,0,0,18,84,1,0,0,0,20,86,1,0,0,0,22,
        90,1,0,0,0,24,92,1,0,0,0,26,96,1,0,0,0,28,98,1,0,0,0,30,100,1,0,
        0,0,32,102,1,0,0,0,34,39,3,2,1,0,35,36,5,1,0,0,36,38,3,2,1,0,37,
        35,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,1,1,0,0,
        0,41,39,1,0,0,0,42,44,3,4,2,0,43,42,1,0,0,0,44,45,1,0,0,0,45,43,
        1,0,0,0,45,46,1,0,0,0,46,3,1,0,0,0,47,49,3,6,3,0,48,50,3,24,12,0,
        49,48,1,0,0,0,49,50,1,0,0,0,50,5,1,0,0,0,51,54,3,12,6,0,52,54,3,
        8,4,0,53,51,1,0,0,0,53,52,1,0,0,0,54,7,1,0,0,0,55,56,5,2,0,0,56,
        57,3,0,0,0,57,58,5,3,0,0,58,9,1,0,0,0,59,60,5,19,0,0,60,61,5,4,0,
        0,61,11,1,0,0,0,62,67,3,30,15,0,63,67,3,22,11,0,64,67,5,10,0,0,65,
        67,3,14,7,0,66,62,1,0,0,0,66,63,1,0,0,0,66,64,1,0,0,0,66,65,1,0,
        0,0,67,13,1,0,0,0,68,70,5,5,0,0,69,71,3,16,8,0,70,69,1,0,0,0,70,
        71,1,0,0,0,71,73,1,0,0,0,72,74,3,18,9,0,73,72,1,0,0,0,74,75,1,0,
        0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,78,5,6,0,0,78,15,
        1,0,0,0,79,80,5,20,0,0,80,17,1,0,0,0,81,85,3,32,16,0,82,85,3,22,
        11,0,83,85,3,20,10,0,84,81,1,0,0,0,84,82,1,0,0,0,84,83,1,0,0,0,85,
        19,1,0,0,0,86,87,3,32,16,0,87,88,5,7,0,0,88,89,3,32,16,0,89,21,1,
        0,0,0,90,91,7,0,0,0,91,23,1,0,0,0,92,94,3,28,14,0,93,95,3,26,13,
        0,94,93,1,0,0,0,94,95,1,0,0,0,95,25,1,0,0,0,96,97,5,19,0,0,97,27,
        1,0,0,0,98,99,7,1,0,0,99,29,1,0,0,0,100,101,7,2,0,0,101,31,1,0,0,
        0,102,103,7,3,0,0,103,33,1,0,0,0,9,39,45,49,53,66,70,75,84,94
    ]

class regexParser ( Parser ):

    grammarFileName = "regex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "'('", "')'", "':'", "'['", "']'", 
                     "'-'", "'{'", "'}'", "'.'", "'\\w'", "'\\W'", "'\\d'", 
                     "'\\D'", "'\\s'", "'\\S'", "'*'", "'+'", "'?'", "'^'", 
                     "'\\b'", "'\\B'", "'$'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "AnyCharacter", "CharacterClassAnyWord", 
                      "CharacterClassAnyWordInverted", "CharacterClassAnyDecimalDigit", 
                      "CharacterClassAnyDecimalDigitInverted", "CharacterClassAnyBlank", 
                      "CharacterClassAnyBlankInverted", "ZeroOrMoreQuantifier", 
                      "OneOrMoreQuantifier", "ZeroOrOneQuantifier", "AnchorStartOfString", 
                      "AnchorWordBoundary", "AnchorNonWordBoundary", "AnchorEndOfString", 
                      "EscapedChar", "Digit", "Char" ]

    RULE_regex = 0
    RULE_expression = 1
    RULE_expressionItem = 2
    RULE_normalItem = 3
    RULE_group = 4
    RULE_groupNonCapturingModifier = 5
    RULE_single = 6
    RULE_characterGroup = 7
    RULE_characterGroupNegativeModifier = 8
    RULE_characterGroupItem = 9
    RULE_characterRange = 10
    RULE_characterClass = 11
    RULE_quantifier = 12
    RULE_lazyModifier = 13
    RULE_quantifierType = 14
    RULE_char = 15
    RULE_charInGroup = 16

    ruleNames =  [ "regex", "expression", "expressionItem", "normalItem", 
                   "group", "groupNonCapturingModifier", "single", "characterGroup", 
                   "characterGroupNegativeModifier", "characterGroupItem", 
                   "characterRange", "characterClass", "quantifier", "lazyModifier", 
                   "quantifierType", "char", "charInGroup" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    AnyCharacter=10
    CharacterClassAnyWord=11
    CharacterClassAnyWordInverted=12
    CharacterClassAnyDecimalDigit=13
    CharacterClassAnyDecimalDigitInverted=14
    CharacterClassAnyBlank=15
    CharacterClassAnyBlankInverted=16
    ZeroOrMoreQuantifier=17
    OneOrMoreQuantifier=18
    ZeroOrOneQuantifier=19
    AnchorStartOfString=20
    AnchorWordBoundary=21
    AnchorNonWordBoundary=22
    AnchorEndOfString=23
    EscapedChar=24
    Digit=25
    Char=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RegexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(regexParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(regexParser.ExpressionContext,i)


        def getRuleIndex(self):
            return regexParser.RULE_regex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegex" ):
                listener.enterRegex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegex" ):
                listener.exitRegex(self)




    def regex(self):

        localctx = regexParser.RegexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_regex)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.expression()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 35
                self.match(regexParser.T__0)
                self.state = 36
                self.expression()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(regexParser.ExpressionItemContext)
            else:
                return self.getTypedRuleContext(regexParser.ExpressionItemContext,i)


        def getRuleIndex(self):
            return regexParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = regexParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 42
                self.expressionItem()
                self.state = 45 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 117570740) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normalItem(self):
            return self.getTypedRuleContext(regexParser.NormalItemContext,0)


        def quantifier(self):
            return self.getTypedRuleContext(regexParser.QuantifierContext,0)


        def getRuleIndex(self):
            return regexParser.RULE_expressionItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionItem" ):
                listener.enterExpressionItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionItem" ):
                listener.exitExpressionItem(self)




    def expressionItem(self):

        localctx = regexParser.ExpressionItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expressionItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.normalItem()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0):
                self.state = 48
                self.quantifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single(self):
            return self.getTypedRuleContext(regexParser.SingleContext,0)


        def group(self):
            return self.getTypedRuleContext(regexParser.GroupContext,0)


        def getRuleIndex(self):
            return regexParser.RULE_normalItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalItem" ):
                listener.enterNormalItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalItem" ):
                listener.exitNormalItem(self)




    def normalItem(self):

        localctx = regexParser.NormalItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_normalItem)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 7, 10, 11, 12, 13, 14, 15, 16, 24, 25, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.single()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.group()
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


    class GroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def regex(self):
            return self.getTypedRuleContext(regexParser.RegexContext,0)


        def getRuleIndex(self):
            return regexParser.RULE_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup" ):
                listener.enterGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup" ):
                listener.exitGroup(self)




    def group(self):

        localctx = regexParser.GroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(regexParser.T__1)
            self.state = 56
            self.regex()
            self.state = 57
            self.match(regexParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupNonCapturingModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZeroOrOneQuantifier(self):
            return self.getToken(regexParser.ZeroOrOneQuantifier, 0)

        def getRuleIndex(self):
            return regexParser.RULE_groupNonCapturingModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroupNonCapturingModifier" ):
                listener.enterGroupNonCapturingModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroupNonCapturingModifier" ):
                listener.exitGroupNonCapturingModifier(self)




    def groupNonCapturingModifier(self):

        localctx = regexParser.GroupNonCapturingModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_groupNonCapturingModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(regexParser.ZeroOrOneQuantifier)
            self.state = 60
            self.match(regexParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def char(self):
            return self.getTypedRuleContext(regexParser.CharContext,0)


        def characterClass(self):
            return self.getTypedRuleContext(regexParser.CharacterClassContext,0)


        def AnyCharacter(self):
            return self.getToken(regexParser.AnyCharacter, 0)

        def characterGroup(self):
            return self.getTypedRuleContext(regexParser.CharacterGroupContext,0)


        def getRuleIndex(self):
            return regexParser.RULE_single

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle" ):
                listener.enterSingle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle" ):
                listener.exitSingle(self)




    def single(self):

        localctx = regexParser.SingleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_single)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 7, 24, 25, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.char()
                pass
            elif token in [11, 12, 13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.characterClass()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.match(regexParser.AnyCharacter)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.characterGroup()
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


    class CharacterGroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def characterGroupNegativeModifier(self):
            return self.getTypedRuleContext(regexParser.CharacterGroupNegativeModifierContext,0)


        def characterGroupItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(regexParser.CharacterGroupItemContext)
            else:
                return self.getTypedRuleContext(regexParser.CharacterGroupItemContext,i)


        def getRuleIndex(self):
            return regexParser.RULE_characterGroup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharacterGroup" ):
                listener.enterCharacterGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharacterGroup" ):
                listener.exitCharacterGroup(self)




    def characterGroup(self):

        localctx = regexParser.CharacterGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_characterGroup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(regexParser.T__4)
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 69
                self.characterGroupNegativeModifier()


            self.state = 73 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self.characterGroupItem()
                self.state = 75 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 127926078) != 0)):
                    break

            self.state = 77
            self.match(regexParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharacterGroupNegativeModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AnchorStartOfString(self):
            return self.getToken(regexParser.AnchorStartOfString, 0)

        def getRuleIndex(self):
            return regexParser.RULE_characterGroupNegativeModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharacterGroupNegativeModifier" ):
                listener.enterCharacterGroupNegativeModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharacterGroupNegativeModifier" ):
                listener.exitCharacterGroupNegativeModifier(self)




    def characterGroupNegativeModifier(self):

        localctx = regexParser.CharacterGroupNegativeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_characterGroupNegativeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(regexParser.AnchorStartOfString)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharacterGroupItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def charInGroup(self):
            return self.getTypedRuleContext(regexParser.CharInGroupContext,0)


        def characterClass(self):
            return self.getTypedRuleContext(regexParser.CharacterClassContext,0)


        def characterRange(self):
            return self.getTypedRuleContext(regexParser.CharacterRangeContext,0)


        def getRuleIndex(self):
            return regexParser.RULE_characterGroupItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharacterGroupItem" ):
                listener.enterCharacterGroupItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharacterGroupItem" ):
                listener.exitCharacterGroupItem(self)




    def characterGroupItem(self):

        localctx = regexParser.CharacterGroupItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_characterGroupItem)
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.charInGroup()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.characterClass()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.characterRange()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharacterRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def charInGroup(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(regexParser.CharInGroupContext)
            else:
                return self.getTypedRuleContext(regexParser.CharInGroupContext,i)


        def getRuleIndex(self):
            return regexParser.RULE_characterRange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharacterRange" ):
                listener.enterCharacterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharacterRange" ):
                listener.exitCharacterRange(self)




    def characterRange(self):

        localctx = regexParser.CharacterRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_characterRange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.charInGroup()
            self.state = 87
            self.match(regexParser.T__6)
            self.state = 88
            self.charInGroup()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharacterClassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CharacterClassAnyWord(self):
            return self.getToken(regexParser.CharacterClassAnyWord, 0)

        def CharacterClassAnyWordInverted(self):
            return self.getToken(regexParser.CharacterClassAnyWordInverted, 0)

        def CharacterClassAnyDecimalDigit(self):
            return self.getToken(regexParser.CharacterClassAnyDecimalDigit, 0)

        def CharacterClassAnyDecimalDigitInverted(self):
            return self.getToken(regexParser.CharacterClassAnyDecimalDigitInverted, 0)

        def CharacterClassAnyBlank(self):
            return self.getToken(regexParser.CharacterClassAnyBlank, 0)

        def CharacterClassAnyBlankInverted(self):
            return self.getToken(regexParser.CharacterClassAnyBlankInverted, 0)

        def getRuleIndex(self):
            return regexParser.RULE_characterClass

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharacterClass" ):
                listener.enterCharacterClass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharacterClass" ):
                listener.exitCharacterClass(self)




    def characterClass(self):

        localctx = regexParser.CharacterClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_characterClass)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 129024) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quantifierType(self):
            return self.getTypedRuleContext(regexParser.QuantifierTypeContext,0)


        def lazyModifier(self):
            return self.getTypedRuleContext(regexParser.LazyModifierContext,0)


        def getRuleIndex(self):
            return regexParser.RULE_quantifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantifier" ):
                listener.enterQuantifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantifier" ):
                listener.exitQuantifier(self)




    def quantifier(self):

        localctx = regexParser.QuantifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_quantifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.quantifierType()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 93
                self.lazyModifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LazyModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZeroOrOneQuantifier(self):
            return self.getToken(regexParser.ZeroOrOneQuantifier, 0)

        def getRuleIndex(self):
            return regexParser.RULE_lazyModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLazyModifier" ):
                listener.enterLazyModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLazyModifier" ):
                listener.exitLazyModifier(self)




    def lazyModifier(self):

        localctx = regexParser.LazyModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_lazyModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(regexParser.ZeroOrOneQuantifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantifierTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZeroOrMoreQuantifier(self):
            return self.getToken(regexParser.ZeroOrMoreQuantifier, 0)

        def OneOrMoreQuantifier(self):
            return self.getToken(regexParser.OneOrMoreQuantifier, 0)

        def ZeroOrOneQuantifier(self):
            return self.getToken(regexParser.ZeroOrOneQuantifier, 0)

        def getRuleIndex(self):
            return regexParser.RULE_quantifierType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantifierType" ):
                listener.enterQuantifierType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantifierType" ):
                listener.exitQuantifierType(self)




    def quantifierType(self):

        localctx = regexParser.QuantifierTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_quantifierType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EscapedChar(self):
            return self.getToken(regexParser.EscapedChar, 0)

        def Digit(self):
            return self.getToken(regexParser.Digit, 0)

        def Char(self):
            return self.getToken(regexParser.Char, 0)

        def getRuleIndex(self):
            return regexParser.RULE_char

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar" ):
                listener.enterChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar" ):
                listener.exitChar(self)




    def char(self):

        localctx = regexParser.CharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_char)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117440656) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharInGroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EscapedChar(self):
            return self.getToken(regexParser.EscapedChar, 0)

        def Digit(self):
            return self.getToken(regexParser.Digit, 0)

        def Char(self):
            return self.getToken(regexParser.Char, 0)

        def AnyCharacter(self):
            return self.getToken(regexParser.AnyCharacter, 0)

        def AnchorStartOfString(self):
            return self.getToken(regexParser.AnchorStartOfString, 0)

        def AnchorEndOfString(self):
            return self.getToken(regexParser.AnchorEndOfString, 0)

        def ZeroOrMoreQuantifier(self):
            return self.getToken(regexParser.ZeroOrMoreQuantifier, 0)

        def OneOrMoreQuantifier(self):
            return self.getToken(regexParser.OneOrMoreQuantifier, 0)

        def ZeroOrOneQuantifier(self):
            return self.getToken(regexParser.ZeroOrOneQuantifier, 0)

        def getRuleIndex(self):
            return regexParser.RULE_charInGroup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharInGroup" ):
                listener.enterCharInGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharInGroup" ):
                listener.exitCharInGroup(self)




    def charInGroup(self):

        localctx = regexParser.CharInGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_charInGroup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 127797054) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





