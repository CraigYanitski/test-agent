import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    args = sys.argv[1:]

    if not args:
        print("missing prompt: need to pass a prompt as an argument")
        exit(1)

    if args[0] == "--verbose":
        print("--verbose argument must follow prompt.")
        exit(1)

    # Check if verbose argument is specified
    if "--verbose" in args:
        verbose = True
    else:
        verbose = False

    prompt = args[0]
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model_name = "gemini-2.0-flash-001"
    
    # Available Functions
    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            }
        ),
    )
    schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Return the content of the specified file, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file path of the file whose contents should be returned, relative to the working directory. Must be provided.",
                ),
            }
        ),
    )
    schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Writes the content of the specified file with a provided string, constrained to the working directory. It will create the file if it does not exist.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file path of the file that should be (over)written, relative to the working directory. Must be provided.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The content that should be written to the specified file. Must be provided.",
                ),
            }
        ),
    )
    schema_run_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Executes the specified Python file, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file path of the file that should be executed, relative to the working directory. Must be provided.",
                ),
            }
        ),
    )

    available_functions = [
        types.Tool(
            function_declarations=[
                schema_get_files_info,
            ]
        ),
        types.Tool(
            function_declarations=[
                schema_get_file_content,
            ]
        ),
        types.Tool(
            function_declarations=[
                schema_write_file,
            ]
        ),
        types.Tool(
            function_declarations=[
                schema_run_file,
            ]
        ),
    ]

    system_prompt = '''
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    '''

    response = client.models.generate_content(
        model=model_name, 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=available_functions,
            system_instruction=system_prompt,
        ),
    )
    
    # Print prompt if verbose output
    if verbose:
        print("\n-- Conversation --\n")
        print(f"User prompt: {prompt}\n")

    # Print response
    print(f"Response: {response.text}\n")
    if len(response.function_calls):
        for c in response.function_calls:
            print(f"Calling function: {c.name}({c.args})")
        print()
    else:
        print("No functions calls were requested.\n")

    # Print token number if verbose output
    if verbose:
        print("\n-- Tokens --")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}\n")
    
    return 0

if __name__ == "__main__":
    main()
