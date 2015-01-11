"""
The compiler composes each phase into a single compile() function to translate the source code into the target language.

Translate: http://en.wikipedia.org/wiki/Translator_(computing)
"""
from romnomnom.lexer import lex
from romnomnom.parser import parse
from romnomnom.generator import generate


def compile(source: str):
    """
    >>> eval(compile("XLII"))
    42
    """
    return generate(parse(lex(source)))
