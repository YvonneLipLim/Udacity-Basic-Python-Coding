"""
Importing local scripts allows you to reuse code from other Python files in your project. An example of an import statement:
from package1.module1 import my_function

Ways to Import Local Scripts:
1. Direct Import: Import a script directly using its filename.
   import my_script
2. Import Specific Functions or Variables
   from my_script import my_function, my_variable
3. Import All Functions and Variables
   from my_script import *

Key Points to Note:
1. File Location: Ensure the script is in the same directory or a subdirectory.
2. File Name: Use the correct filename (with `.py` extension).
3. Module Name: Use the correct module name (without `.py` extension).
4. Import Order: Import local scripts after standard library imports.
5. Circular Imports: Avoid circular imports (importing script A in script B and vice versa).
6. Relative Imports: Use relative imports for scripts within the same package.
7. Package Structure: Organize scripts into packages and subpackages.
8. Use `__init__.py` files to define package structure.
9. Use `importlib` module for dynamic imports.
10. Use a linter or IDE to detect import errors.

Example Directory Structure:
my_project/
    __init__.py
    script1.py
    script2.py
    package1/
        __init__.py
        module1.py
        module2.py
    package2/
        __init__.py
        module3.py
        module4.py
"""
