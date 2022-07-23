from instructions import available_instructions
from instructions.instructiongenerator import InstructionGenerator

class InvalidSyntaxException(Exception):
    pass

DEBUG = False

def parse(script: str) -> str:
    instructions: list[InstructionGenerator] = []
    
    for index, line in enumerate(script.split("\n")):
        is_valid = False
        
        # Ignore tabs and 4 tab spaces
        line = line.replace("\t", "")
        line = line.replace("    ", "")
        
        # If the line starts with '#', it's a comment
        if line.startswith("#"):
            continue
        
        # Ignore empty lines
        if len(line) == 0:
            continue
        
        # Find the instruction for the specific line
        for instruction_generator_class in available_instructions:
            instruction_generator = instruction_generator_class(line)
            
            if instruction_generator.is_valid_instruction():
                is_valid = True
                instructions.append(instruction_generator)
                break
            
        # If no instruction is found, raise an exception
        if not is_valid:
            raise InvalidSyntaxException(f"Line {index + 1} cannot be parsed.")
        
    # Generate the code based on the static and dynamic code
    generated_code = ""    
    for instruction in instructions:
        generated_code += instruction.generate_code() + "\n\n"
        
        if DEBUG:
            instruction_name = type(instruction).__name__.replace('InstructionGenerator', '')
            generated_code += f"fmt.Println(\"{instruction_name}\")\nfmt.Println(stack)\n\n"
        
    with open("base_script.go", "r") as f:
        base_script = f.read()
        
    script = base_script.replace("\t//[generated_code]", generated_code)
        
    return script