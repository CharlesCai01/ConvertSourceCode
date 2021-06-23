# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:    SourceCode
Description:  
Author:       蔡创
Date:         2021/6/23
-------------------------------------------------
"""
import os

from CommentFilter import CommentFilter


class SourceCode:

    def __init__(self, root: str, file_path: str):
        self.__root = root
        self.__file_path = file_path
        self.__comment_filter = CommentFilter()

    def get_content(self):
        with open(self.__file_path, 'r', encoding='utf-8', errors='ignore') as source_code_file:
            lines = source_code_file.readlines()
            filtered_content = self.__comment_filter.filter(lines)
        return self.__add_prefix(filtered_content)

    def __add_prefix(self, filtered_content):
        prefix_str = "// {}\n".format(os.path.relpath(self.__file_path, self.__root))
        return prefix_str + filtered_content + "\n"
