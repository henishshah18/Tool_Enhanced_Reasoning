import math
from typing import List, Union

class MathTools:
    """Class containing mathematical tool functions."""
    
    def calculate_average(self, numbers: List[Union[int, float]]) -> float:
        """
        Calculate the average of a list of numbers.
        
        Args:
            numbers: List of numbers to average
            
        Returns:
            Average of the numbers
        """
        return sum(numbers) / len(numbers)
    
    def calculate_square_root(self, number: Union[int, float]) -> float:
        """
        Calculate the square root of a number.
        
        Args:
            number: Number to find square root of
            
        Returns:
            Square root of the number
        """
        return math.sqrt(number)
    
    def add_numbers(self, numbers: List[Union[int, float]]) -> Union[int, float]:
        """
        Add a list of numbers.
        
        Args:
            numbers: List of numbers to add
            
        Returns:
            Sum of the numbers
        """
        return sum(numbers)
    
    def multiply_numbers(self, numbers: List[Union[int, float]]) -> Union[int, float]:
        """
        Multiply a list of numbers.
        
        Args:
            numbers: List of numbers to multiply
            
        Returns:
            Product of the numbers
        """
        result = 1
        for num in numbers:
            result *= num
        return result
    
    def compare_numbers(self, a: Union[int, float], b: Union[int, float]) -> str:
        """
        Compare two numbers and return the relationship.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            String describing the relationship (greater, less, equal)
        """
        if a > b:
            return "greater"
        elif a < b:
            return "less"
        else:
            return "equal" 