import os
import json
from typing import Dict, Any, List
from dotenv import load_dotenv
from openai import OpenAI

from tools.math_tools import MathTools
from tools.string_tools import StringTools
from function_specs import get_all_tools

# Load environment variables
load_dotenv()

class ToolEnhancedReasoning:
    def __init__(self):
        """Initialize the reasoning system with tools."""
        self.math_tools = MathTools()
        self.string_tools = StringTools()
        self.api_key = os.getenv('OPENAI_API_KEY')
        
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    def chat_completion_request(self, messages, tools=None, tool_choice=None, model="gpt-4o-mini"):
        """Make a request to the Chat Completions API."""
        try:
            client = OpenAI(api_key=self.api_key)
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                tools=tools,
                tool_choice=tool_choice,
            )
            return response
        except Exception as e:
            print(f"API Error: {e}")
            return None
    
    def plan_execution(self, query: str) -> Dict[str, Any]:
        """
        Step 1: Get the LLM to plan the execution using CoT reasoning.
        
        Args:
            query: The natural language query
            
        Returns:
            Dictionary with reasoning and tool plan
        """
        messages = [
            {
                "role": "system",
                "content": """You are a helpful assistant that plans how to solve problems using tools.

When given a query, think through it step by step and plan which tools you need to use.

IMPORTANT: You must respond in EXACTLY this format:

REASONING: [Your step-by-step reasoning here]

TOOLS:
tool_name_1
tool_name_2
tool_name_3

Available tools (use ONLY these exact names):
- calculate_average
- calculate_square_root
- add_numbers
- multiply_numbers
- compare_numbers
- count_vowels
- count_letters
- count_words
- extract_numbers
- compare_string_lengths

Rules:
1. List ONLY the tool names, one per line
2. Do NOT include arguments, brackets, or extra text
3. Do NOT include dashes or bullet points
4. Use the exact tool names as shown above
5. Order them in the sequence they should be executed"""
            },
            {
                "role": "user",
                "content": query
            }
        ]
        
        response = self.chat_completion_request(messages)
        if not response:
            return {"reasoning": "Failed to plan", "tools": []}
        
        content = response.choices[0].message.content
        
        # Parse the response with better error handling
        reasoning = ""
        tools = []
        
        # Extract reasoning
        if "REASONING:" in content:
            reasoning_part = content.split("REASONING:")[1]
            if "TOOLS:" in reasoning_part:
                reasoning = reasoning_part.split("TOOLS:")[0].strip()
            else:
                reasoning = reasoning_part.strip()
        
        # Extract tools
        if "TOOLS:" in content:
            tools_section = content.split("TOOLS:")[1].strip()
            # Split by lines and clean each tool name
            tool_lines = tools_section.split('\n')
            for line in tool_lines:
                line = line.strip()
                # Remove any extra characters and get clean tool name
                if line:
                    # Remove common prefixes/suffixes
                    clean_tool = line.replace('-', '').replace('*', '').replace('•', '').strip()
                    # Remove any arguments in brackets
                    if '(' in clean_tool:
                        clean_tool = clean_tool.split('(')[0].strip()
                    # Remove any comments after #
                    if '#' in clean_tool:
                        clean_tool = clean_tool.split('#')[0].strip()
                    # Only add if it's a valid tool name
                    if clean_tool and len(clean_tool) <= 64:  # OpenAI limit
                        tools.append(clean_tool)
        
        return {
            "reasoning": reasoning,
            "tools": tools
        }
    
    def execute_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        """Execute a single tool."""
        try:
            print(f"    Executing {tool_name} with arguments: {arguments}")
            print(f"    Argument types: {[(k, type(v)) for k, v in arguments.items()]}")
            
            # Math tools
            if tool_name == "calculate_average":
                result = self.math_tools.calculate_average(arguments["numbers"])
                print(f"    calculate_average result: {result} (type: {type(result)})")
                return result
            elif tool_name == "calculate_square_root":
                result = self.math_tools.calculate_square_root(arguments["number"])
                print(f"    calculate_square_root result: {result} (type: {type(result)})")
                return result
            elif tool_name == "add_numbers":
                result = self.math_tools.add_numbers(arguments["numbers"])
                print(f"    add_numbers result: {result} (type: {type(result)})")
                return result
            elif tool_name == "multiply_numbers":
                result = self.math_tools.multiply_numbers(arguments["numbers"])
                print(f"    multiply_numbers result: {result} (type: {type(result)})")
                return result
            elif tool_name == "compare_numbers":
                result = self.math_tools.compare_numbers(arguments["a"], arguments["b"])
                print(f"    compare_numbers result: {result} (type: {type(result)})")
                return result
            
            # String tools
            elif tool_name == "count_vowels":
                result = self.string_tools.count_vowels(arguments["text"])
                print(f"    count_vowels result: {result} (type: {type(result)})")
                return result
            elif tool_name == "count_letters":
                result = self.string_tools.count_letters(arguments["text"])
                print(f"    count_letters result: {result} (type: {type(result)})")
                return result
            elif tool_name == "count_words":
                result = self.string_tools.count_words(arguments["text"])
                print(f"    count_words result: {result} (type: {type(result)})")
                return result
            elif tool_name == "extract_numbers":
                result = self.string_tools.extract_numbers(arguments["text"])
                print(f"    extract_numbers result: {result} (type: {type(result)})")
                return result
            elif tool_name == "compare_string_lengths":
                result = self.string_tools.compare_string_lengths(arguments["text1"], arguments["text2"])
                print(f"    compare_string_lengths result: {result} (type: {type(result)})")
                return result
            else:
                error_msg = f"Error: Unknown tool {tool_name}"
                print(f"    {error_msg}")
                return error_msg
        except Exception as e:
            error_msg = f"Error executing {tool_name}: {str(e)}"
            print(f"    {error_msg}")
            print(f"    Exception type: {type(e)}")
            import traceback
            print(f"    Traceback: {traceback.format_exc()}")
            return error_msg
    
    def execute_tools_sequentially(self, tools: List[str], query: str) -> List[Dict[str, Any]]:
        """
        Step 2: Execute tools sequentially based on the plan.
        
        Args:
            tools: List of tool names to execute
            query: Original query for context
            
        Returns:
            List of tool results
        """
        results = []
        messages = [
            {
                "role": "system",
                "content": """You are a helpful assistant. Use tools when needed to answer the user's question.
                
When calling a tool, provide the appropriate arguments based on the context and previous results.
For mathematical operations, extract numbers from the query or use results from previous tools.
For string operations, use the text specified in the query."""
            },
            {
                "role": "user",
                "content": query
            }
        ]
        
        for i, tool_name in enumerate(tools):
            print(f"  Step {i+1}: Executing {tool_name}")
            
            # Create a fresh conversation for each tool call
            current_messages = messages.copy()
            
            # Add context about previous results if any
            if results:
                context = f"\nPrevious results: {[f'{r['tool']}: {r['result']}' for r in results]}"
                current_messages.append({
                    "role": "user",
                    "content": f"Now call {tool_name}. {context}"
                })
            
            # Ask LLM to call the specific tool
            response = self.chat_completion_request(
                current_messages, 
                tools=get_all_tools(), 
                tool_choice={"type": "function", "function": {"name": tool_name}}
            )
            
            if not response or not response.choices[0].message.tool_calls:
                print(f"    Failed to call {tool_name}")
                continue
            
            # Execute the tool
            tool_call = response.choices[0].message.tool_calls[0]
            function_args = json.loads(tool_call.function.arguments)
            
            print(f"    Arguments: {function_args}")
            
            tool_result = self.execute_tool(tool_name, function_args)
            print(f"    Result: {tool_result}")
            
            results.append({
                "tool": tool_name,
                "arguments": function_args,
                "result": tool_result
            })
            
            # Add the assistant message and tool result to the main conversation
            messages.append(response.choices[0].message)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_name,
                "content": str(tool_result)
            })
        
        return results
    
    def generate_final_answer(self, query: str, reasoning: str, tool_results: List[Dict[str, Any]]) -> str:
        """
        Step 3: Generate final answer using the reasoning and tool results.
        
        Args:
            query: Original query
            reasoning: Initial reasoning
            tool_results: Results from tool execution
            
        Returns:
            Final answer
        """
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant. Provide a clear final answer based on the reasoning and tool results."
            },
            {
                "role": "user",
                "content": f"""Query: {query}
                
Reasoning: {reasoning}

Tool Results:
{chr(10).join([f"- {result['tool']}: {result['result']}" for result in tool_results]) if tool_results else "No tools were successfully executed"}

Please provide a clear final answer. If tools failed, provide the answer based on your knowledge."""
            }
        ]
        
        response = self.chat_completion_request(messages)
        if not response:
            return "Failed to generate final answer"
        
        return response.choices[0].message.content
    
    def process_query(self, query: str) -> Dict[str, Any]:
        """
        Main method: Plan, execute, and answer.
        
        Args:
            query: The natural language query
            
        Returns:
            Dictionary containing reasoning, tool usage, and final answer
        """
        print(f"Processing: {query}")
        
        # Step 1: Plan the execution
        print("Step 1: Planning execution...")
        plan = self.plan_execution(query)
        print(f"Reasoning: {plan['reasoning']}")
        print(f"Planned tools: {plan['tools']}")
        
        # Step 2: Execute tools sequentially
        print("Step 2: Executing tools...")
        tool_results = self.execute_tools_sequentially(plan['tools'], query)
        
        # Step 3: Generate final answer
        print("Step 3: Generating final answer...")
        final_answer = self.generate_final_answer(query, plan['reasoning'], tool_results)
        
        return {
            "reasoning": plan['reasoning'],
            "tool_used": f"{len(tool_results)} tools" if tool_results else "None",
            "tool_results": tool_results,
            "final_answer": final_answer
        }

def main():
    """Main function to run the tool-enhanced reasoning script."""
    reasoning_system = ToolEnhancedReasoning()
    
    # Example queries for testing
    test_queries = [
        "What's the square root of the average of 18 and 50?",
        "How many vowels are in the word 'Multimodality'?",
        "Is the number of letters in 'machine' greater than the number of vowels in 'reasoning'?"
    ]
    
    for query in test_queries:
        print(f"\n{'='*60}")
        print(f"Query: {query}")
        print(f"{'='*60}")
        
        try:
            result = reasoning_system.process_query(query)
            
            print(f"\nFinal Results:")
            print(f"Reasoning: {result['reasoning']}")
            print(f"Tool Used: {result['tool_used']}")
            
            if result['tool_results']:
                print("Tool Results:")
                for tool_result in result['tool_results']:
                    print(f"  - {tool_result['tool']}: {tool_result['result']}")
            
            print(f"Final Answer: {result['final_answer']}")
            
        except Exception as e:
            print(f"Error processing query: {e}")

if __name__ == "__main__":
    main() 