
import re

KEYWORDS = {"if", "else", "while", "return", "int", "float", "void", "for", "break", "continue", "switch", "case", "default", "do"}
OPERATORS = {"==", "+", "-","*", "/", "=", "<",">",}
DELIMITERS = {";", "(", ")", "{", "}"}

TOKEN_SPEC = [
    ("NUMBER", r"\d+(\.\d+)?"),
    ("ID", r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("OP", r"==|!=|>=|<=|>|<|[-+*/=]"),
    ("DELIM", r"[;(){}]"),
    ("NEWLINE", r"\n"),
    ("SKIP", r"[ \t]+"),
    ("MISMATCH", r"."),
]


token_regex = re.compile("|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC))

class Token:
    def __init__(self, type_, value, position):
        self.type = type_
        self.value = value
        self.position = position

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

def tokenize(code):
    tokens = []
    for mo in token_regex.finditer(code):
        kind = mo.lastgroup
        value = mo.group()
        pos = mo.start()
        if kind == "NUMBER":
            tokens.append(Token("NUMBER", value, pos))

        elif kind == "ID":
            if value in KEYWORDS:
                tokens.append(Token("KEYWORD", value, pos))

            else:
                tokens.append(Token("IDENTIFIER", value, pos))

        elif kind == "OP":
            tokens.append(Token("OPERATOR", value, pos))

        elif kind == "DELIM":
            tokens.append(Token("DELIMITER", value, pos))

        elif kind == "SKIP" or kind == "NEWLINE":
            continue
        
        elif kind == "MISMATCH":
            tokens.append(Token("UNKNOWN", value, pos))
    return tokens
