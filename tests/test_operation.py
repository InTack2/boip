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
    def test_value(self, sample_yaml, search_attr, answer):
        """yamlファイルを渡し、対応する値になっているか確認する
        """
        ins = operation.SettingData(sample_yaml, "sample/path")
        compare_value = getattr(ins, search_attr)
        assert answer == compare_value
