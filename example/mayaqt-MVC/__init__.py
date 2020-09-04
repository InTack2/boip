# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division

from . import controller
from . import model
from . import view

from .gui import sample_gui

reload(controller)
reload(model)
reload(view)
reload(sample_gui)


def main():
    global sample_window_controller

    try:
        sample_window_controller.close_gui()
    except:
        pass

    sample_window_controller = controller.Controller()
    sample_window_controller.show_gui()
