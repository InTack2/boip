# -*- coding: utf-8 -*-
"""searchr
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division

import os
import shutil
from abc import ABCMeta, abstractmethod

import yaml


PRESET_FOLDER = os.path.join(os.path.dirname(__file__), "preset")
SETTING_FILE = "boitem.yaml"
TEMPLATE_FOLDER = "template"


class FolderOperation(object):
    def __init__(self, search_path=PRESET_FOLDER):
        self.__template_set_list = self.__get_template_data(search_path)

    @property
    def template_set_list(self):
        return self.__template_set_list

    def __get_template_data(self, search_path):
        """boitemSetを取得する

        Returns:
            list(SettingData): Setting Data list.
        """
        found_template_set = []
        for root, dirs, files in os.walk(search_path):
            if TEMPLATE_FOLDER in dirs and SETTING_FILE in files:
                file_index = files.index(SETTING_FILE)
                setting_file = os.path.join(root, files[file_index])

                dir_index = dirs.index(TEMPLATE_FOLDER)
                template_folder = os.path.join(root, dirs[dir_index])

                found_template_set.append(SettingData(setting_file, template_folder))

        return found_template_set

    def select_template_path(self, target_title):
        """titleから該当のtemplateを取得する

        Args:
            target_title (str): setting_file内のtitle名
        """
        for template_set in self.__template_set_list:
            if target_title == template_set.title:
                return template_set.template_path

    def select_questions(self, target_title):
        for template_set in self.__template_set_list:
            if target_title == template_set.title:
                return template_set.questions

    def duplicate_template_folder(self, dis_folder, src_folder_name):
        """TemplateFolderを複製する

        Args:
            target_folder (str): 複製先のフォルダ
        """
        current_directory = os.getcwd()

        target_folder = os.path.join(current_directory, src_folder_name)

        shutil.copytree(dis_folder, target_folder)
        return target_folder

    def get_title_list(self):
        """タイトルリストを取得する

        Returns:
            list: タイトルリスト
        """
        title_list = []
        for template_set in self.__template_set_list:
            title_list.append(template_set.title)
        return title_list

# =================================================================================
# Reader
# =================================================================================


class BaseReader(object):
    """ベースの読み込みクラス
    """
    __metaclass__ = ABCMeta

    def __init__(self, path):
        self.read_path = path

    @abstractmethod
    def get_read_data(self):
        """読み込んだデータを返す
        """
        pass


class YamlFileReader(BaseReader):
    """YamlFile用のReader
    """

    def get_read_data(self):
        """読み込んだデータを返す
        """
        with open(self.read_path) as f:
            yaml_data = yaml.load(f, Loader=yaml.FullLoader)
            return yaml_data


# =================================================================================
# Data
# =================================================================================
class SettingData(object):
    """SettingDataデータ構造
    """

    def __init__(self, setting_file, template_folder, reader=YamlFileReader):
        self.__data = self.get_load_data(setting_file, reader)
        self.__title = self.__data["title"]
        self.__questions = self.__data["question"]
        self.__convert_extensions = self.__data["convertExtensions"]
        self.__template_path = template_folder

    @ property
    def title(self):
        return self.__title

    @ property
    def questions(self):
        return self.__questions

    @ property
    def convert_extensions(self):
        return self.__convert_extensions

    @ property
    def template_path(self):
        return self.__template_path

    def get_load_data(self, setting_file, reader):
        """データを読み込む
        """
        _reader = reader(setting_file)
        data = _reader.get_read_data()
        return data
