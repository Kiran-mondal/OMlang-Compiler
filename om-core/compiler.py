# =====================================================================
# MODULE: compiler.py (AST TO BYTECODE TRANSLATION ENGINE)
# =====================================================================
# Note: In a multi-file layout, you would do:
# from opcodes import OpCode
# from lexer import TokenType
# from parser import NumNode, VarNode, AssignNode, ShowNode, BinOpNode

class OmBytecodeCompiler:
    def init(self):
        self.bytecode = []
        self.constants = []

    def add_constant(self, value):
        """Stores a unique numerical constant and returns its index register position."""
        if value not in self.constants:
            self.constants.append(value)
        return self.constants.index(value)

    def compile(self, ast):
        """Accepts a list of AST statement nodes and generates the complete bytecode package."""
        for stmt in ast:
            self.gen(stmt)
        
        # Append the terminal HALT instruction to signify the end of the script
        self.bytecode.append(OpCode.HALT)
        return self.bytecode, self.constants

    def gen(self, node):
        """Recursive node visitor that emits structural instruction bytes."""
        if isinstance(node, NumNode):
            # Evaluate type safety for floating points vs absolute integers
            val = float(node.val) if '.' in node.val else int(node.val)
            const_idx = self.add_constant(val)
            # Emit instruction code followed by the data index parameter
            self.bytecode.extend([OpCode.LOAD_CONST, const_idx])
            
        elif isinstance(node, VarNode):
            self.bytecode.extend([OpCode.LOAD_VAR, node.name])
            
        elif isinstance(node, AssignNode):
            # Compile the expression evaluation first to place its result on the stack
            self.gen(node.value)
            # Store the resulting stack value into the variable key
            self.bytecode.extend([OpCode.STORE_VAR, node.name])
            
        elif isinstance(node, ShowNode):
            # Compile the child expression evaluation
            self.gen(node.expr)
            # Push the terminal print instruction command
            self.bytecode.append(OpCode.PRINT)
            
        elif isinstance(node, BinOpNode):
            # Follow Left-to-Right Postfix evaluation stack logic
            self.gen(node.left)
            self.gen(node.right)
            
            # Append math operators based on structural syntax token type matching
            if node.op == TokenType.PLUS: 
                self.bytecode.append(OpCode.ADD)
            elif node.op == TokenType.MINUS: 
                self.bytecode.append(OpCode.SUB)
            elif node.op == TokenType.MUL: 
                self.bytecode.append(OpCode.MUL)
            elif node.op == TokenType.DIV: 
                self.bytecode.append(OpCode.DIV)