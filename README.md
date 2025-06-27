# Tool-Enhanced Reasoning Script

A simple Python script that uses OpenAI's GPT-4.1-mini to interpret natural language queries, perform chain-of-thought reasoning, and call external tools when necessary to produce final answers. This implementation follows the [OpenAI Cookbook pattern](https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models) for function calling.

## Features

- Chain-of-thought (CoT) style reasoning using OpenAI's GPT-4o-mini
- Automatic tool detection and execution using OpenAI's function calling API
- Mathematical operations (average, square root, addition, multiplication, comparison)
- String operations (vowel counting, letter counting, word counting, number extraction, length comparison)
- Retry logic for API calls with exponential backoff
- Pretty-printed conversation debugging

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd Assignment4.3
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
   - Copy `env_example.txt` to `.env`
   - Add your OpenAI API key to the `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

Run the main script:
```bash
python main.py
```

The script will process example queries and display:
- The LLM's reasoning steps
- Whether a tool was used
- Tool results (if any)
- The final answer

## Project Structure

```
├── main.py                 # Main reasoning script (OpenAI cookbook pattern)
├── function_specs.py       # Function specifications for OpenAI API
├── tools/
│   ├── __init__.py        # Package initialization
│   ├── math_tools.py      # Mathematical operations
│   └── string_tools.py    # String operations
├── README.md              # This file
├── requirements.txt       # Python dependencies
└── env_example.txt        # Environment setup instructions
```

## Example Queries and Expected Output

### 1. Mathematical Query
**Query:** "What's the square root of the average of 18 and 50?"

**Expected Output:**
- Reasoning: "I need to find the average of 18 and 50 first, then take the square root of that result."
- Tool Used: Multiple tools
- Tool Results:
  - calculate_average: 34.0
  - calculate_square_root: 5.830951894845301
- Final Answer: "The square root of the average of 18 and 50 is approximately 5.83"

### 2. String Analysis Query
**Query:** "How many vowels are in the word 'Multimodality'?"

**Expected Output:**
- Reasoning: "I need to count the vowels (a, e, i, o, u) in the word 'Multimodality'."
- Tool Used: Single tool
- Tool Results:
  - count_vowels: 5
- Final Answer: "There are 5 vowels in the word 'Multimodality'."

### 3. Comparison Query
**Query:** "Is the number of letters in 'machine' greater than the number of vowels in 'reasoning'?"

**Expected Output:**
- Reasoning: "I need to count letters in 'machine' and vowels in 'reasoning', then compare them."
- Tool Used: Multiple tools
- Tool Results:
  - count_letters: 7
  - count_vowels: 4
  - compare_numbers: greater
- Final Answer: "Yes, 'machine' has 7 letters which is greater than the 4 vowels in 'reasoning'."

### 4. Complex Mathematical Query
**Query:** "What is 15 plus 27 divided by 3?"

**Expected Output:**
- Reasoning: "I need to perform the division first (27/3 = 9), then add 15 to the result."
- Tool Used: Multiple tools
- Tool Results:
  - add_numbers: 24
- Final Answer: "15 plus 27 divided by 3 equals 24."

### 5. String Length Comparison
**Query:** "Which word is longer: 'artificial' or 'intelligence'?"

**Expected Output:**
- Reasoning: "I need to count the letters in both words and compare their lengths."
- Tool Used: Multiple tools
- Tool Results:
  - compare_string_lengths: longer
- Final Answer: "'Intelligence' is longer with 12 letters compared to 'artificial' with 10 letters."

## How the Implementation Works

This implementation follows the [OpenAI Cookbook pattern](https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models) for function calling:

### 1. Function Specifications (`function_specs.py`)
- Defines all available tools in OpenAI's function specification format
- Separates math and string tools for modularity
- Provides clear descriptions and parameter requirements

### 2. Tool Execution (`main.py`)
- Uses OpenAI's `tools` parameter to provide function specifications
- Implements the 4-step process:
  1. **Initial Request**: Send query with tools available
  2. **Tool Detection**: Check if model wants to call tools
  3. **Tool Execution**: Execute tools with model-generated arguments
  4. **Final Response**: Get final answer from model with tool results

### 3. Error Handling
- Retry logic with exponential backoff for API calls
- Graceful error handling for tool execution
- Clear error messages for debugging

## Implementation Notes

- **OpenAI Function Calling**: Uses OpenAI's native function calling API instead of manual parsing
- **Retry Logic**: Implements robust retry mechanism for API calls
- **Modular Design**: Tools are implemented as simple Python functions
- **Type Safety**: Proper type hints throughout the codebase
- **Debugging Support**: Pretty-printed conversation output for development

## API Key Setup

1. Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create a `.env` file in the project root
3. Add your API key: `OPENAI_API_KEY=your_key_here`

## Dependencies

- `openai`: OpenAI API client
- `python-dotenv`: Environment variable management
- `tenacity`: Retry logic for API calls
- `termcolor`: Colored output for debugging

## Contributing

This is a learning assignment. Feel free to extend the functionality by:
- Adding more tools to `function_specs.py`
- Improving the system prompt for better reasoning
- Enhancing error handling and logging
- Adding more complex query types
- Implementing parallel tool calling for complex queries 