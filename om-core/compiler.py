# =====================================================================
# MODULE: om-core/compiler.py
# =====================================================================
try:
    from .opcodes import OpCode
    from .lexer import TokenType
except (ImportError, ValueError):
    from opcodes import OpCode
    from lexer import TokenType

# ... (Keep the rest of your OmBytecodeCompiler class code exactly the same) ...