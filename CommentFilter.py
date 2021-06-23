# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:    CommentFilter
Description:  
Author:       蔡创
Date:         2021/6/23
-------------------------------------------------
"""
import re
from re import RegexFlag
from typing import List, AnyStr, Pattern, Union


class CommentFilter(object):

    def __init__(self):
        self.source_code = ""

    def filter(self, source_code_lines: List[str]):
        self.source_code = "".join(source_code_lines)
        self.__filter_help(r"\s*?//.*?\n", "\n") \
            .__filter_help(r"/[*].*?[*]/", '', re.S) \
            .__filter_help(r"<!--.*?-->", '', re.S) \
            .__filter_help(r"\n\s*\n", "\n")
        return self.source_code

    def __filter_help(self, pattern, repl, flags: Union[int, RegexFlag] = ...):
        if flags is not ...:
            self.source_code = re.sub(pattern, repl, self.source_code, flags=flags)
        else:
            self.source_code = re.sub(pattern, repl, self.source_code)
        return self
