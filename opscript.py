import parser
import os
import time
import sys

def current_milli_time():
    return round(time.time() * 1000)

def show_help_page():
    print("""
        OPScript Help
        
        * python opscript.py run <file>
        * python opscript.py build <file>
        
        Arguments:
        -h | Shows this help menu
        -d | Enables debug mode
        """)
    
    exit()

if len(sys.argv) == 1 or "-h" in sys.argv:
    show_help_page()
    
parser.DEBUG = "-d" in sys.argv

if sys.argv[1] == "run":
    mode = "run"
elif sys.argv[1] == "build":
    mode = "build"
else:
    show_help_page()
    
file = sys.argv[2]

if not os.path.exists(file):
    print("The file you specified does not exist.")
    exit()
    
# Read and parse the OPScript file we want to build
with open(file, "r") as f:
    script = f.read()
    
code = parser.parse(script)

# Build the go code into an exe
build_name = f"{current_milli_time()}"
with open(f"{build_name}.go", "w") as f:
    f.write(code)
    
os.system(f"go {mode} {build_name}.go")
os.remove(f"{build_name}.go")

if mode == "build":
    print(f"File saved as {build_name}.exe")