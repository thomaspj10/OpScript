from instructions.instructiongenerator import InstructionGenerator

class IfInstructionGenerator(InstructionGenerator):
    
    operations = ["==", "!=", ">", "<", ">=", "<="]
    
    def is_valid_instruction(self) -> bool:
        return self.line.startswith("if ") and len(self.line.split(" ")) == 2 and self.line.split(" ")[1] in self.operations
    
    def generate_code(self) -> str:
        return f"\tif (stack[len(stack) - 1] {self.line.split(' ')[1]} stack[len(stack) - 2]) " + "{"