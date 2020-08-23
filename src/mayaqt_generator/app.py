# -*- coding: utf-8 -*-
"""メイン処理
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division


import pprint


import PyInquirer

from operation import FolderOperation

custom_style_2 = PyInquirer.style_from_dict({
    "separator": '#6C6C6C',
    "questionmark": '#FF9D00 bold',
    "selected": '#5F819D',
    "pointer": '#FF9D00 bold',
    "instruction": '',  # default
    "answer": '#5F819D bold',
    "question": '',
})


class BoitemQuestionCreator(object):
    def __init__(self):
        self.operator = FolderOperation()

    def create_template_selector(self):
        """テンプレートを選択する質問を生成

        Returns:
            dict: {title: choice_title}
        """
        title_list = _boitem_question_creator.operator.get_title_list()
        questions = [
            {
                "type": "list",
                "name": "title",
                "message": "テンプレートを選択",
                "choices": title_list
            }
        ]
        answers = PyInquirer.prompt(questions)
        title = answers["title"]
        template_path = self.operator.select_template_path(title)
        folder_name = self.create_folder_question()
        self.operator.duplicate_template_folder(template_path, folder_name)

        return title

    def create_multi_question(self, target_title):
        """複数の質問を生成

        Args:
            target_title (str): 設定fileのタイトル

        Returns:
            list: questions.
        """
        add_questions = _boitem_question_creator.operator.select_questions(target_title)
        questions = []
        for quest in add_questions:
            quest = {key: unicode(value) for key, value in quest.items()}

            question_template = {
                "type": "input",
            }
            question_template.update(quest)

            questions.append(question_template)
        questions_answers = PyInquirer.prompt(questions)
        return questions_answers

    def create_folder_question(self):
        question = {
            "type": "input",
            "name": "folder_name",
            "message": "フォルダ名は？"
        }
        folder_answer = PyInquirer.prompt(question)
        if folder_answer["folder_name"] == "":
            raise self.NotFoundFolderName("フォルダ名が不正です。")
        return folder_answer["folder_name"]

    class NotFoundFolderName(Exception):
        pass


if __name__ == "__main__":
    _boitem_question_creator = BoitemQuestionCreator()
    title_answer = _boitem_question_creator.create_template_selector()
    # answers = _boitem_question_creator.create_multi_question(title_answer)

    # リスト質問

    print(title_answer)
