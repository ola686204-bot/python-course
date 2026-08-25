# Code Quality Report
## Part 1 - PEP 8 Compliance
### Flake8 Before Fixes

The following violations where found when flake8 was run before making any code quality changes:
.\Advanced_Text.py:3:32: W291 trailing whitespace
.\Advanced_Text.py:7:1: E302 expected 2 blank lines, found 1
.\Advanced_Text.py:9:1: W293 blank line contains whitespace
.\Advanced_Text.py:12:1: W293 blank line contains whitespace
.\Advanced_Text.py:22:1: E302 expected 2 blank lines, found 1
.\Advanced_Text.py:24:1: W293 blank line contains whitespace
.\Advanced_Text.py:27:1: W293 blank line contains whitespace
.\Advanced_Text.py:29:80: E501 line too long (96 > 79 characters)
.\Advanced_Text.py:34:1: E302 expected 2 blank lines, found 1
.\Advanced_Text.py:37:1: W293 blank line contains whitespace
.\Advanced_Text.py:40:1: W293 blank line contains whitespace
.\Advanced_Text.py:46:1: E302 expected 2 blank lines, found 1
.\Advanced_Text.py:48:1: W293 blank line contains whitespace
.\Advanced_Text.py:53:1: W293 blank line contains whitespace
.\Advanced_Text.py:59:1: E302 expected 2 blank lines, found 1
.\Advanced_Text.py:61:1: W293 blank line contains whitespace
.\Advanced_Text.py:64:1: W293 blank line contains whitespace
.\Advanced_Text.py:69:16: E225 missing whitespace around operator
.\Advanced_Text.py:73:23: W291 trailing whitespace
.\Advanced_Text.py:75:1: E302 expected 2 blank lines, found 1
.\Advanced_Text.py:76:55: W291 trailing whitespace
.\Advanced_Text.py:79:1: W293 blank line contains whitespace
.\Advanced_Text.py:93:1: E302 expected 2 blank lines, found 1
.\Advanced_Text.py:124:1: E302 expected 2 blank lines, found 0
.\Advanced_Text.py:125:9: E117 over-indented
.\Advanced_Text.py:128:1: E305 expected 2 blank lines after class or function definition, found 1
.\Advanced_Text.py:129:11: W291 trailing whitespace
.\Advanced_Text.py:129:12: W292 no newline at end of file
.\Continous_Calculator.py:12:1: E302 expected 2 blank lines, found 1
.\Continous_Calculator.py:18:7: E111 indentation is not a multiple of 4
.\Continous_Calculator.py:19:7: E111 indentation is not a multiple of 4
.\Continous_Calculator.py:22:1: W293 blank line contains whitespace
.\Continous_Calculator.py:23:7: E111 indentation is not a multiple of 4
.\Continous_Calculator.py:24:1: W293 blank line contains whitespace
.\Continous_Calculator.py:26:8: E111 indentation is not a multiple of 4
.\Continous_Calculator.py:27:8: E111 indentation is not a multiple of 4
.\Continous_Calculator.py:29:1: E305 expected 2 blank lines after class or function definition, found 1
.\Continous_Calculator.py:44:7: E111 indentation is not a multiple of 4
.\Continous_Calculator.py:49:7: E111 indentation is not a multiple of 4
.\Continous_Calculator.py:50:7: E111 indentation is not a multiple of 4
.\Continous_Calculator.py:53:16: E225 missing whitespace around operator
.\Continous_Calculator.py:54:7: E111 indentation is not a multiple of 4
.\Continous_Calculator.py:55:7: E111 indentation is not a multiple of 4
.\Continous_Calculator.py:56:1: W293 blank line contains whitespace
.\Continous_Calculator.py:58:7: E111 indentation is not a multiple of 4
.\Continous_Calculator.py:59:7: E111 indentation is not a multiple of 4
.\Continous_Calculator.py:60:1: W293 blank line contains whitespace
.\Continous_Calculator.py:64:7: E111 indentation is not a multiple of 4
.\Continous_Calculator.py:65:1: W293 blank line contains whitespace
.\Continous_Calculator.py:66:20: E231 missing whitespace after ','
.\Continous_Calculator.py:66:22: E231 missing whitespace after ','
.\Continous_Calculator.py:67:7: E111 indentation is not a multiple of 4
.\Continous_Calculator.py:69:7: E111 indentation is not a multiple of 4
.\Continous_Calculator.py:72:6: E111 indentation is not a multiple of 4
.\Robustcalculator.py:15:22: E231 missing whitespace after ','
.\Robustcalculator.py:15:27: E231 missing whitespace after ','
.\Robustcalculator.py:20:22: E231 missing whitespace after ','
.\Robustcalculator.py:20:27: E231 missing whitespace after ','
.\Robustcalculator.py:33:53: E231 missing whitespace after ','
.\Robustcalculator.py:34:61: E231 missing whitespace after ','
.\Robustcalculator.py:35:64: E231 missing whitespace after ','
.\Robustcalculator.py:36:58: E231 missing whitespace after ','
.\Robustcalculator.py:37:64: E231 missing whitespace after ','
.\Robustcalculator.py:38:57: E231 missing whitespace after ','
.\Robustcalculator.py:39:70: E231 missing whitespace after ','
.\Robustcalculator.py:41:6: E225 missing whitespace around operator
.\Robustcalculator.py:41:80: E501 line too long (97 > 79 characters)
.\Robustcalculator.py:45:60: W292 no newline at end of file
.\Simplecalculator.py:2:32: W291 trailing whitespace
.\Simplecalculator.py:8:1: E265 block comment should start with '# '
.\Simplecalculator.py:11:1: E265 block comment should start with '# '
.\Simplecalculator.py:14:1: E265 block comment should start with '# '
.\Simplecalculator.py:17:1: E265 block comment should start with '# '
.\Simplecalculator.py:20:1: E265 block comment should start with '# '
.\Simplecalculator.py:23:1: E265 block comment should start with '# '
.\Simplecalculator.py:26:1: E265 block comment should start with '# '
.\Simplecalculator.py:27:67: W292 no newline at end of file
.\Smartcalculator.py:2:38: W291 trailing whitespace
.\Smartcalculator.py:7:1: E302 expected 2 blank lines, found 1
.\Smartcalculator.py:9:25: E231 missing whitespace after ','
.\Smartcalculator.py:9:29: E231 missing whitespace after ','
.\Smartcalculator.py:9:33: E231 missing whitespace after ','
.\Smartcalculator.py:9:37: E231 missing whitespace after ','
.\Smartcalculator.py:9:41: E231 missing whitespace after ','
.\Smartcalculator.py:9:45: E231 missing whitespace after ','
.\Smartcalculator.py:15:1: E302 expected 2 blank lines, found 1
.\Smartcalculator.py:15:38: E251 unexpected spaces around keyword / parameter equals
.\Smartcalculator.py:16:80: E501 line too long (135 > 79 characters)
.\Smartcalculator.py:20:1: W293 blank line contains whitespace
.\Smartcalculator.py:21:9: W291 trailing whitespace
.\Smartcalculator.py:22:12: E225 missing whitespace around operator
.\Smartcalculator.py:23:23: W291 trailing whitespace
.\Smartcalculator.py:26:40: E231 missing whitespace after ','
.\Smartcalculator.py:29:1: W293 blank line contains whitespace
.\Smartcalculator.py:34:1: E302 expected 2 blank lines, found 1
.\Smartcalculator.py:43:6: E114 indentation is not a multiple of 4 (comment)
.\Smartcalculator.py:43:6: E116 unexpected indentation (comment)
.\Smartcalculator.py:47:15: E261 at least two spaces before inline comment
.\Smartcalculator.py:48:1: W293 blank line contains whitespace
.\Smartcalculator.py:49:36: W291 trailing whitespace
.\Smartcalculator.py:54:1: W293 blank line contains whitespace
.\Smartcalculator.py:55:37: W291 trailing whitespace
.\Smartcalculator.py:57:80: E501 line too long (96 > 79 characters)
.\Smartcalculator.py:60:1: W293 blank line contains whitespace
.\Smartcalculator.py:73:22: E221 multiple spaces before operator
.\Smartcalculator.py:78:19: E225 missing whitespace around operator
.\Smartcalculator.py:80:14: E225 missing whitespace around operator
.\Smartcalculator.py:81:9: E701 multiple statements on one line (colon)
.\Smartcalculator.py:82:5: F841 local variable 'result' is assigned to but never used
.\Smartcalculator.py:83:5: F841 local variable 'label' is assigned to but never used
.\Smartcalculator.py:85:34: W291 trailing whitespace
.\Smartcalculator.py:87:1: E305 expected 2 blank lines after class or function definition, found 1
.\Testing.py:9:14: E211 whitespace before '('
.\Testing.py:9:29: E231 missing whitespace after ','
.\Testing.py:10:11: F541 f-string is missing placeholders
.\Testing.py:10:40: E202 whitespace before ')'
.\Testing.py:12:11: F541 f-string is missing placeholders
.\Testing.py:14:14: E211 whitespace before '('
.\Testing.py:14:29: E231 missing whitespace after ','
.\Testing.py:15:11: F541 f-string is missing placeholders
.\Testing.py:17:11: F541 f-string is missing placeholders
.\Testing.py:27:53: E231 missing whitespace after ','
.\Testing.py:28:61: E231 missing whitespace after ','
.\Testing.py:28:67: W291 trailing whitespace
.\Testing.py:29:64: E231 missing whitespace after ','
.\Testing.py:30:58: E231 missing whitespace after ','
.\Testing.py:31:70: E231 missing whitespace after ','
.\Testing.py:32:65: E231 missing whitespace after ','
.\Testing.py:33:58: E231 missing whitespace after ','
.\Testing.py:33:64: W292 no newline at end of file
.\clean_calculator.py:141:1: W293 blank line contains whitespace
.\clean_calculator.py:141:5: W292 no newline at end of file
.\hello.py:9:29: W291 trailing whitespace
.\hello.py:10:12: W291 trailing whitespace
.\hello.py:11:19: W291 trailing whitespace
.\hello.py:12:70: W291 trailing whitespace
.\hello.py:13:42: W291 trailing whitespace
.\hello.py:14:58: W291 trailing whitespace
.\hello.py:15:8: E261 at least two spaces before inline comment
.\hello_world.py:2:25: W292 no newline at end of file
.\menu_calculator.py:178:11: W292 no newline at end of file
.\modular_calculator.py:17:24: E231 missing whitespace after ','
.\modular_calculator.py:17:26: E231 missing whitespace after ','
.\modular_calculator.py:20:8: E211 whitespace before '('
.\modular_calculator.py:24:1: E302 expected 2 blank lines, found 1
.\modular_calculator.py:24:13: E211 whitespace before '('
.\modular_calculator.py:25:4: E111 indentation is not a multiple of 4
.\modular_calculator.py:26:4: E111 indentation is not a multiple of 4
.\modular_calculator.py:26:16: W291 trailing whitespace
.\modular_calculator.py:28:1: E302 expected 2 blank lines, found 1
.\modular_calculator.py:28:13: E211 whitespace before '('
.\modular_calculator.py:32:1: E302 expected 2 blank lines, found 1
.\modular_calculator.py:32:11: E211 whitespace before '('
.\modular_calculator.py:38:1: E302 expected 2 blank lines, found 1
.\modular_calculator.py:38:17: E211 whitespace before '('
.\modular_calculator.py:44:1: E302 expected 2 blank lines, found 1
.\modular_calculator.py:44:12: E211 whitespace before '('
.\modular_calculator.py:50:1: E302 expected 2 blank lines, found 1
.\modular_calculator.py:50:17: E211 whitespace before '('
.\modular_calculator.py:63:1: E302 expected 2 blank lines, found 1
.\modular_calculator.py:74:9: E303 too many blank lines (2)
.\modular_calculator.py:78:29: W291 trailing whitespace
.\modular_calculator.py:86:32: E231 missing whitespace after ','
.\modular_calculator.py:117:21: W291 trailing whitespace
.\modular_calculator.py:131:31: W291 trailing whitespace
.\modular_calculator.py:134:24: W291 trailing whitespace
.\modular_calculator.py:156:35: E201 whitespace after '('
.\modular_calculator.py:156:48: E231 missing whitespace after ','
.\modular_calculator.py:165:42: E231 missing whitespace after ','
.\modular_calculator.py:175:30: W291 trailing whitespace
.\modules\calculator.py:21:17: W292 no newline at end of file
.\modules\greeting.py:3:29: W292 no newline at end of file
.\recursion_lab.py:154:22: W291 trailing whitespace
.\recursion_lab.py:154:82: W292 no newline at end of file
.\text_processor.py:89:11: W292 no newline at end of file


### Pycodestyle Statistics - After Fixes
command used:
pycodestyle --statistics .

Output:
No output - pep 8  violations found.

## Part 2 - Readability Improvements

The project was reviewed for readability, naming, abstraction, comments, and consistency. The following improvement were made.

### Improvement 1 -Renamed 'Exponentiate' to 'exponentiate'
Improvement:

The function name was changed from:

Exponentiate()

to:

exponentiate()

Property addressed: Naming

Reason:

Python functions should use snake_case. The new name is also consistent
with the other calculator functions such as add(), subtract(),
multiply(), and divide().

### Improvement 2 — Corrected QUIT_OPTION

Variable: QUIT_OPTION

Improvement:

The original code used:

QUIT_OPTION = len("OPERATIONS")

This was changed to:

QUIT_OPTION = len(OPERATIONS)

Property addressed: Naming and consistency

Reason:

The program needs the number of items in the OPERATIONS list rather than
the number of characters in the word "OPERATIONS". Using the list directly
makes the purpose of the constant clearer and prevents the quit option from
being incorrect.

### Improvement 3 — Improved number variable names

Variables: first_number and second_number

Improvement:

Less descriptive variable names were replaced with:

first_number
second_number

Property addressed: Naming

Reason:

These names clearly describe what each value represents. This makes the
program easier to understand without having to examine where the values
came from.

### Improvement 4 — Improved calculator function structure

Functions:

add()
subtract()
multiply()
divide()
floor_divide()
modulus()
exponentiate()

Improvement:

Each arithmetic operation is handled by its own function instead of putting
all calculations into one large block of code.

Property addressed: Abstraction

Reason:

Separating the operations makes the program easier to read, test, debug,
and maintain. Each function has one clear responsibility.

### Improvement 5 — Replaced a magic value with a named constant

Variable: QUIT_OPTION

Improvement:

Instead of relying on a hard-coded menu number, the program uses:

QUIT_OPTION = len(OPERATIONS)

Property addressed: Maintainability and consistency

Reason:

The named constant explains what the value represents. It also means that
if another operation is added to the menu, the quit option can update
automatically.

### Improvement 6 — Removed comments that repeated the code

Files: Calculator programs

Improvement:

Comments such as:

# This is a basic Arithmetic that perform addition

were removed or reduced because the code already clearly showed the
operation being performed.

Property addressed: Comments

Reason:

Comments should provide useful information that is not immediately obvious
from the code. Comments that simply repeat the code make programs longer
without making them easier to understand.

### Improvement 7 — Improved comments

Files: Calculator programs

Improvement:

Unnecessary comments were removed, while useful comments were kept where
they helped explain the purpose or reasoning behind the code.

Property addressed: Comments

Reason:

Good comments should explain why something is being done rather than simply
describe what the code is doing.

### Improvement 8 — Improved whitespace and formatting consistency

Files: Project Python files

Improvement:

Spacing around operators, commas, indentation, blank lines, and line endings
were corrected throughout the project.

Property addressed: Consistency

Reason:

Consistent formatting makes code easier to read and helps different parts of
the project follow the same coding style.

| # | Improvement                                    | Property             |
| - | ---------------------------------------------- | -------------------- |
| 1 | Renamed `Exponentiate` to `exponentiate`       | Naming               |
| 2 | Corrected `QUIT_OPTION`                        | Naming / Consistency |
| 3 | Improved number variable names                 | Naming               |
| 4 | Separated calculator operations into functions | Abstraction          |
| 5 | Replaced a magic value with a named constant   | Maintainability      |
| 6 | Removed comments that repeated the code        | Comments             |
| 7 | Improved comments to explain purpose           | Comments             |
| 8 | Improved whitespace and formatting consistency | Consistency          |

A total of eight readability improvements were documented.

### Part 3 
## Help ()
# Help(add)
 Output:
 Help on function add in module modular_calculator:                                                                                          

add(a, b)
    Return the sum of two numbers.                                                                                                          
# Help(subtract)
 Output:
 Help on function add in module modular_calculator:                                                                                          

add(a, b)
    Return the sum of two numbers.                                                                                                          
# Help(exponentiate)
 Output:
 Help on function exponentiate in module modular_calculator:                                                                                 

exponentiate(a, b)
    Return a raised to the power of b.    
