from instructions.instructiongenerator import InstructionGenerator

class GotoInstructionGenerator(InstructionGenerator):
    
    def is_valid_instruction(self) -> bool:
        return self.line.startswith("goto ") and len(self.line.split(" ")) == 2
    
    def generate_code(self) -> str:
        return f"\t{self.line}"