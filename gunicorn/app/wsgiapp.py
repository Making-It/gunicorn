# -*- coding: utf-8 -
#
# This file is part of gunicorn released under the MIT license. 
# See the NOTICE for more information.

import os
import sys

from gunicorn import util
from gunicorn.app.base import Application

class WSGIApplication(Application):
    
    def init(self, parser, opts, args):
        if len(args) != 1:
            parser.error("No application module specified.")

        self.cfg.set("default_proc_name", args[0])
        # 获取命令行第一个位置参数，一般是web_app，如module:app
        self.app_uri = args[0]

        # 将当前进程的工作加入sys.path（python搜索路径）
        sys.path.insert(0, os.getcwd())

    def load(self):
        return util.import_app(self.app_uri)

def run():
    """\
    The ``gunicorn`` command line runner for launcing Gunicorn with
    generic WSGI applications.
    """
    from gunicorn.app.wsgiapp import WSGIApplication
    WSGIApplication("%prog [OPTIONS] APP_MODULE").run()