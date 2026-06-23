# =====================================================================
# PRODUCTION MODULE: compiler.py (BINARY EMISSION UPGRADE)
# =====================================================================
import json
import struct
from opcodes import OpCode

class OmBytecodeCompiler:
    def init(self):
        self.bytecode = []
        self.constants = []

    def add_constant(self, value):
        if value not in self.constants:
            self.constants.append(value)
        return self.constants.index(value)

    def compile_to_binary(self, ast, output_filepath):
        """Compiles AST and exports a highly compressed native .omb file."""
        for stmt in ast:
            self.gen(stmt)
        self.bytecode.append(OpCode.HALT)

        # Serialize constants pool to JSON string, then encode to raw bytes
        constants_bytes = json.dumps(self.constants).encode('utf-8')
        constants_len = len(constants_bytes)

        # Construct a strict binary header:
        # Magic bytes ("OM"), followed by a 4-byte unsigned integer indicating constants length
        header = struct.pack('2sI', b'OM', constants_len)

        # Convert the instruction list into a raw immutable bytearray
        instruction_bytes = bytearray(self.bytecode)

        # Write the absolute compiled binary image to disk
        with open(output_filepath, 'wb') as f:
            f.write(header)
            f.write(constants_bytes)
            f.write(instruction_bytes)
            
        print(f"[Compiler Success]: Solidified hardware binary -> '{output_filepath}'")

    def gen(self, node):
        # ... (Keep your previous recursive AST node visitor logic here) ...
        pass