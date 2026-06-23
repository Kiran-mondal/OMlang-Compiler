# =====================================================================
# MODULE: om-core/parser.py (GRAMMATICAL PARSING ENGINE)
# =====================================================================
import sys
from lexer import TokenType

class AssignNode:
    def init(self, name, value): self.name = name; self.value = value
class ShowNode:
    def init(self, expr): self.expr = expr
class BinOpNode:
    def init(self, left, op, right): self.left = left; self.op = op; self.right = right
class NumNode:
    def init(self, val): self.val = val
class VarNode:
    def init(self, name): self.name = name

class OmParser:
    def init(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def consume(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            print(f"Syntax Error: Expected token type '{token_type}', found '{self.current_token.type}'")
            sys.exit(1)

    def parse(self):
        statements = []
        while self.current_token.type != TokenType.EOF:
            if self.current_token.type == TokenType.SHOW:
                self.consume(TokenType.SHOW)
                statements.append(ShowNode(self.expr()))
            elif self.current_token.type == TokenType.IDENTIFIER:
                name = self.current_token.value
                self.consume(TokenType.IDENTIFIER)
                self.consume(TokenType.ASSIGN)
                statements.append(AssignNode(name, self.expr()))
            else:
                print(f"Syntax Error: Invalid token start sequence '{self.current_token.value}'")
                sys.exit(1)
        return statements

    def expr(self):
        node = self.term()
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token.type
            self.consume(self.current_token.type)
            node = BinOpNode(node, op, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.current_token.type in (TokenType.MUL, TokenType.DIV):
            op = self.current_token.type
            self.consume(self.current_token.type)
            node = BinOpNode(node, op, self.factor())
        return node

    def factor(self):
        t = self.current_token
        if t.type == TokenType.NUMBER:
            self.consume(TokenType.NUMBER)
            return NumNode(t.value)
        elif t.type == TokenType.IDENTIFIER:
            name = t.value
            self.consume(TokenType.IDENTIFIER)
            return VarNode(name)
        print(f"Parser Error: Unexpected token evaluation context {t}")
        sys.exit(1)