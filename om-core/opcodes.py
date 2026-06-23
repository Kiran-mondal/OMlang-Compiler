# =====================================================================
# MODULE: om-core/opcodes.py
# =====================================================================
class OpCode:
    LOAD_CONST = 0x01
    STORE_VAR  = 0x02
    LOAD_VAR   = 0x03
    ADD        = 0x04
    SUB        = 0x05
    MUL        = 0x06
    DIV        = 0x07
    PRINT      = 0x08
    INPUT      = 0x09
    
    # NEW: Logic and Control Flow Instructions
    CMP_EQ     = 0x0A   # Compare Equals (==)
    CMP_LT     = 0x0B   # Compare Less Than (<)
    CMP_GT     = 0x0C   # Compare Greater Than (>)
    JUMP_FALSE = 0x0D   # Jump if condition is false (Used for IF / WHILE)
    JUMP       = 0x0E   # Unconditional Jump (Used to loop back)
    
    HALT       = 0x00