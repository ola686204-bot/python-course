# REVIEW.md

## Code Quality Review

### 1. Variable names were unclear

**Before**

```python
x_float
y_float
Score
```

**After**

```python
first_number
second_number
results
```

**Why**

The new names clearly describe what each variable represents and follow the snake_case naming convention.

---

### 2. Magic number used

**Before**

```python
round(result_add, 2)
```

**After**

```python
DECIMAL_PLACES = 2

round(result_add, DECIMAL_PLACES)
```

**Why**

The value `2` was a magic number. It is now stored in a named constant to improve readability and make future changes easier.

---

### 3. Code was not divided into functions

**Before**

All calculations and printing were written in one long block.

**After**

```python
get_number()
validate_number()
calculate_results()
display_results()
display_summary()
main()
```

**Why**

Each function now performs one specific task, making the program easier to understand, test, and maintain.

---

### 4. No early return after invalid input

**Before**

```python
except ValueError:
    print("Invalid input.")
```

The program continued executing, which could cause errors because the variables were never assigned.

**After**

```python
if first_number is None:
    return
```

**Why**

Using early returns stops the program immediately when invalid input is detected.

---

### 5. Repeated print statements

**Before**

```python
print(...)
print(...)
print(...)
```

Seven separate print statements displayed each result.

**After**

```python
for operation, value in results.items():
    print(f"{operation}: {round(value, DECIMAL_PLACES)}")
```

**Why**

A loop removes duplicated code and makes the program easier to extend and maintain.

---

### 6. Variable naming did not follow PEP 8

**Before**

```python
Score = [...]
```

**After**

```python
results = {...}
```

**Why**

Variable names should use snake_case. `Score` violated the PEP 8 naming convention.

---

### 7. Program entry point

**Before**

The program executed immediately when imported.

**After**

```python
if __name__ == "__main__":
    main()
```

**Why**

Using a `main()` function and the `if __name__ == "__main__":` guard follows Python best practices and improves code organization.
