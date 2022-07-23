from instructions.instructiongenerator import InstructionGenerator

class EndifInstructionGenerator(InstructionGenerator):
    
    def is_valid_instruction(self) -> bool:
        return self.line == "endif"
    
    def generate_code(self) -> str:
        return "\t}"