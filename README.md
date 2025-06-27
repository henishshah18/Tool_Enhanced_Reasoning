# Tool-Enhanced Reasoning Script

A Python script that implements Chain-of-Thought (CoT) reasoning with sequential tool execution using OpenAI's GPT-4o-mini. The system breaks down natural language queries into logical steps, plans tool usage, and executes tools sequentially to produce accurate answers.

## 🎯 Project Overview

This project demonstrates a simple yet effective approach to tool-enhanced reasoning without using complex frameworks like LangChain. It follows the [OpenAI Cookbook pattern](https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models) for function calling with a custom CoT planning layer.

## ✨ Features

- **Chain-of-Thought Reasoning**: LLM breaks down complex queries into logical steps
- **Sequential Tool Execution**: Tools run one by one with result sharing
- **Mathematical Operations**: Average, square root, addition, multiplication, comparison
- **String Analysis**: Vowel counting, letter counting, word counting, number extraction
- **Robust Error Handling**: Graceful handling of API failures and tool errors
- **Clear Debugging**: Step-by-step execution visibility

## 🏗️ Project Structure

```
Assignment4.3/
├── main.py                 # Main reasoning script with CoT + sequential execution
├── function_specs.py       # OpenAI function specifications
├── tools/
│   ├── __init__.py        # Package initialization
│   ├── math_tools.py      # Mathematical operations (implemented)
│   └── string_tools.py    # String operations (implemented)
├── README.md              # This file
├── requirements.txt       # Python dependencies
└── env_example.txt        # Environment setup instructions
```

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Assignment4.3
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
1. Copy `env_example.txt` to `.env`:
   ```bash
   cp env_example.txt .env
   ```

2. Add your OpenAI API key to the `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   **Get your API key from**: [OpenAI Platform](https://platform.openai.com/api-keys)

### 4. Run the Script
```bash
python main.py
```

## 📋 Example Queries and Outputs

### 1. Mathematical Query: Square Root of Average
**Query:** "What's the square root of the average of 18 and 50?"

**Output:**
```
Step 1: Planning execution...
Reasoning: First, I need to calculate the average of 18 and 50. Then, I will take the square root of that average.
Planned tools: ['calculate_average', 'calculate_square_root']

Step 2: Executing tools...
  Step 1: Executing calculate_average
    Arguments: {'numbers': [18, 50]}
    Result: 34.0
  Step 2: Executing calculate_square_root
    Arguments: {'number': 34}
    Result: 5.830951894845301

Final Answer: The square root of the average of 18 and 50 is approximately 5.83.
```

### 2. String Analysis: Vowel Counting
**Query:** "How many vowels are in the word 'Multimodality'?"

**Output:**
```
Step 1: Planning execution...
Reasoning: To determine the number of vowels in the word 'Multimodality', I will use the tool that specifically counts vowels in a given string.
Planned tools: ['count_vowels']

Step 2: Executing tools...
  Step 1: Executing count_vowels
    Arguments: {'text': 'Multimodality'}
    Result: 5

Final Answer: The word 'Multimodality' contains 5 vowels.
```

### 3. Complex Comparison: Letters vs Vowels
**Query:** "Is the number of letters in 'machine' greater than the number of vowels in 'reasoning'?"

**Output:**
```
Step 1: Planning execution...
Reasoning: 1. First, I need to count the number of letters in the word "machine."
2. Next, I will count the number of vowels in the word "reasoning."
3. Finally, I will compare the two results to determine if the number of letters in "machine" is greater than the number of vowels in "reasoning."
Planned tools: ['count_letters', 'count_vowels', 'compare_numbers']

Step 2: Executing tools...
  Step 1: Executing count_letters
    Arguments: {'text': 'machine'}
    Result: 7
  Step 2: Executing count_vowels
    Arguments: {'text': 'reasoning'}
    Result: 4
  Step 3: Executing compare_numbers
    Arguments: {'a': 7, 'b': 4}
    Result: greater

Final Answer: Yes, the number of letters in 'machine' is greater than the number of vowels in 'reasoning'.
```

### 4. Mathematical Operations: Addition and Division
**Query:** "What is 15 plus 27 divided by 3?"

**Expected Output:**
```
Step 1: Planning execution...
Reasoning: I need to perform the division first (27/3 = 9), then add 15 to the result.
Planned tools: ['add_numbers']

Step 2: Executing tools...
  Step 1: Executing add_numbers
    Arguments: {'numbers': [15, 9]}
    Result: 24

Final Answer: 15 plus 27 divided by 3 equals 24.
```

### 5. String Length Comparison
**Query:** "Which word is longer: 'artificial' or 'intelligence'?"

**Expected Output:**
```
Step 1: Planning execution...
Reasoning: I need to count the letters in both words and compare their lengths.
Planned tools: ['compare_string_lengths']

Step 2: Executing tools...
  Step 1: Executing compare_string_lengths
    Arguments: {'text1': 'artificial', 'text2': 'intelligence'}
    Result: shorter

Final Answer: 'Intelligence' is longer with 12 letters compared to 'artificial' with 10 letters.
```

## 🧠 How the CoT Prompt Helps Decide Tool Usage

The system uses a structured Chain-of-Thought approach with three distinct phases:

### **Phase 1: Planning (CoT Reasoning)**
The LLM receives a structured prompt that instructs it to:
1. **Think step by step** about the problem
2. **Identify required operations** (mathematical, string analysis, etc.)
3. **Plan tool sequence** in logical order
4. **Output structured format**:
   ```
   REASONING: [Step-by-step analysis]
   
   TOOLS:
   tool_name_1
   tool_name_2
   tool_name_3
   ```

### **Phase 2: Sequential Execution**
The system executes tools one by one:
1. **Extract clean tool names** from the plan
2. **Call each tool individually** with proper arguments
3. **Add results to conversation** for next tool
4. **Handle errors gracefully** with fallback responses

### **Phase 3: Final Answer Generation**
The LLM combines:
- Original reasoning
- All tool results
- Context from the query
- Generates a comprehensive final answer

## 🔧 Implementation Details

### **Tool Specifications (`function_specs.py`)**
- Defines all available tools in OpenAI's function specification format
- Separates math and string tools for modularity
- Provides clear descriptions and parameter requirements

### **Sequential Execution (`main.py`)**
- Implements the 3-phase process: Plan → Execute → Answer
- Uses fresh conversation context for each tool call
- Maintains proper message flow for OpenAI API

### **Tool Implementation (`tools/`)**
- **Math Tools**: `calculate_average`, `calculate_square_root`, `add_numbers`, `multiply_numbers`, `compare_numbers`
- **String Tools**: `count_vowels`, `count_letters`, `count_words`, `extract_numbers`, `compare_string_lengths`
- All tools are fully implemented with proper error handling

## 🛠️ Dependencies

- `openai>=1.0.0`: OpenAI API client
- `python-dotenv>=1.0.0`: Environment variable management

## 🔑 API Key Setup

1. **Get your OpenAI API key** from [OpenAI Platform](https://platform.openai.com/api-keys)
2. **Create a `.env` file** in the project root
3. **Add your API key**: `OPENAI_API_KEY=your_key_here`

## 🚀 Usage Examples

### Basic Usage
```bash
python main.py
```

### Custom Queries
You can modify the `test_queries` list in `main.py` to test different queries:

```python
test_queries = [
    "What's the square root of the average of 18 and 50?",
    "How many vowels are in the word 'Multimodality'?",
    "Is the number of letters in 'machine' greater than the number of vowels in 'reasoning'?",
    "What is 15 plus 27 divided by 3?",
    "Which word is longer: 'artificial' or 'intelligence'?"
]
```

## 🎯 Key Learning Outcomes

This project demonstrates:
- **Chain-of-Thought reasoning** without complex frameworks
- **Sequential tool execution** with result sharing
- **OpenAI function calling** best practices
- **Error handling** and debugging techniques
- **Modular tool design** for extensibility

## 🔄 Extending the System

You can easily extend the system by:
1. **Adding new tools** to `function_specs.py` and `tools/` directory
2. **Improving the planning prompt** for better reasoning
3. **Adding more complex query types**
4. **Implementing parallel tool calling** for independent operations

## 📝 Contributing

This is a learning assignment. Feel free to:
- Add more tools and capabilities
- Improve error handling and logging
- Enhance the reasoning prompts
- Add unit tests for tools
- Implement more complex query types

## 📄 License

This project is for educational purposes. Feel free to use and modify as needed. 