"writing html is tedious.  py-list-html-translator makes it fun!"

"""
how to use py-list-html-translator:
 
from list_html_translator import Translator
in_list = ["@html"]
translator = Translator(in_list)
out_html = translator.translate()
print(out_html)
"""

from .list_html_translator import Translator

__version__ = "1.0.0"

__author__ = "critical-path"

__all__ = ["list_html_translator.py"]
