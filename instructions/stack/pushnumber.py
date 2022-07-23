from instructions.instructiongenerator import InstructionGenerator

class PushNumberInstructionGenerator(InstructionGenerator):
    
    def is_valid_instruction(self) -> bool:
        return self.line.startswith("push ") and len(self.line.split(" ")) == 2 and self.line.split(" ")[1].isnumeric()

    def generate_code(self) -> str:
        return f"\tstack = append(stack, {self.line.split(' ')[1]})"