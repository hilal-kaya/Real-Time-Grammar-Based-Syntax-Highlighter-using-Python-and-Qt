from lexer import Token, tokenize

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return Token("EOF", "", len(self.tokens))

    def match(self, expected_type, expected_value=None):
        token = self.current_token()
        if token.type == expected_type and (expected_value is None or token.value == expected_value):
            self.pos += 1
            return token
        raise SyntaxError(f"Expected {expected_type} '{expected_value}' at pos {token.position}, got '{token.value}'")

    def parse(self):
        while self.current_token().type != "EOF":
            self.statement()

    def statement(self):
        token = self.current_token()
        if token.type == "KEYWORD" and token.value in {"int", "float"}:
            self.var_declaration()
        elif token.type == "IDENTIFIER":
            self.assignment()
        elif token.type == "KEYWORD" and token.value == "if":
            self.if_statement()
        elif token.type == "KEYWORD" and token.value == "while":
            self.while_statement()
        else:
            raise SyntaxError(f"Unexpected token '{token.value}'")

    def var_declaration(self):
        self.match("KEYWORD")
        self.match("IDENTIFIER")
        self.match("DELIMITER", ";")

    def assignment(self):
        self.match("IDENTIFIER")
        self.match("OPERATOR", "=")
        self.expression()
        self.match("DELIMITER", ";")

    def if_statement(self):
        self.match("KEYWORD", "if")
        self.match("DELIMITER", "(")
        self.expression()
        self.match("DELIMITER", ")")
        self.match("DELIMITER", "{")
        while self.current_token().value != "}":
            self.statement()
        self.match("DELIMITER", "}")

    def while_statement(self):
        self.match("KEYWORD", "while")
        self.match("DELIMITER", "(")
        self.expression()
        self.match("DELIMITER", ")")
        self.match("DELIMITER", "{")
        while self.current_token().value != "}":
            self.statement()
        self.match("DELIMITER", "}")

    def expression(self):
        self.arith_expression()
        if self.current_token().type == "OPERATOR" and self.current_token().value in {">", "<", ">=", "<=", "==", "!="}:
            self.match("OPERATOR")
            self.arith_expression()

    def arith_expression(self):
        self.term()
        while self.current_token().value in {"+", "-"}:
            self.match("OPERATOR")
            self.term()



    def term(self):
        self.factor()
        while self.current_token().value in {"*", "/"}:
            self.match("OPERATOR")
            self.factor()

    def factor(self):
        token = self.current_token()
        if token.type == "NUMBER":
            self.match("NUMBER")
        elif token.type == "IDENTIFIER":
            self.match("IDENTIFIER")
        elif token.value == "(":
            self.match("DELIMITER", "(")
            self.expression()
            self.match("DELIMITER", ")")
        else:
            raise SyntaxError(f"Unexpected token '{token.value}' in factor")
