#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division
import os

import pytest

from mayaqt_generator import operation


SCRIPT_PATH = os.path.dirname(__file__)


# @pytest.fixture()
# def mayaqt_generator():
#     """クラスを生成する
#     """
#     mayaqt_generator = MayaQtTemplate()
#     return mayaqt_generator


# class TestMayaQtTemplate(object):
#     class TestStringFormatToDict(object):
#         @pytest.fixture()
#         def template_dict(self):
#             template_dict = {"temp": "format", "title": "name", "class": "mayaqt", "author": "tack2"}
#             return template_dict

#         def test_format_fstring_temp_to_string_format(self, mayaqt_generator, template_dict):
#             """{temp}を"format"にフォーマットする
#             """

#             format_string = mayaqt_generator.string_format_to_dict("{temp}", template_dict)
#             assert "format" == format_string

#         def test_format_fstring_title_to_string_name(self, mayaqt_generator, template_dict):
#             """{title}を"name"にフォーマットする
#             """

#             format_string = mayaqt_generator.string_format_to_dict("{title}", template_dict)
#             assert "name" == format_string

#         def test_format_fstring_class_and_author_to_string_mayaqt_and_tack2(self, mayaqt_generator, template_dict):
#             """{class}と{author}を"mayaqt"と"Tack2"にフォーマットする
#             """

#             target_string = "{class}\n{author}"
#             format_string = mayaqt_generator.string_format_to_dict(target_string, template_dict)
#             assert "mayaqt\ntack2" == format_string

#     class TestCreatePythonFileToString(object):
#         """PythonFileを文字列で作成する
#         """
#         @pytest.fixture
#         def template_folder(self, tmpdir):
#             test_dir = tmpdir.mkdir("create_file")
#             return test_dir

#         def test_create_python_file(self, template_folder, mayaqt_generator):
#             """PythonFileを作成する
#             """
#             mayaqt_generator.create_file(str(template_folder), "temp", ".py")
#             assert len(template_folder.listdir()) == 1

#         def test_create_file_with_template_name(self, template_folder, mayaqt_generator):
#             """PythonFileに「template」名で書き込む
#             """
#             mayaqt_generator.create_file(str(template_folder), "template", ".py")
#             compare_file = template_folder / "template.py"
#             assert template_folder.listdir()[0] == compare_file

#     class TestEditPythonFileToString(object):
#         """PythonFileを文字列で編集する
#         """
#         @pytest.fixture
#         def template_file(self, tmpdir):
#             """一時ファイル
#             """
#             test_file = tmpdir.mkdir("TestEditPythonFileToString").join("write.py")
#             return test_file

#         def test_writing_to_python_file_as_insert(self, template_file, mayaqt_generator):
#             """PythonFileに「insert」と書き込む
#             """
#             insert_text = "insert"
#             mayaqt_generator.edit_file(str(template_file), insert_text)
#             assert template_file.read() == insert_text

#     class TestLoadFile(object):
#         """ファイルを読み込む
#         """
#         @pytest.fixture
#         def template_yaml(self, tmpdir):
#             """一時ファイル
#             """
#             test_file = tmpdir.mkdir("TestLoadTemplateTextFile").join("sample.yaml")
#             test_file.write("{temp}")
#             return test_file

#         def test_reading_temp_in_text_file_as_string(self, mayaqt_generator, template_yaml):
#             """テキストファイルの中の{temp}を文字列として読み込む
#             """
#             load_text = mayaqt_generator.get_template_yaml(str(template_yaml))
#             assert "{temp}" == load_text


class TestYamlFileReader(object):
    """test code to YamlFIleReader.
    """

    @pytest.fixture
    def template_yaml(self, tmpdir):
        """一時ファイル
            """
        test_file = tmpdir.mkdir("TestLoadTemplateTextFile").join("sample.yaml")
        test_file.write("temp: sample")
        return test_file

    def test_reading_temp_in_text_file_as_string(self, template_yaml):
        """テキストファイルの中の{temp}を文字列として読み込む
        """
        load_text = operation.YamlFileReader(str(template_yaml)).get_read_data()
        assert {"temp": "sample"} == load_text


class TestSettingData(object):
    """test code SettingData.
    """

    parameters = [("title", "sample"),
                  ("questions", [{"name": "sample", "message": "what"}]),
                  ("convert_extensions", {"txt": "py", "ui": "ui"}),
                  ("template_path", "sample/path")
                  ]

    @pytest.fixture
    def sample_yaml(self):
        target_path = os.path.join(SCRIPT_PATH, "data", "setting_data_test.yaml")
        return target_path

    @pytest.mark.parametrize("search_attr, answer", parameters)
    def test_create_value(self, sample_yaml, search_attr, answer):
        ins = operation.SettingData(sample_yaml, "sample/path")
        compare_value = getattr(ins, search_attr)
        assert answer == compare_value
