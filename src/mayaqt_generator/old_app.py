#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""main
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division

import os
from ABC import ABCMeta, abstractmethod


class FileExtensionRule(object):
    def __init__(self, rule):
        for key, value in rule.items():
            setattr(self, key, value)


class MayaQtTemplate(object):
    """MayaQt用のテンプレートクラス
    """

    def __init__(self):
        self.__python_path = ""

    def string_format_to_dict(self, target_string, format_settings):
        """string format to dict.

        Args:
            target_string (str): format target.
            format_settings (dict): A dictionary for format.
                                    If the key of this dictionary is in target_string, you should format it with a values.

        Returns:
            str: fromat after data.
        """
        format_after_data = target_string.format(**format_settings)
        return format_after_data

    def create_file(self, target_dir, file_name, target_extension):
        """create to python file.

        Args:
            target_dir (str): create target path.
            file_name (str): create python file name.
        """
        self.__python_path = os.path.join(target_dir, file_name + target_extension)
        with open(self.__python_path, mode="w"):
            pass

    def edit_file(self, target_file=None, insert_text=None):
        """python file editing.

        Args:
            target_file (str): target file path.
            insert_text (str): Adding a string to a file.
        """
        load_file_path = target_file
        if target_file is None:
            load_file_path = self.__python_path
        with open(load_file_path, mode="w") as f:
            f.write(insert_text)


if __name__ == "__main__":
    script_path = os.path.dirname(__file__)

    template_root_path = os.path.join(script_path, "template")
    template_qt_mvc_file = os.path.join(template_root_path, "qt_mvc.txt")

    _maya_qt_generator = MayaQtTemplate()
    template_data = _maya_qt_generator.get_template_file(template_qt_mvc_file)

    fromat_settings = {"test": "dekita", "test_02": "yattane"}
    after_format_data = _maya_qt_generator.string_format_to_dict(template_data, fromat_settings)
    _maya_qt_generator.create_file(script_path, "format_template", ".py")
    _maya_qt_generator.edit_file(insert_text=after_format_data)
    print("complete.")
