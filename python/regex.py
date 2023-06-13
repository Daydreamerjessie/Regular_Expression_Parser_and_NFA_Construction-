#!/usr/bin/env python

import json
import sys
from typing import List

import antlr4.Token
from antlr4 import CommonTokenStream, InputStream

from antlr_parser.regexLexer import regexLexer
from antlr_parser.regexParser import regexParser
from nfa import NFA
from nfa import Rule

"""
本文件中已经定义好了一些类和函数，类内也已经定义好了一些成员变量和方法。不建议大家修改这些已经定义好的东西。
但是，为了实现功能，你可以自由地增加新的函数、类等，包括可以在已经定义好的类自由地添加新的成员变量和方法。

本文件可以直接作为python的入口点文件。
支持两种运行方式：
1、将输入文件的文件名作为唯一的命令行参数传入。
   例如: python regex.py ../cases/01.txt
2、若不传入任何参数，则程序将从stdin中读取输入。
"""
"""
在第二次实验中：
  - 保证正则表达式字符串和待操作的文本内容都仅包含ASCII字符，且不包含'\0'和换行符'\r' '\n'。
  - 要求支持的正则表达式文法为，随第二次实验下发的`regex.g4`中，所有未被注释的部分。
    - 即，本次不需要实现除了anchor、backreference、非捕获分组、区间次数限定符(rangeQualifier)
  - 只需要实现compile函数（将正则表达式编译为NFA），和match函数（返回串中第一个匹配结果）。
  - 不要求支持返回捕获分组（即你实现的match函数，返回只含一个元素的数组即可）。
  - 要求支持的特殊字符在`regex.g4`中均有列出。具体包括（如下一行列举的内容与`regex.g4`中的声明有冲突，请以`regex.g4`为准）：
    - \d \w \s \D \W \S .
  - 不需要支持任何正则表达式的修饰符。保证传给compile函数的flags参数永远为空串。
正则表达式中各种字符的具体定义可查看 https://www.runoob.com/regexp/regexp-metachar.html 
"""


class Regex:
    """
    表示一个正则表达式的类。
    """
    nfa: NFA  # 正则表达式所使用的NFA

    @staticmethod
    def parse(pattern: str) -> regexParser.RegexContext:
        """
        解析正则表达式的字符串，生成语法分析树。
        你应该在compile函数中调用一次本函数，以得到语法分析树。
        通常，你不需要改动此函数，也不需要理解此函数实现每一行的具体含义。
        但是，你应当对语法分析树的数据结构(RegexContext)有一定的理解，作业文档中有相关的教程可供参考。
        :param pattern 要解析的正则表达式的字符串
        :return regexParser.RegexContext类的对象
        """
        input_stream = InputStream(pattern)
        lexer = regexLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = regexParser(stream)
        tree = parser.regex()
        errCount = parser.getNumberOfSyntaxErrors()
        if errCount > 0: raise ValueError("parser解析失败，表达式中有" + str(errCount) + "个语法错误！")
        if stream.LA(1) != antlr4.Token.EOF: raise ValueError(
            "parser解析失败，解析过程未能到达字符串结尾，可能是由于表达式中间有无法解析的内容！已解析的部分：" +
            stream.getText(0, stream.index - 1))
        return tree

    def compile(self, pattern: str, flags="") -> None:
        """
        编译给定的正则表达式。
        具体包括两个过程：解析正则表达式得到语法分析树（这步已经为你写好，即parse方法），
        和在语法分析树上进行分析（遍历），构造出NFA（需要你完成的部分）。
        在语法分析树上进行分析的方法，可以是直接自行访问该树，也可以是使用antlr的Visitor机制，详见作业文档。
        你编译产生的结果，NFA应保存在self.nfa中，其他内容也建议保存在当前对象下。
        :param pattern 正则表达式的字符串
        :param flags 正则表达式的修饰符（第二次实验不要求支持，保证传入的永远是空串）
        """
        tree = Regex.parse(pattern)  # 这是语法分析树
        # TODO 请你完成这个函数
        # 你应该根据tree中的内容，恰当地构造NFA
        # 构造好的NFA，和其他数据变量（如有），均建议保存在当前对象中。
        # self.nfa = NFA()
        self.max_state = 1
        self.s = 0
        self.d = 1
        self._rule=[]
        self.stack=[] 
        self.neg = 0
        self.visitRegrex(tree)
        self.pattern = pattern
     

        self.txt = []
        self.txt.append("states: "+str(self.max_state))
        self.txt.append("final: 1")
        self.txt.append("rules:")
        # self._rule.sort()
        self.txt+=self._rule
        self.txt_data = '\n'.join(self.txt)
        print(self.txt_data)#这里打印出生成的NFA的文本形式，之后根据这个文本形式创建nfa
        self.nfa = NFA.from_text(self.txt_data)
        # self.nfa.exec("101010")

        # node = tree.expression(0)
        # node.children()
        # isinstance(node, RuleContext)
        # isinstance(node, TerminalNode)
        # rulenode.getRuleIndex()

    def visitRegrex(self,tree):
        x = self.d
        y = self.s
        self.d = self.max_state+1
        self.max_state+=1

        for i in tree.expression():  # 获取第一个 expression 节点
            self.visitExpression(i)
            self._rule.append(f"{self.s}->{x} \e")
            self.s = y
        self.s = x

    def visitExpression(self, node):
        for child in node.children:
            ruleNode = child
            if ruleNode.getRuleIndex() == regexParser.RULE_expressionItem:
                itemNode = ruleNode
                self.visitExpressionItem(itemNode)

    def visitExpressionItem(self, node):
        normalItemNode = node.normalItem()
        if normalItemNode:
            self.visitNormalItem(normalItemNode)

        quantifierNode = node.quantifier()
        if quantifierNode:
            self.visitQuantifier(quantifierNode)

    def visitNormalItem(self, node):
        # 处理 normalItem 节点的逻辑
        self.stack.append([node,self.s])
        singleNode = node.single()
        if singleNode:
            if singleNode.char():
                n=singleNode.char().Char()
                label = 0
                if n:
                    self._rule.append(f"{self.s}->{self.d} {n}")
                    label =1 
                n=singleNode.char().EscapedChar()
                if n:
                    self._rule.append(f"{self.s}->{self.d} {n}")
                    label = 1
                n=singleNode.char().Digit()
                if n:
                    self._rule.append(f"{self.s}->{self.d} {n}")
                    label = 1
                if not label:
                    self._rule.append(f"{self.s}->{self.d} {singleNode.char().getText()}")
                self.s=self.d
                self.d=self.max_state+1
                self.max_state+=1
                
                


            if singleNode.characterClass():
                n=singleNode.characterClass()
                if n.CharacterClassAnyWord():
                    self._rule.append(f"{self.s}->{self.d} {n.CharacterClassAnyWord()}")
                if n.CharacterClassAnyWordInverted():
                    self._rule.append(f"{self.s}->{self.d} {n.CharacterClassAnyWordInverted()}")
                if n.CharacterClassAnyDecimalDigit():
                    self._rule.append(f"{self.s}->{self.d} {n.CharacterClassAnyDecimalDigit()}")
                if n.CharacterClassAnyDecimalDigitInverted():
                    self._rule.append(f"{self.s}->{self.d} {n.CharacterClassAnyDecimalDigitInverted()}")
                if n.CharacterClassAnyBlank():
                    self._rule.append(f"{self.s}->{self.d} {n.CharacterClassAnyBlank()}")
                if n.CharacterClassAnyBlankInverted():
                    self._rule.append(f"{self.s}->{self.d} {n.CharacterClassAnyBlankInverted()}")
                self.s=self.d
                self.d=self.max_state+1
                self.max_state+=1
            if singleNode.AnyCharacter():
                self._rule.append(f"{self.s}->{self.d} \.")
                self.s=self.d
                self.d=self.max_state+1
                self.max_state+=1
            if singleNode.characterGroup():
                if singleNode.characterGroup().characterGroupNegativeModifier():
                    n=singleNode.characterGroup().characterGroupNegativeModifier().AnchorStartOfString()
                    if n:
                        self._rule.append(f"{self.s}->{self.d} \e")
                        self.neg =1
                    self.s=self.d
                    self.d=self.max_state+1
                    self.max_state+=1
                GroupItems = singleNode.characterGroup().characterGroupItem()
                for GroupItem in GroupItems :
                    if GroupItem.charInGroup():
                        n = GroupItem.charInGroup().EscapedChar()
                        did = 0
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}")
                            did =1
                        n = GroupItem.charInGroup().Digit()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}")
                            did =1
                        n = GroupItem.charInGroup().Char()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}")
                            did =1
                        n = GroupItem.charInGroup().AnyCharacter()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}")
                            did =1
                        n = GroupItem.charInGroup().AnchorStartOfString()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}")
                            did =1
                        n = GroupItem.charInGroup().AnchorEndOfString()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}")
                            did =1
                        n = GroupItem.charInGroup().ZeroOrMoreQuantifier()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}")
                            did =1
                        n = GroupItem.charInGroup().OneOrMoreQuantifier()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}")
                            did =1
                        n = GroupItem.charInGroup().ZeroOrOneQuantifier()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}")
                            did =1
                        if not did:
                            self._rule.append(f"{self.s}->{self.d} \{GroupItem.charInGroup().getText()}")
                            # print(1)1
                    if GroupItem.characterClass():
                        n= GroupItem.characterClass()
                        if n.CharacterClassAnyWord():
                            self._rule.append(f"{self.s}->{self.d} {n.CharacterClassAnyWord()}")
                        if n.CharacterClassAnyWordInverted():
                            self._rule.append(f"{self.s}->{self.d} {n.CharacterClassAnyWordInverted()}")
                        if n.CharacterClassAnyDecimalDigit():
                            self._rule.append(f"{self.s}->{self.d} {n.CharacterClassAnyDecimalDigit()}")
                        if n.CharacterClassAnyDecimalDigitInverted():
                            self._rule.append(f"{self.s}->{self.d} {n.CharacterClassAnyDecimalDigitInverted()}")
                        if n.CharacterClassAnyBlank():
                            self._rule.append(f"{self.s}->{self.d} {n.CharacterClassAnyBlank()}")
                        if n.CharacterClassAnyBlankInverted():
                            self._rule.append(f"{self.s}->{self.d} {n.CharacterClassAnyBlankInverted()}")
                    if GroupItem.characterRange():
                        m = GroupItem.characterRange().charInGroup(0)
                        t = GroupItem.characterRange().charInGroup(1)
                        n = m.EscapedChar()
                        z = t.EscapedChar()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}-{z}")
                        n = m.Digit()
                        z = t.Digit()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}-{z}")
                        n = m.Char()
                        z = t.Char()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}-{z}")
                        n = m.AnyCharacter()
                        z = t.AnyCharacter()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}-{z}")
                        n = m.AnchorStartOfString()
                        z = t.AnchorStartOfString()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}-{z}")
                        n = m.AnchorEndOfString()
                        z = t.AnchorEndOfString()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}-{z}")
                        n = m.ZeroOrMoreQuantifier()
                        z = t.ZeroOrMoreQuantifier()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}-{z}")
                        n = m.OneOrMoreQuantifier()
                        z = t.OneOrMoreQuantifier()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}-{z}")
                        n = m.ZeroOrOneQuantifier()
                        z = t.ZeroOrOneQuantifier()
                        if n:
                            self._rule.append(f"{self.s}->{self.d} {n}-{z}")
                    self.s=self.d
                    self.d=self.max_state+1
                    self.max_state+=1
                
        groupNode = node.group()
        if groupNode:
            self.visitRegrex(groupNode.regex())


    def visitQuantifier(self, node):
        # 处理 quantifier 节点的逻辑
        x = self.stack.pop()
        x=x[1]
        # print(x)
        TypeNode = node.quantifierType()
        if TypeNode:
            i = -1
            while(1):
                arrow_pos = self._rule[i].find("->")
                space_pos = self._rule[i].find(" ")
                s = int(self._rule[i][0:arrow_pos])
                d = int(self._rule[i][arrow_pos + 2:space_pos])
                content = self._rule[-1][space_pos + 1:]
                if s == x:
                    break
                i-=1
            # print(s)

            n = TypeNode.ZeroOrMoreQuantifier()
            if n:
                self._rule.append(f"{self.s}->{s} \e")
                self._rule.append(f"{s}->{self.s} \e")
            n = TypeNode.OneOrMoreQuantifier()
            if n:
                # if more
                self._rule.append(f"{self.s}->{s} \e")

            n = TypeNode.ZeroOrOneQuantifier()
            if n:
                self._rule.append(f"{s}->{self.s} \e")
            # self.s=self.d
            # self.d=self.max_state+1
            # self.max_state+=1
        LazyNode = node.lazyModifier()
        if LazyNode:
            n = LazyNode.ZeroOrOneQuantifier()
            i = -1
            while(1):
                arrow_pos = self._rule[i].find("->")
                space_pos = self._rule[i].find(" ")
                s = int(self._rule[i][0:arrow_pos])
                d = int(self._rule[i][arrow_pos + 2:space_pos])
                content = self._rule[-1][space_pos + 1:]
                if s == x:
                    break
                i-=1
            if n:
                self._rule.append(f"{s}->{self.s} \e")


    def match(self, text: str) -> List[str]:
        """
        在给定的输入文本上，进行正则表达式匹配，返回匹配到的第一个结果。
        匹配不成功时，返回空数组[]；
        匹配成功时，返回一个由字符串组成的数组，其中下标为0的元素是匹配到的字符串，
        下标为i(i>=1)的元素是匹配结果中的第i个分组。
        （第二次实验中不要求支持分组功能，返回的数组中只含一个元素即可）
        :param text 输入的文本
        :return 如上所述
        """
        # TODO 请你完成这个函数
        # print(text)
        if not len(text):
            return []
        result = self.nfa.exec(text)
        if not result:
            return self.match(text[1:])
        res=['']
        for i in result.consumes:
            res[0]+=i
        return res


if __name__ == '__main__':
    """
    程序入口点函数。已经帮你封装好了读取文本输入、调用compile方法和match等方法、输出结果等。
    一般来说，你不需要阅读和改动这里的代码，只需要完成上面Regex类中的标有TODO的函数即可。
    """
    if len(sys.argv) >= 2:
        with open(sys.argv[1], "r") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    type = ""
    pattern = None
    flags = ""
    input_str = None
    lines = text.splitlines(keepends=True)
    lenBeforeInputLine = 0
    for line in lines:
        if line.startswith("type:"):
            type = line[5:].strip()
        elif line.startswith("pattern: "):
            pattern = line.splitlines()[0][9:]  # 去掉结尾的换行符
        elif line.startswith("flags:"):
            flags = line[6:].strip()
        elif line.startswith("input: "):
            input_str = text[lenBeforeInputLine + 7:]
        lenBeforeInputLine += len(line)
    if pattern is None or input_str is None:
        raise ValueError("pattern或input未找到！注意pattern: 和input: ，冒号后面必须有空格！")

    if type == "find":
        regex = Regex()
        regex.compile(pattern, flags)
        matchRes = regex.match(input_str)
        # print(matchRes)
        print(json.dumps(matchRes))
    else:
        raise ValueError("不支持的输入文件类型！")
