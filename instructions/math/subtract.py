from instructions.instructiongenerator import InstructionGenerator

class SubtractInstructionGenerator(InstructionGenerator):
    
    def is_valid_instruction(self) -> bool:
        return self.line == "-"
    
    def generate_code(self) -> str:
        return f"\ta = pop(&stack)\n\tb = pop(&stack)\n\tstack = append(stack, a-b)"