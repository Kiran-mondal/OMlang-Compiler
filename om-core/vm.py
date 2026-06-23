# =====================================================================
# MODULE: om-core/vm.py
# =====================================================================
try:
    from .opcodes import OpCode
except (ImportError, ValueError):
    from opcodes import OpCode

# ... (Keep the rest of your OmVirtualMachine class code exactly the same) ...