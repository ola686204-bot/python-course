# Debugging Lab

## Part 1 — Runtime Errors

## 1. IndexError — get_first_item()

### Broken Code


def get_first_item(items):
    """Return the first item from a list."""
    return items[5]

* Test
print(get_first_item(["apple", "banana"]))

* Full Traceback
Traceback (most recent call last):
  File "c:\Users\USER\Documents\python-course\debugging_lab.py", line 12, in <module>
    print(get_first_item(["apple", "banana"]))
          ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\USER\Documents\python-course\debugging_lab.py", line 11, in get_first_item
    return items[5]
           ~~~~~^^^
IndexError: list index out of range

* Traceback Annotation
the traceback shows that an IndexError occured.
The function get_first_item() attempted to access index 5.

The list only contains two items:
*apple is at index 0.
*banana is at index 1.
Therefore, index 5 does not exist.
* The root cause is:
return items[5]
* Fix
I changed:
return items[5]
to:
return items[0]
* Verification
assert get_first_item(["apple", "banana"]) == "apple"
The assertion passed, confirming that the function now returns the correct first item.



---

# 2. KeyError

** 2. KeyError — get_student_name()

### Broken Code

def get_student_name(student):
    """Return the student's name."""
    return student["fullname"]
* Test
    print(get_student_name({"name": "John", "age": 20}))

* Full Traceback
Traceback (most recent call last):
  File "c:\Users\USER\Documents\python-course\debugging_lab.py", line 4, in <module>
    print(get_student_name({"name": "John", "age": 20}))
          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\USER\Documents\python-course\debugging_lab.py", line 3, in get_student_name
    return student["fullname"]
           ~~~~~~~^^^^^^^^^^^^
KeyError: 'fullname'

* Traceback Annotation
The traceback identifies the get_student_name() function as
the location where the error occurred.
* The Root cause is the incorrect dictionary key.
"name"
* Fix
I changed:
    return student['fullname"]
to:
    return student["name"]
* Verification
    assert get_student_name({"name": "John"}) == "John"
The assertion passed, confirming the fix.


---

## 3. TypeError — add_numbers()

### Broken Code

def add_numbers(a, b):
    """Add two numbers."""
    return a + b

* Test 
    print(add_numbers(10, "5"))

* Full Traceback
T raceback (most recent call last):
  File "c:\Users\USER\Documents\python-course\debugging_lab.py", line 4, in <module>
    print(add_numbers(10, "5"))
          ~~~~~~~~~~~^^^^^^^^^
  File "c:\Users\USER\Documents\python-course\debugging_lab.py", line 3, in add_numbers
    return a + b
           ~~^~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'

* Traceback Annotation
The traceback points to the addition operation inside
add_numbers().

* Fix
I converted the second value o an integer:
    return a + int(b)

* Verification
    assert add_numbers(10, "5") == 15
The assertion passed, confirming that the function now produces the correct result.


---

## 4. AttributeError — make_uppercase()

### Broken Code

def make_uppercase(word):
    """Return a word in uppercase."""
    return word.uppercase()

* Test
    print(make_uppercase("hello"))

* Full Traceback
Traceback (most recent call last):
  File "c:\Users\USER\Documents\python-course\debugging_lab.py", line 4, in <module>
    print(make_uppercase("hello"))
          ~~~~~~~~~~~~~~^^^^^^^^^
  File "c:\Users\USER\Documents\python-course\debugging_lab.py", line 3, in make_uppercase
    return word.uppercase()
           ^^^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'uppercase'

* Traceback Annotation
The traceback points to the upercase() method,
Python strings do not have a method called uppercase()

* Fix
I changed:
    return word.uppercase()
to:
    return word.upper()

* Verification
    assert make_uppercase("hello") == "HELLO"
The assertion passed, confirming the fix.


---

## 5. NameError — calculate_total()

### Broken Code

def calculate_total(price, quantity):
    """Calculate the total price."""
    return price * quanity

* Test
    print(calculate_total(10, 3))

* Full Traceback
Traceback (most recent call last):
  File "c:\Users\USER\Documents\python-course\debugging_lab.py", line 4, in <module>
    print(calculate_total(10, 3))
          ~~~~~~~~~~~~~~~^^^^^^^
  File "c:\Users\USER\Documents\python-course\debugging_lab.py", line 3, in calculate_total
    return price * quanity
                   ^^^^^^^
NameError: name 'quanity' is not defined. Did you mean: 'quantity'?

* Traceback Annotation
The function receives a parameter called:
    quantity
However, the calculation uses:
    quanity

* Fix 
I changed:
    quanity
to:
    quantity

* Verification
    assert calculate_total(10, 3) == 30
The assertion passed, confirming the fix.


---
# Part 2 — Logical Errors

## 6. Off-by-One Error — count_numbers()

### Broken Code

def count_numbers(numbers):
    """Return the number of items in a list."""
    count = 0

    for index in range(len(numbers) - 1):
        count += 1

    return count

* Test
    count_numbers([10, 20, 30])
* Symptom
The function returned:
    2
but the expected result was:
    3

| Step             |       Index | Count |
| ---------------- | ----------: | ----: |
| Start            |           - |     0 |
| First iteration  |           0 |     1 |
| Second iteration |           1 |     2 |
| Third item       | Not reached |     2 |

* Hypothesis
I suspected an off-by-one error because the loop stopped before
processing the final item.

The problem was:
    range(len(numbers) - 1)

Before-Fix Assertion
    assert count_numbers([10, 20, 30]) != 3
This assertion confirmed that the function was producing the
wrong result.

* Fix
I changed:
    range(len(numbers) - 1)
to:
    range(len(numbers))

After-Fix Assertion
    assert count_numbers([10, 20, 30]) == 3
The assertion passed


---
## 7. Wrong Operator — calculate_area()

### Broken Code

def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length + width
* Test
    calculate_area(5, 4)
* Symptom
The function returned:
    9
The expected area was:
    20
* Trace Table
| Step | Length | Width | Operation | Result |
| ---- | -----: | ----: | --------- | -----: |
| 1    |      5 |     4 | 5 + 4     |      9 |
* Hypothesis
I suspected that the wrong arithmetic operator was being used.
The are of a rectangle should be:
    length * width
not:
    length + width

* Before-Fix Assertion
    assert calculate_area(5, 4) != 20
* Fix 
I changed:
    return length + width
to:
return length * width
* After-Fix Assertion
    assert calculate_area(5, 4) == 20
The assertion passed.


---
## 8. Reversed Condition — check_age()

### Broken Code
def check_age(age):
    """Check whether someone is old enough."""
    if age < 18:
        return "Allowed"

    return "Not allowed"
* Test
    check_age(15)
* Symptom
The function returned:
    Allowed
for age 15.
The expected result was:
    Not allowed
* Trace Table
| Step | Age | Condition       | Result  |
| ---- | --: | --------------- | ------- |
| 1    |  15 | 15 < 18 is True | Allowed |
* Hypothesis
I suspected that the condition had been reversed.
The function should allow people who are 18 or older.
* Before-Fix Assertion
    assert check_age(15) != "Not alowed"
* Fix
I Changed:
    if age <18:
to:
    if age >= 18:
After-Fix Assertions
    assert check_age(15) == "Not allowed"
    assert check_age(20) == "Allowed"
Both assertion passed.


---
## 9. Missing Return — multiply()

### Broken Code
def multiply(a, b):
    """Multiply two numbers."""
    result = a * b

* Test
    multiply(4, 5)
* Symptom
The function returned:
    None
instead of:
    20
* Trace Table
| Step | Operation           | Result |
| ---- | ------------------- | -----: |
| 1    | a = 4               |      4 |
| 2    | b = 5               |      5 |
| 3    | a * b               |     20 |
| 4    | No return statement |   None |

* Hypothesis
I suspected that the calculation was correct but the result
was not being returned from the function.
* Before-Fix Assertion
    assert multiply(4, 5) is None
This confirmed that the function returned None.
* Fix
I added:
    return result
* After-Fix Assertion
    assert multiply(4, 5) == 20
The assertion passed, confirming the fix.