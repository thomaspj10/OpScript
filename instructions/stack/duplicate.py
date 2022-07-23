from instructions.instructiongenerator import InstructionGenerator

class DuplicateInstructionGenerator(InstructionGenerator):
    
    def is_valid_instruction(self) -> bool:
        return self.line == "duplicate"

    def generate_code(self) -> str:
        return f"\ta = pop(&stack)\n\tstack = append(stack, a)\n\tstack = append(stack, a)"