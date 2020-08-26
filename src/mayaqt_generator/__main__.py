# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division

from app import BoitemQuestionCreator

_boitem_question_creator = BoitemQuestionCreator()

title_answer = _boitem_question_creator.create_template_selector()
answers = _boitem_question_creator.create_multi_question(title_answer)
create_folder = _boitem_question_creator.create_folder_question(title_answer)
convert_extension_data = _boitem_question_creator.operator.select_convert_extensions(title_answer)
_boitem_question_creator.operation_replace_file(create_folder, convert_extension_data, formatter_data=answers)

# リスト質問
print("title_answer :{}".format(title_answer))
print(answers)
print("create_folder : {}".format(create_folder))
