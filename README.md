# AI Tools Lab

## 1. Project Description

**AI Tools Lab** is a beginner-friendly Python project created for a college lab exercise. It contains a collection of simple, well-documented Python functions and algorithms, including:

- A **Bubble Sort** algorithm implementation
- Utility functions:
  - `is_palindrome()` — checks if a given string is a palindrome
  - `count_words()` — counts the number of words in a given text
  - `celsius_to_fahrenheit()` — converts a temperature from Celsius to Fahrenheit

This project is intended to demonstrate basic Python programming concepts such as loops, conditionals, string manipulation, and simple math operations.

## 2. Installation Instructions

No external libraries are required — this project uses only Python's standard library.

**Steps:**

1. Make sure Python 3.x is installed on your system. You can check by running:
   ```bash
   python --version
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ai-tools-lab.git
   ```
3. Navigate into the project folder:
   ```bash
   cd ai-tools-lab
   ```
4. Run the project files directly using Python:
   ```bash
   python main.py
   ```

## 3. Usage Examples

### Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

numbers = [5, 2, 9, 1, 5, 6]
print(bubble_sort(numbers))
# Output: [1, 2, 5, 5, 6, 9]
```

### is_palindrome()

```python
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print(is_palindrome("Madam"))
# Output: True

print(is_palindrome("Hello"))
# Output: False
```

### count_words()

```python
def count_words(text):
    return len(text.split())

print(count_words("This is an AI Tools Lab project"))
# Output: 6
```

### celsius_to_fahrenheit()

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(25))
# Output: 77.0
```

## 4. Contributors

- Vanshika Verma

## 5. License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this code for educational or personal purposes.