from instructions.instructiongenerator import InstructionGenerator

class SwapInstructionGenerator(InstructionGenerator):
    
    def is_valid_instruction(self) -> bool:
        return self.line.startswith("swap ") and len(self.line.split(" ")) == 3 and self.line.split(" ")[1].isnumeric() and self.line.split(" ")[2].isnumeric()

    def generate_code(self) -> str:
        a = self.line.split(' ')[1]
        b = self.line.split(' ')[2]
        
        return f"\tstack[len(stack) - {a} - 1], stack[len(stack) - {b} - 1] = stack[len(stack) - {b} - 1], stack[len(stack) - {a} - 1]"