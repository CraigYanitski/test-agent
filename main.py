import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

import call_function as cf
from config import MAX_ITERATIONS
from prompt import system_prompt


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

    
    # Print prompt if verbose output
    if verbose:
        print("\n-- Conversation --\n")
        print(f"User prompt: {prompt}\n")

    # Print response
    for _ in range(MAX_ITERATIONS):
        response = client.models.generate_content(
            model=model_name, 
            contents=messages,
            config=types.GenerateContentConfig(
                tools=available_functions,
                system_instruction=system_prompt,
            ),
        )

        for variant in response.candidates:
            messages.append(variant.content)
        if response.function_calls:
            for c in response.function_calls:
                out = cf.call_function(c, verbose=verbose)
                messages.append(out)
                try:
                    resp = out.parts[0].function_response.response
                except:
                    raise ValueError("function response not in function return; need type `types.Content`")
                if verbose:
                    print(f"-> {resp['result']}")
            # Print token number if verbose output
            if verbose:
                print("\n-- Tokens --")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}\n")
        else:
            print()
            # print("No functions calls were requested.\n")
            break
    print(f"Response: {response.text}\n")
    
    return 0

if __name__ == "__main__":
    main()
