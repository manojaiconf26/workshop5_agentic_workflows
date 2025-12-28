"""
Palindrome Checker Function
==========================

A palindrome is a word, phrase, number, or other sequence of characters that reads
the same forward and backward. Examples include "racecar", "A man a plan a canal Panama",
and "Madam".

This module provides functions to check if strings are palindromes.
"""

def is_palindrome(text):
    """
    Check if a string is a palindrome (reads the same forwards and backwards).
    
    This function ignores case, spaces, and punctuation when checking for palindromes,
    focusing only on the alphanumeric characters.
    
    Args:
        text (str): The string to check for palindrome properties
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
        
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("hello")
        False
    """
    # Convert to lowercase and keep only alphanumeric characters
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    
    # Compare the string with its reverse
    return cleaned == cleaned[::-1]


def is_palindrome_simple(text):
    """
    Simple palindrome checker that considers exact string matching.
    
    This version is case-sensitive and includes all characters including spaces
    and punctuation.
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if the string is exactly the same forwards and backwards
        
    Examples:
        >>> is_palindrome_simple("racecar")
        True
        >>> is_palindrome_simple("Racecar")
        False
        >>> is_palindrome_simple("12321")
        True
    """
    return text == text[::-1]


def demonstrate_palindromes():
    """
    Demonstrate the palindrome checker with various examples.
    """
    test_cases = [
        "racecar",
        "A man a plan a canal Panama",
        "race a car", 
        "Madam",
        "Was it a car or a cat I saw?",
        "hello world",
        "12321",
        "12345"
    ]
    
    print("Palindrome Analysis Results:")
    print("=" * 50)
    
    for test in test_cases:
        result = is_palindrome(test)
        simple_result = is_palindrome_simple(test)
        
        print(f"Text: '{test}'")
        print(f"  Advanced check (ignoring case/punctuation): {result}")
        print(f"  Simple check (exact matching): {simple_result}")
        
        if result:
            cleaned = ''.join(char.lower() for char in test if char.isalnum())
            print(f"  Cleaned version: '{cleaned}'")
        
        print("-" * 30)


# Additional educational function
def explain_palindrome_concept():
    """
    Provide an educational explanation of palindromes.
    """
    explanation = """
    PALINDROMES IN ENGLISH LANGUAGE
    ===============================
    
    A palindrome is a fascinating linguistic phenomenon where words, phrases, or 
    sentences read the same forwards and backwards. The term comes from the Greek 
    words 'palin' (meaning 'again') and 'dromos' (meaning 'way' or 'direction').
    
    Types of Palindromes:
    
    1. Single Words:
       - racecar, level, radar, civic, rotor
    
    2. Phrases (ignoring spaces and punctuation):
       - "A man a plan a canal Panama"
       - "Madam, I'm Adam"
       - "Was it a car or a cat I saw?"
    
    3. Names:
       - Hannah, Otto, Ada
    
    4. Numbers:
       - 12321, 1001, 7337
    
    Palindromes demonstrate the playful and artistic nature of language, often
    used in wordplay, literature, and puzzles. They challenge our understanding
    of symmetry in written communication.
    """
    
    return explanation


if __name__ == "__main__":
    # Run demonstrations when the script is executed directly
    print(explain_palindrome_concept())
    print("\n")
    demonstrate_palindromes()