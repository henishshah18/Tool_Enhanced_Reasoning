from typing import List
import re

class StringTools:
    """Class containing string manipulation tool functions."""
    
    def count_vowels(self, text: str) -> int:
        """
        Count the number of vowels in a string.
        
        Args:
            text: String to count vowels in
            
        Returns:
            Number of vowels in the string
        """
        return sum(1 for char in text.lower() if char in 'aeiou')
    
    def count_letters(self, text: str) -> int:
        """
        Count the number of letters in a string (excluding spaces and punctuation).
        
        Args:
            text: String to count letters in
            
        Returns:
            Number of letters in the string
        """
        return sum(1 for char in text if char.isalpha())
    
    def count_words(self, text: str) -> int:
        """
        Count the number of words in a string.
        
        Args:
            text: String to count words in
            
        Returns:
            Number of words in the string
        """
        return len(text.split())
    
    def extract_numbers(self, text: str) -> List[float]:
        """
        Extract all numbers from a string.
        
        Args:
            text: String to extract numbers from
            
        Returns:
            List of numbers found in the string
        """
        return [float(num) for num in re.findall(r'-?\d+\.?\d*', text)]
    
    def compare_string_lengths(self, text1: str, text2: str) -> str:
        """
        Compare the lengths of two strings.
        
        Args:
            text1: First string
            text2: Second string
            
        Returns:
            String describing the relationship (longer, shorter, equal)
        """
        if len(text1) > len(text2):
            return "longer"
        elif len(text1) < len(text2):
            return "shorter"
        else:
            return "equal" 