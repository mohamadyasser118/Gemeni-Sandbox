import os 
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_functions import available_functions, call_function  


# Setup argparse to accept user prompt from command line
parser = argparse.ArgumentParser(description="AI Agent using Gemini API")
parser.add_argument(
    'user_prompt', 
     type=str, 
     help='The prompt to generate a response for')

parser.add_argument(
    "--verbose",
    action="store_true",
    help="Enable verbose output"
)
args = parser.parse_args()

# Load environment variables from .env file
load_dotenv() 
# Get the Gemini API key from environment variables
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

# Initialize the Gemini API client
client = genai.Client(api_key=GEMINI_API_KEY)


def main():
    """Main agent loop."""
    # Initialize conversation history with the user's initial prompt
    messages = [
        types.Content(
            role="user",
            parts=[types.Part(text=args.user_prompt)]
        )
    ]
    
    # Agentic loop - max 20 iterations
    MAX_ITERATIONS = 20
    for iteration in range(MAX_ITERATIONS):
        if args.verbose:
            print(f"\n=== Iteration {iteration + 1} ===")
        
        # Call the model with full conversation history
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt
            ),
        )
        
        # Check metadata
        if response.usage_metadata is None:
            raise RuntimeError("Response metadata is missing. Please check the API response.")
        
        # Calculate token usage
        prompt_tokens = response.usage_metadata.prompt_token_count     
        response_tokens = response.usage_metadata.candidates_token_count
        total_tokens = prompt_tokens + response_tokens
        
        # Print token usage if verbose flag is set
        if args.verbose:
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")
            print(f"Total tokens: {total_tokens}")
        
        # Add model's response candidates to conversation history
        if response.candidates:
            for candidate in response.candidates:
                if candidate.content:
                    messages.append(candidate.content)
        
        # Check if the model produced a final response (no function calls)
        if not response.function_calls:
            # Model has produced a final response
            if response.text:
                print(response.text)
            break
        
        # Process function calls
        function_responses = []
        for function_call in response.function_calls:
            # Call the function and get the result
            function_call_result = call_function(function_call, args.verbose)
            
            # Validate the response structure
            if not function_call_result.parts:
                raise RuntimeError("Function call result has no parts")
            
            if function_call_result.parts[0].function_response is None:
                raise RuntimeError("Function response is None")
            
            if function_call_result.parts[0].function_response.response is None:
                raise RuntimeError("Function response data is None")
            
            # Store the result
            function_responses.append(function_call_result.parts[0])
            
            # Print result if verbose
            if args.verbose:
                response_data = function_call_result.parts[0].function_response.response
                print(f"-> {response_data}")
        
        # Add function results to conversation history for next iteration
        if function_responses:
            messages.append(types.Content(role="user", parts=function_responses))
    else:
        # Maximum iterations reached without a final response
        print(f"Error: Agent did not produce a final response after {MAX_ITERATIONS} iterations.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()