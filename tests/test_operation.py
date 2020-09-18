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

from boip import operation


SCRIPT_PATH = os.path.dirname(__file__)


@pytest.fixture
def sample_data_path():
    data_path = os.path.join(SCRIPT_PATH, "data")
    return data_path


@pytest.fixture
def sample_yaml(sample_data_path):
    target_path = os.path.join(sample_data_path, operation.SETTING_FILE_NAME)
    return target_path


@pytest.fixture
def sample_template_folder(sample_data_path):
    template_path = os.path.join(sample_data_path, operation.TEMPLATE_FOLDER_NAME)
    return template_path


@pytest.fixture
def sample_create_boip_set(sample_data_path):
    boip_set_list = operation.BoipSetList(sample_data_path)
    return boip_set_list


class TestFileFormatter(object):
    """test code to FileFormatter.
    """

    def test_replace_file(self, tmp_path):
        temporary_path = tmp_path / "test_replace_file"
        temporary_path.mkdir()
        temp_file = temporary_path / "sample.txt"
        temp_file.write_text(r"{sample}")

        sample_formatter_data = {"sample": "replace word"}
        _operation = operation.FileFormatter(sample_formatter_data)
        _operation.replace_file(str(temp_file), "txt")

        assert "replace word" == temp_file.read_text()


class TestFolderFormatter(object):
    """test code to FolderFormatter.
    """

    def test_replace_file(self, tmp_path):
        temporary_path = tmp_path / "test_template_folder_replace_file"
        temporary_path.mkdir()
        temp_file = temporary_path / "sample.txt"
        temp_file_2 = temporary_path / "sample_2.txt"
        temp_file.write_text(r"{sample}")
        temp_file_2.write_text(r"{sample} {sample}")

        sample_formatter_data = {"sample": "replace word"}
        _operation = operation.FolderFormatter(str(temporary_path), {"txt": "txt"}, sample_formatter_data)
        _operation.replace_files()

        assert "replace word" == temp_file.read_text()
        assert "replace word replace word" == temp_file_2.read_text()


class TestBoipSetList(object):
    """test code to BoipSetList.
    """

    def test_select_template_path(self, sample_create_boip_set, sample_template_folder):
        assert sample_template_folder == sample_create_boip_set.select_template_path("sample")

    def test_select_questions(self, sample_create_boip_set):
        assert [{"message": "what question?", "name": "sample"}] == sample_create_boip_set.select_questions("sample")

    def test_select_convert_extensions(self, sample_create_boip_set):
        assert {"txt": "py", "ui": "ui"} == sample_create_boip_set.select_convert_extensions("sample")

    def test_duplicate_template_folder(self, tmp_path, sample_create_boip_set):
        temporary_path = tmp_path / "test_duplicate"
        template_folder_path = sample_create_boip_set.select_template_path("sample")
        sample_create_boip_set.duplicate_template_folder(template_folder_path, str(temporary_path))
        assert 1 == len(list(temporary_path.iterdir()))

    def test_get_title_list(self, sample_create_boip_set):
        title_list = sample_create_boip_set.get_title_list()
        assert 2 == len(title_list)


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
                  ("questions", [{"name": "sample", "message": "what question?"}]),
                  ("convert_extensions", {"txt": "py", "ui": "ui"}),
                  ("template_path", "sample/path")
                  ]

    @pytest.mark.parametrize("search_attr, answer", parameters)
    def test_value(self, sample_yaml, search_attr, answer):
        """yamlファイルを渡し、対応する値になっているか確認する
        """
        ins = operation.SettingData(sample_yaml, "sample/path")
        compare_value = getattr(ins, search_attr)
        assert answer == compare_value
