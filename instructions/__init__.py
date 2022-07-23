from instructions.logic.ifstatement import *
from instructions.logic.endif import *
from instructions.logic.goto import *
from instructions.logic.gotolabel import *

from instructions.math.add import *
from instructions.math.subtract import *
from instructions.math.divide import *
from instructions.math.multiply import *

from instructions.operations.print import *
from instructions.operations.input import *

from instructions.stack.pushnumber import *
from instructions.stack.duplicate import *
from instructions.stack.delete import *
from instructions.stack.swap import *

available_instructions = [
    IfInstructionGenerator,
    EndifInstructionGenerator,
    GotoInstructionGenerator,
    GotolabelInstructionGenerator,
    
    AddInstructionGenerator,
    SubtractInstructionGenerator,
    DivideInstructionGenerator,
    MultiplyInstructionGenerator,
    
    PrintInstructionGenerator,
    InputInstructionGenerator,
    
    PushNumberInstructionGenerator,
    DuplicateInstructionGenerator,
    DeleteInstructionGenerator,
    SwapInstructionGenerator
]