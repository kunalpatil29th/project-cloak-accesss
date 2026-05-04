# Tests Module

Unit tests for Project Cloak Access.

## Concepts Covered

- **Unit Testing**: Testing individual components in isolation
- **Test Automation**: Automated verification of code correctness
- **Assertions**: Validating expected outcomes

## Running Tests

### Using unittest (built-in)

```bash
python -m unittest discover tests
```

Or run specific test file:

```bash
python -m unittest tests/test_cloak.py
```

### Verbose Mode

```bash
python -m unittest discover tests -v
```

## Test Files

- `test_cloak.py`: Tests for configuration settings and core functionality

## Writing New Tests

1. Create a new test file in `tests/` directory
2. Name it `test_*.py`
3. Import `unittest` and your module
4. Create a test class inheriting from `unittest.TestCase`
5. Write test methods starting with `test_`

Example:

```python
import unittest

class TestMyModule(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1 + 1, 2)

if __name__ == "__main__":
    unittest.main()
```
