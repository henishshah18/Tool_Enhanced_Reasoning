"""
Function specifications for the tool-enhanced reasoning system.
This file contains the tool definitions that will be passed to the OpenAI API.
"""

def get_math_tools():
    """Return mathematical tool specifications."""
    return [
        {
            "type": "function",
            "function": {
                "name": "calculate_average",
                "description": "Calculate the average of a list of numbers",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "numbers": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "List of numbers to calculate the average of"
                        }
                    },
                    "required": ["numbers"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "calculate_square_root",
                "description": "Calculate the square root of a number",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "number": {
                            "type": "number",
                            "description": "Number to find the square root of"
                        }
                    },
                    "required": ["number"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "add_numbers",
                "description": "Add a list of numbers together",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "numbers": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "List of numbers to add"
                        }
                    },
                    "required": ["numbers"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "multiply_numbers",
                "description": "Multiply a list of numbers together",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "numbers": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "List of numbers to multiply"
                        }
                    },
                    "required": ["numbers"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "compare_numbers",
                "description": "Compare two numbers and return their relationship",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {
                            "type": "number",
                            "description": "First number to compare"
                        },
                        "b": {
                            "type": "number",
                            "description": "Second number to compare"
                        }
                    },
                    "required": ["a", "b"]
                }
            }
        }
    ]

def get_string_tools():
    """Return string manipulation tool specifications."""
    return [
        {
            "type": "function",
            "function": {
                "name": "count_vowels",
                "description": "Count the number of vowels (a, e, i, o, u) in a text",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {
                            "type": "string",
                            "description": "Text to count vowels in"
                        }
                    },
                    "required": ["text"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "count_letters",
                "description": "Count the number of letters in a text (excluding spaces and punctuation)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {
                            "type": "string",
                            "description": "Text to count letters in"
                        }
                    },
                    "required": ["text"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "count_words",
                "description": "Count the number of words in a text",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {
                            "type": "string",
                            "description": "Text to count words in"
                        }
                    },
                    "required": ["text"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "extract_numbers",
                "description": "Extract all numbers from a text string",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {
                            "type": "string",
                            "description": "Text to extract numbers from"
                        }
                    },
                    "required": ["text"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "compare_string_lengths",
                "description": "Compare the lengths of two strings",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text1": {
                            "type": "string",
                            "description": "First string to compare"
                        },
                        "text2": {
                            "type": "string",
                            "description": "Second string to compare"
                        }
                    },
                    "required": ["text1", "text2"]
                }
            }
        }
    ]

def get_all_tools():
    """Return all available tool specifications."""
    return get_math_tools() + get_string_tools() 