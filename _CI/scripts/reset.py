#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: reset.py
#
# Copyright 2018 Costas Tyfoxylos
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#

import os
import sys
import shutil
import stat
import logging

# This is the main prefix used for logging
LOGGER_BASENAME = '''_CI.reset'''
LOGGER = logging.getLogger(LOGGER_BASENAME)
LOGGER.addHandler(logging.NullHandler())


current_file_path = os.path.dirname(os.path.abspath(__file__))
ci_path = os.path.abspath(os.path.join(current_file_path, '..'))
PROJECT_ROOT = os.path.dirname(ci_path)
if ci_path not in sys.path:
    sys.path.append(ci_path)

from configuration import ENVIRONMENT_VARIABLES


def on_error(func, path, exc_info):  # pylint: disable=unused-argument
    """
    Error handler for ``shutil.rmtree``.

    # Copyright Michael Foord 2004
    # Released subject to the BSD License
    # Please see http://www.voidspace.org.uk/python/license.shtml
    """
    if not os.access(path, os.W_OK):
        # Is the error an access error ?
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise  # pylint: disable=misplaced-bare-raise

def reset(project_root, environment_variables):
    pipfile_path = environment_variables.get('PIPENV_PIPFILE', 'Pipfile')
    venv = os.path.join(project_root, os.path.dirname(pipfile_path), '.venv')
    try:
        shutil.rmtree(venv, onerror=on_error)
        print(f'Successfully removed venv {venv}')
    except Exception as e:
        print(e)
        print(f'Unable to remove venv, make sure {venv} exists.')


if __name__ == '__main__':
    reset(PROJECT_ROOT, ENVIRONMENT_VARIABLES)
