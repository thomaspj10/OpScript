from instructions.instructiongenerator import InstructionGenerator

class PrintInstructionGenerator(InstructionGenerator):
    
    def is_valid_instruction(self) -> bool:
        return self.line == "print"
    
    def generate_code(self) -> str:
        return f"\tfmt.Println(pop(&stack))"