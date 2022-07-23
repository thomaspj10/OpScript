from instructions.instructiongenerator import InstructionGenerator

class DeleteInstructionGenerator(InstructionGenerator):
    
    def is_valid_instruction(self) -> bool:
        return self.line == "delete"

    def generate_code(self) -> str:
        return f"pop(&stack)"