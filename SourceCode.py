# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:    SourceCode
Description:  
Author:       蔡创
Date:         2021/6/23
-------------------------------------------------
"""
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
        return filtered_content
