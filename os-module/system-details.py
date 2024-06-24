# Get os version, machinetype, architecture type, processor name, python implementation

import platform
import sys

info={
    "architecture": platform.architecture(executable=sys.executable,bits='',linkage=''),
    "processor": platform.processor(),
    "compiler": platform.python_compiler(),
    "python_implementation": platform.python_implementation(),
    "os_type": platform.system()
}

for key,val in info.items():
    print(key, " : " , val)