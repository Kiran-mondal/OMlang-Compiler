# =====================================================================
# MODULE: main.py (SYSTEM DRIVER & CLIENT ENTRY POINT)
# =====================================================================
import sys

# Note: In your final public repository directory structure, 
# you would uncomment these standard Python module imports:
#
# from opcodes import OpCode
# from lexer import OmLexer, TokenType
# from parser import OmParser
# from compiler import OmBytecodeCompiler
# from vm import OmVirtualMachine

def run_standalone_om_engine(source_code):
    """Executes the complete translation and processing pipeline for Om."""
    
    # Phase 1 & 2: Lexing & Parsing
    print("[Pipeline Stage 1 & 2]: Generating Abstract Syntax Tree...")
    lexer = OmLexer(source_code)
    parser = OmParser(lexer)
    ast = parser.parse()
    
    # Phase 3: Structural Bytecode Compilation
    print("[Pipeline Stage 3]: Emitting Independent Bytecode Vectors...")
    compiler = OmBytecodeCompiler()
    bytecode, constants = compiler.compile(ast)
    
    # Low-Level Diagnostic Output
    print("\n" + "-"*50)
    print(f"DEBUG - Binary Bytecode Stream : {bytecode}")
    print(f"DEBUG - Hardware Constant Pool   : {constants}")
    print("-"*50 + "\n")
    
    # Phase 4: Virtual Machine Core Boot
    print("=========================================")
    print("        BOOTING STANDALONE OM VM         ")
    print("=========================================")
    
    vm = OmVirtualMachine(bytecode, constants)
    vm.run()


if name == "main":
    # A native script script written entirely in your Om Language syntax layout
    om_sample_script = """
    alpha = 5 * 4
    beta = alpha + 10.5
    show beta
    """
    
    print("Initializing Om Runtime Framework Context...")
    print("Loading source payload...\n")
    
    # Trigger the compilation and execution loop
    run_standalone_om_engine(om_sample_script)