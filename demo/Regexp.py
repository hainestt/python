# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

import re

# 1
txt = re.compile(r'<[^>]+>')
ts = txt.sub('$', '<html><head>Head</head><body>Body</body></html>')
words = re.compile(r'[^a-z^A-Z]+').split(ts)
print(ts, words)