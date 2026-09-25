def is_palindrome(s):
    """Check whether s reads the same forwards and backwards.

    The check ignores capitalization, spaces, and punctuation.
    """
    cleaned = "".join(character.lower() for character in s if character.isalnum())
    return cleaned == cleaned[::-1]


def count_words(text):
    """Count the words in text.

    Words are separated by whitespace, such as spaces or newlines.
    """
    return len(text.split())


def celsius_to_fahrenheit(c):
    """Convert a temperature from Celsius to Fahrenheit.

    Args:
        c: The temperature in degrees Celsius.

    Returns:
        The temperature in degrees Fahrenheit.
    """
    return (c * 9 / 5) + 32