"""
String Utilities Module
Provides string manipulation functions
"""


def reverse(text):
    """Reverse a string"""
    return text[::-1]


def count_vowels(text):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def capitalize_words(text):
    """Capitalize first letter of each word"""
    return text.title()


def is_palindrome(text):
    """Check if text is a palindrome (reads same forwards and backwards)"""
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]


def count_words(text):
    """Count number of words in text"""
    return len(text.split())


def remove_spaces(text):
    """Remove all spaces from text"""
    return text.replace(" ", "")


def to_snake_case(text):
    """Convert text to snake_case"""
    return text.lower().replace(" ", "_")


def to_camel_case(text):
    """Convert text to camelCase"""
    words = text.split()
    if not words:
        return ""
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])


def truncate(text, length=10, suffix="..."):
    """Truncate text to specified length and add suffix"""
    if len(text) <= length:
        return text
    return text[:length] + suffix


def count_characters(text, char):
    """Count occurrences of a character in text"""
    return text.count(char)


# Module metadata
__version__ = "1.0.0"
__author__ = "Python Series"


# Test code (runs only when executed directly)
if __name__ == "__main__":
    print("📝 String Utils Module - Testing")
    print(f"reverse('Python') = {reverse('Python')}")
    print(f"count_vowels('Hello World') = {count_vowels('Hello World')}")
    print(f"capitalize_words('hello world') = {capitalize_words('hello world')}")
    print(f"is_palindrome('racecar') = {is_palindrome('racecar')}")
    print(f"count_words('This is a test') = {count_words('This is a test')}")
    print(f"remove_spaces('Hello World') = {remove_spaces('Hello World')}")
    print(f"to_snake_case('Hello World') = {to_snake_case('Hello World')}")
    print(f"to_camel_case('hello world') = {to_camel_case('hello world')}")
    print(f"truncate('Python Programming', 10) = {truncate('Python Programming', 10)}")
    print(
        f"count_characters('Mississippi', 's') = {count_characters('Mississippi', 's')}"
    )
