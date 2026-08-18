**Python Feature Workflow Project**

*What the Project Does*
This project demonstrates a Git feature-branch workflow while implementing a greeting tool and basic calculator operations.

*How to Run*
Run the greeting tool with:
**For Addition**
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

**For subtraction**
def subtract(a, b):
    """Subtract the second number from the first number.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference between the two numbers.
    """
    return a - b

**For Multiplication**
def multiply(a, b):
    """Return the product the product of two numbers."""
    return a * b
   

**Directory Structure**
project/
|-- modules/
|   |--__init__.py
|   |--greeting.py
|   |--calculator.py
|--main_greeting.py
|--README.md
|--DECISIONS.md
WORKFLOW_LOG.md

**Features
- Greeting function
- Addition
- Subtraction
- Multiplication
- Google-style docstrings
- Git feature branches
- Atomic commits
- Feature branch merges
