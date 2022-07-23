from instructions.instructiongenerator import InstructionGenerator

class InputInstructionGenerator(InstructionGenerator):
    
    def is_valid_instruction(self) -> bool:
        return self.line == "input"
    
    def generate_code(self) -> str:
        return f"\tfmt.Scan(&a)\n\tstack = append(stack, a)"