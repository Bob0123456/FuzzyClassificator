# -*- coding: utf-8 -*-

import os
import shutil
from recommonmark.parser import CommonMarkParser

if not os.path.exists('docs'):
    os.mkdir('docs')

shutil.copy('README.md', 'docs')


source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']
