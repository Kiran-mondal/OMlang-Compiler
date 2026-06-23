# =====================================================================
# MODULE: om-core/lexer.py
# =====================================================================
import sys

class TokenType:
    EOF = "EOF"; IDENTIFIER = "IDENTIFIER"; NUMBER = "NUMBER"; STRING = "STRING"
    SHOW = "show"; INPUT = "input"; ASSIGN = "="
    PLUS = "+"; MINUS = "-"; MUL = "*"; DIV = "/"
    
    # NEW TOKENS
    IF = "if"; WHILE = "while"
    LBRACE = "{"; RBRACE = "}"
    EQ = "=="; LT = "<"; GT = ">"

class Token:
    def init(self, type_, value):
        self.type = type_; self.value = value
    def repr(self):
        return f"Token({self.type}, {repr(self.value)})"

class OmLexer:
    def init(self, text):
        self.text = text; self.pos = 0
        self.current_char = text[0] if text else None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance(); continue
                
            if self.current_char in ('"', "'"):
                quote_type = self.current_char
                self.advance()
                val = ""
                while self.current_char is not None and self.current_char != quote_type:
                    val += self.current_char
                    self.advance()
                self.advance() 
                return Token(TokenType.STRING, val)

            if self.current_char.isdigit() or self.current_char == '.':
                val = ""
                while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
                    val += self.current_char
                    self.advance()
                return Token(TokenType.NUMBER, val)
                
            if self.current_char.isalpha() or self.current_char == '_':
                val = ""
                while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
                    val += self.current_char
                    self.advance()
                if val in ("show", "echo"): return Token(TokenType.SHOW, val)
                if val == "input": return Token(TokenType.INPUT, val)
                if val == "if": return Token(TokenType.IF, val)
                if val == "while": return Token(TokenType.WHILE, val)
                return Token(TokenType.IDENTIFIER, val)
            
            # Multi-character operator for ==
            if self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(TokenType.EQ, "==")
                return Token(TokenType.ASSIGN, "=")

            mapping = {'+': TokenType.PLUS, '-': TokenType.MINUS, '*': TokenType.MUL, '/': TokenType.DIV, 
                       '<': TokenType.LT, '>': TokenType.GT, '{': TokenType.LBRACE, '}': TokenType.RBRACE}
            
            if self.current_char in mapping:
                t = Token(mapping[self.current_char], self.current_char)
                self.advance()
                return t
                
            print(f"Lexer Error: Unknown character '{self.current_char}'")
            sys.exit(1)
            
        return Token(TokenType.EOF, None)