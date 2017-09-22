#!/usr/bin/env python3
# coding=utf-8

"""
Translate input English text to jamaican
"""

from urllib.request import urlopen
import html
import sys
import re

if len(sys.argv) < 2 :
    print("You must provide English Text to translate as arguments")
    exit(0)

sentence = '+'.join(sys.argv[1:])
sentence = html.escape(sentence)

html = urlopen("http://www.jamaicantranslator.com/?english=" + sentence)
b = re.sub(r".*class=\"translatorP\">\\n(.+) </p>.*", r"\1", str(html.read()), re.M)

print(b)
