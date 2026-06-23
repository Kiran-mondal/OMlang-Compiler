# =====================================================================
# MODULE: main.py (PRODUCTION CLI ENGINE DRIVER)
# =====================================================================
import sys
import os

# Import all of your custom, independent components from the local folder
from opcodes import OpCode
from lexer import OmLexer, TokenType
from parser import OmParser
from compiler import OmBytecodeCompiler
from vm import OmVirtualMachine

def execute_file_pipeline(filepath):
    """Reads a standalone .om file from disk and runs it through the VM pipeline."""
    if not os.path.exists(filepath):
        print(f"System Error: File target location '{filepath}' could not be resolved.")
        sys.exit(1)
        
    if not filepath.endswith('.om'):
        print("System Error: The Om virtual machine engine only executes native '.om' files.")
        sys.exit(1)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            source_code = f.read()
    except Exception as e:
        print(f"System Error: Unable to read file content safely. Details: {e}")
        sys.exit(1)

    # --- Phase 1 & 2: Structural Verification ---
    lexer = OmLexer(source_code)
    parser = OmParser(lexer)
    ast = parser.parse()

    # --- Phase 3: Compilation ---
    compiler = OmBytecodeCompiler()
    bytecode, constants = compiler.compile(ast)

    # --- Phase 4: Isolated Environment Execution ---
    vm = OmVirtualMachine(bytecode, constants)
    vm.run()

def show_help_menu():
    """Prints standard compiler diagnostic options to the user."""
    print("==================================================")
    print("          The Om Language Standalone CLI          ")
    print("==================================================")
    print("Usage Rules:")
    print("  python main.py run <filename.om>   | Compiles and runs a script file")
    print("  python main.py version             | Displays system version data")
    print("==================================================")

if name == "main":
    # Check if the user passed enough system arguments in the terminal
    if len(sys.argv) < 2:
        show_help_menu()
        sys.exit(0)

    command = sys.argv[1].lower()

    if command == "version":
        print("Om Language Compiler Environment: Standalone-v4.0.0-Bytecode-VM")
        
    elif command == "run":
        if len(sys.argv) < 3:
            print("CLI Error: Missing file target. Syntax target: python main.py run <filename.om>")
            sys.exit(1)
            
        target_file = sys.argv[2]
        execute_file_pipeline(target_file)
        
    else:
        print(f"CLI Error: Unknown operation token '{command}' entered.")
        show_help_menu()