from instructions.instructiongenerator import InstructionGenerator

class GotolabelInstructionGenerator(InstructionGenerator):
    
    def is_valid_instruction(self) -> bool:
        return self.line.endswith(":") and len(self.line.split(" ")) == 1
    
    def generate_code(self) -> str:
        return f"\t{self.line}"