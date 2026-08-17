# Debugging Lab

## Part 1 — Runtime Errors

## 1. IndexError — get_first_item()

### Broken Code

```python
def get_first_item(items):
    """Return the first item from a list."""
    return items[5]
# Test
print(get_first_item(["apple", "banana"]))