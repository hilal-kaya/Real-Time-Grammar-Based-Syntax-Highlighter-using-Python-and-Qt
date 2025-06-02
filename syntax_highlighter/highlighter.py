from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt5.QtCore import Qt
from lexer import tokenize

class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.formats = {
            "KEYWORD": self.create_format("purple", bold=True),
            "IDENTIFIER": self.create_format("black"),
            "NUMBER": self.create_format("blue"),
            "OPERATOR": self.create_format("red"),
            "DELIMITER": self.create_format("green"),
            "UNKNOWN": self.create_format("gray", bold=True),

        }

    def create_format(self, color, bold=False):
        fmt = QTextCharFormat()
        fmt.setForeground(QColor(color))
        if bold:
            fmt.setFontWeight(QFont.Bold)
        return fmt

    def highlightBlock(self, text):
        tokens = tokenize(text)
        for token in tokens:
            token_format = self.formats.get(token.type)
            if token_format:
                self.setFormat(token.position, len(token.value), token_format)
