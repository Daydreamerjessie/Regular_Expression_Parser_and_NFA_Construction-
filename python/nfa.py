#!/usr/bin/env python

import sys
from enum import Enum
from typing import List, Optional

"""
本文件中已经定义好了一些类和函数，类内也已经定义好了一些成员变量和方法。不建议大家修改这些已经定义好的东西。
但是，为了实现功能，你可以自由地增加新的函数、类等，包括可以在已经定义好的类自由地添加新的成员变量和方法。

本文件可以直接作为python的入口点文件。
支持两种运行方式：
1、将输入文件的文件名作为唯一的命令行参数传入。
   例如: python nfa.py ../cases/01.txt
2、若不传入任何参数，则程序将从stdin中读取输入。
"""
"""
在第一次实验中，保证状态转移规则的字母和输入的字符串都仅包含ASCII字符。
第一次实验要求支持的特殊字符有：\d \w \s \D \W \S \. 
前六个的定义同一般正则表达式中的定义，最后一个\.则等同于一般正则表达式中的.，可匹配任何字符。
各个字符的具体定义可查看 https://www.runoob.com/regexp/regexp-metachar.html 
"""


class RuleType(Enum):
    """
    用于表示状态转移的类型的枚举。
    示例用法： if rule.type == RuleType.EPSILON:
    """
    NORMAL = 0  # 一般转移。如 a
    RANGE = 1  # 字符区间转移。如 a-z
    SPECIAL = 2  # 特殊转移。如 \d （注意Rule的by属性里面是没有斜杠的，只有一个字母如d）
    EPSILON = 3  # epsilon-转移。


class Rule:
    """
    表示一条状态转移规则。
    """
    dst: int  # 目的状态
    type: RuleType  # 状态转移的类型，详见RuleType的注释
    by: str = ""  # 对特殊字符转移，这里只有一个字母，如d；对字符区间转移，这里是区间的开头，如a；对一般转移，这里就是转移所需的字母；对epsilon-转移，这里固定为空串。
    to: str = ""  # 对字符区间转移，这里是区间的结尾，如z；对任何其他类型的转移，这里固定为空串。


class Path:
    """
    表示一条从初态到终态的路径。
    当输入字符串的执行结果是接受时，你需要根据接受的路径，正确构造一个该类的对象并返回。
    """
    states: List[int] = []  # 从初态到终态经历的状态列表。开头必须是0。
    consumes: List[str] = []  # 长度必须为states的长度-1。consumes[i]表示states[i]迁移到states[j]时所消耗的字母（若是不消耗字母的epsilon转移，则设为空串""即可）]

    def __str__(self):
        """
        将Path转为（序列化为）文本的表达格式（以便于通过stdout输出）
        你不需要理解此函数的含义、阅读此函数的实现和调用此函数。
        """
        result = ""
        if len(self.consumes) != len(self.states) - 1: raise AssertionError("Path的len(consumes)不等于len(states)-1！")
        for i in range(len(self.consumes)):
            result += str(self.states[i]) + " " + self.consumes[i] + " "
        result += str(self.states[-1])
        return result


class NFA:
    """
    表示一个NFA的类。
    本类定义的自动机，约定状态用编号0~(num_states-1)表示，初态固定为0。
    """
    num_states: int = 0  # 状态个数
    is_final: List[bool] = []  # 用于判断状态是否为终态的数组，长为num_states。is_final[i]为true表示状态i为终态。
    rules: List[List[Rule]] = []  # 表示所有状态转移规则的二维数组，长为num_states。rules[i]表示从状态i出发的所有转移规则。

    def exec(self, text: str) -> Optional[Path]:
        """
        在自动机上执行指定的输入字符串。
        :param text: 输入字符串
        :return: 若拒绝，返回None。若接受，返回一个Path类的对象。
        """
        # TODO 请你完成这个函数
        
        length =  len(text) # 字符串长度
        cur_state = set([0])  # 当前状态，为一个集合的形式，然后只要有可以转移的，就转移
        res = Path() # 返回Path

        # 先写一个list来装epsilon闭包，然后循环里不判断epsilon，最后，把同个epsilon闭包里的加到next_state里
        # 然后在最后的res，在逆向找路径的过程中，如果出现了找不到的情况，再去epsilon里找
        eps_list = set([1])
        for i in range(self.num_states):
            for rule in self.rules[i]:
                if rule.type == RuleType.EPSILON and rule.dst == 1:
                    eps_list.add(i)
                    # flag = True
                    # for eps_set in eps_list:
                        # if i in eps_set or rule.dst in eps_set:
                        # if i in eps_set:
                            # eps_set.add(i)
                            # eps_set.add(rule.dst)
                            # print(i,rule.dst,eps_set)
                            # flag = False
                            # break
                        
                    
                    # eps_list.append(set([i,rule.dst]))
        # print(eps_list)
        path_all = []
        i = 0
        label = 0
        f = 0
        while i < length:
            
            flag = False
            char = text[i]
            next_state = set()
            cur_trans = []
            f = 0

            # epsilon
            new_add = set()
            for cur_s in cur_state:
                for rule in self.rules[cur_s]:
                    if rule.type == RuleType.EPSILON:
                        new_add.add(rule.dst)

            #     for eps_set in eps_list:
            #         if cur_s in eps_set:
            #             new_add |= eps_set
            cur_state |= new_add

            for cur_s in cur_state:
                for rule in self.rules[cur_s]:

                    if rule.type == RuleType.NORMAL:
                        if char == rule.by:
                            next_state.add(rule.dst)
                            cur_trans.append([rule,cur_s,char])
                            flag = True
                    elif rule.type == RuleType.RANGE:
                        if rule.by <= char <= rule.to:
                            next_state.add(rule.dst)
                            cur_trans.append([rule,cur_s,char])
                            flag =True

                    elif rule.type == RuleType.SPECIAL:
                        if self.is_special(char,rule.by):
                            next_state.add(rule.dst)
                            cur_trans.append([rule,cur_s,char])
                            flag =True
                    # elif rule.type == RuleType.EPSILON:
                    #     next_state.add(rule.dst)
                        # cur_trans.append([rule,cur_s,""])
                    # lab2
                    # if rule.dst in eps_list:
                    #     label = 1
                    
            # lab2
            # if label ==1:
            #     break

            # if flag == False:
            #     return None
            
            i += 1
            # if cur_trans:
            cur_state = next_state
            new_add = set()
            for cur_s in cur_state:
                for rule in self.rules[cur_s]:
                    if rule.type == RuleType.EPSILON:
                        new_add.add(rule.dst)
            cur_state |= new_add
            # print(label,cur_state)
            if label ==0:
                for cur_s in cur_state:
                    if cur_s in eps_list:
                        label = 1
            # else:
            #     # print("zzxzxzx")
            #     for cur_s in cur_state:
            #         if cur_s in eps_list:
            #             f = 1
            #     if f==0:
            #         # print("qeqweqwe")
            #         break
            path_all.append(cur_trans)

        print(path_all)
        no_end_flag = True
        end_state = 1
        # print(text,cur_state)
        # epsilon

        # new_add = set()
        # for cur_s in cur_state:
        #     for eps_set in eps_list:
        #         if cur_s in eps_set:
        #             new_add |= eps_set
        # cur_state |= new_add

        # for i in cur_state:
        #     if self.is_final[i]:
        #         no_end_flag = False
        #         end_state = i
        # if no_end_flag:
        #     return None
        if label ==0:
            return None
        eps = []
        for _ in range(self.num_states):
            for i in range(self.num_states):
                eps.append(set([i]))

            for i in range(self.num_states):
                for rule in self.rules[i]:
                    if rule.type == RuleType.EPSILON:
                        eps[rule.dst]|=eps[i]
        # print(eps)
        # 把不需要的部分剪掉
        step = len(path_all)-1
        f=0
        while step >=0:
            for [rule,s,c] in path_all[step]:
                if rule.dst in eps[end_state]:
                    f =1
                    break
            if f==1:
                break
            step-=1

        path_all=path_all[:step+1]


        
        step = len(path_all)-1
        end_state = 1
        res.states.insert(0,1)
        while step >= 0:
            flag = True
            
            for [rule,s,c] in path_all[step]:
                
                print(rule.dst,end_state,eps[end_state])

                if end_state == rule.dst or rule.dst in eps[end_state]:
                    flag = False
                    res.states.insert(0,s)
                    res.consumes.insert(0,c)
                    end_state = s
                    break
            step -= 1
            # if flag:
            #     for [rule,s,c] in path_all[step]:
            #         for eps_set in eps_list:
            #             if rule.dst in eps_set and end_state in eps_set:
            #                 # 有可能不是一步转移 DFS遍历
            #                 # print(rule.dst,end_state)
            #                 e_path = self.find_epath(rule.dst,end_state)
                            
            #                 for item in e_path:
            #                     res.states.insert(0,item)
            #                     res.consumes.insert(0,"")
            #                 end_state = rule.dst                                                   
            #                 break # 有rule.dst 和 end_state在同一个eps_set里，不用再看其他rule了
    
        # if res.states[0] != 0:
        #     for eps_set in eps_list:
        #         if 0 in eps_set and res.states[0] in eps_set:
        #             e_path = self.find_epath(0,res.states[0])
        #             for item in e_path:
        #                 res.states.insert(0,item)
        #                 res.consumes.insert(0,"")  
                    # break
        return res

    def find_epath(self,start,end):
        # DFS
        # print(start,end)
        visited = set([start])
        path = [start]
        cur = start
        while cur != end:
            flag = True
            for rule in self.rules[cur]:
                if rule.type == RuleType.EPSILON and rule.dst not in visited:
                    path.append(rule.dst)
                    cur = rule.dst
                    visited.add(cur)
                    flag = False
                    break
            # print(path)
            if flag:
                path.pop()
                # cur = path[-1]
                if path:
                    cur = path[-1]
                else:
                    return []
        path = path[:-1]
        return path[::-1]

    

    @staticmethod
    def is_special(t,sp):
        """
        判断字符t是否始于特殊字符sp代表的范围
        """
        # print(t)
        if sp == '.':
            if t not in ['\r','\n']:
                # print(t)
                return True
            else:
                return False
        elif sp == 'd':
            if '0' <= t <= '9':
                return True
            else:
                return False
        elif sp == 's':
            if t in [' ','\f','n','\r','\t','\v']:
                return True
            else:
                return False
        elif sp == 'w':
            if '0' <= t <= '9' or t == '_' or 'a' <= t <= 'z' or 'A' <= t <= 'Z':
                return True
            else:
                return False
        elif sp == 'D':
            if '0' <= t <= '9':
                return False
            else:
                return True
        elif sp == 'S':
            if t in [' ','\f','n','\r','\t','\v']:
                return False
            else:
                return True
        elif sp == 'W':
            if '0' <= t <= '9' or t == '_' or 'a' <= t <= 'z' or 'A' <= t <= 'Z':
                return False
            else:
                return True
        elif sp == "-":
            if t =='-':
                return True
            else:
                return False
        elif sp =="+":
            if t == "+":
                return True
            else:
                return False
        elif sp =="/":
            if t =='/':
                return True
            else:
                return False
        elif sp == "[":
            if t== '[':
                return True
            else:
                return False
        elif sp == "]":
            if t== ']':
                return True
            else:
                return False
        elif sp == "{":
            if t== '{':
                return True
            else:
                return False
        elif sp == "}":
            if t== '}':
                return True
            else:
                return False
        elif sp == "(":
            if t== '(':
                return True
            else:
                return False
        elif sp == ")":
            if t== ')':
                return True
            else:
                return False
        elif sp == "?":
            if t== '?':
                return True
            else:
                return False
        else:
            # print(t)
            raise AssertionError("不支持的特殊字符")
       

    @staticmethod
    def from_text(text: str) -> "NFA":
        """
        从自动机的文本表示构造自动机
        你不需要理解此函数的含义、阅读此函数的实现和调用此函数。
        """
        nfa = NFA()
        lines = text.splitlines()
        reading_rules = False
        for line in lines:
            if line == "": continue
            if line.startswith("states:"):
                nfa.num_states = int(line[7:])
                nfa.is_final = [False for _ in range(nfa.num_states)]
                nfa.rules = [[] for _ in range(nfa.num_states)]
                continue
            elif line.startswith("final:"):
                if nfa.num_states == 0: raise AssertionError("states必须出现在final和rules之前!")
                content = line[6:].strip()
                for s in content.split(" "):
                    if s == "": continue
                    nfa.is_final[int(s)] = True
                reading_rules = False
                continue
            elif line.startswith("rules:"):
                if nfa.num_states == 0: raise AssertionError("states必须出现在final和rules之前!")
                reading_rules = True
                continue
            elif line.startswith("input:"):
                reading_rules = False
                continue
            elif reading_rules:
                arrow_pos = line.find("->")
                space_pos = line.find(" ")
                if arrow_pos != -1 and space_pos != -1 and arrow_pos < space_pos:
                    src = int(line[0:arrow_pos])
                    dst = int(line[arrow_pos + 2:space_pos])
                    content = line[space_pos + 1:]
                    success = True
                    while success and content != "":
                        p = content.find(" ")
                        if p == -1:
                            p = len(content)
                        elif p == 0:
                            p = 1  # 当第一个字母是空格时，说明转移的字符就是空格。于是假定第二个字母也是空格（如果不是，会在后面直接报错）
                        rule = Rule()
                        rule.dst = dst
                        if p == 3 and content[1] == '-':
                            rule.type = RuleType.RANGE
                            rule.by = content[0]
                            rule.to = content[2]
                        elif p == 2 and content[0] == "\\":
                            if content[1] == "e":
                                rule.type = RuleType.EPSILON
                            else:
                                rule.type = RuleType.SPECIAL
                                rule.by = content[1]
                        elif p == 1 and (p >= len(content) or content[p] == ' '):
                            rule.type = RuleType.NORMAL
                            rule.by = content[0]
                        else:
                            success = False
                        nfa.rules[src].append(rule)
                        content = content[p + 1:]
                    if success:
                        continue
            raise ValueError("无法parse输入文件！失败的行： " + line)
        return nfa


if __name__ == '__main__':
    """
    程序入口点函数。已经帮你封装好了读取文本输入、构造自动机并执行字符串、输出结果等。
    一般来说，你不需要阅读和改动这里的代码，只需要完成exec函数即可。
    """
    if len(sys.argv) >= 2:
        with open(sys.argv[1], "r") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    input_str = None
    lines = text.splitlines()
    for line in lines:
        if line.startswith("input: "): input_str = line[7:]
    if input_str is None:
        raise ValueError("未找到输入字符串！注意输入字符串必须以input: 开头，其中冒号后面必须有空格！")

    nfa = NFA.from_text(text)
    result = nfa.exec(input_str)
    if result is None:
        print("Reject", end='')
    else:
        print(str(result), end='')
