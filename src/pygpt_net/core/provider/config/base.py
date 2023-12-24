#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2023.12.23 19:00:00                  #
# ================================================== #


class BaseProvider:
    def __init__(self, window=None):
        self.window = window
        self.id = ""
        self.type = "config"
        self.path = None
        self.path_app = None
        self.meta = None

    def load(self, all=False):
        pass

    def load_base(self):
        pass

    def save(self, items, filename='config.json'):
        pass

    def get_options(self):
        pass

    def get_version(self):
        pass
