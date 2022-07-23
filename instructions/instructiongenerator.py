class InstructionGenerator:
    
    instruction_name: str
    line: str
    
    def __init__(self, line: str) -> None:
        self.line = line
        
    def is_valid_instruction(self) -> bool:
        return False
    
    def generate_code(self) -> str:
        return ""