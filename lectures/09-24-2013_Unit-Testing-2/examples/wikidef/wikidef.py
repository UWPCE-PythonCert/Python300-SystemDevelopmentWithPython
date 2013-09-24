#!/usr/bin/env python

import sys

from api import Wikipedia

title = sys.argv[1]

print Wikipedia.article(title).encode('utf-8')

